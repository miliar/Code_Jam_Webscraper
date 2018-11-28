#include <iostream>
#include<fstream>

using namespace std;

void check_win(char mat[4][4], fstream &obj,int test_case);
int check_rows(char mat[4][4]);
int check_diag(char mat[4][4]);
int check_col(char mat[4][4]);
void dump(char mat[4][4],int t);

int main()
{
    int T; //no. of test cases
    char grid[4][4];
    fstream fin("input.in",ios::in);
    fstream fout("output.out",ios::out);
    if(!fin || !fout)
    {
        return -1;
    }
    else
    {
        while(!fin.eof())
        {
            fin>>T;
            for(int i=1;i<=T;i++)
            {
                if(fin.tellg()==-1)
                break;
                for(int j=0;j<4;j++)
                {
                    for(int k=0;k<4;k++)
                    {
                        fin>>grid[j][k];
                    }
                }
                dump(grid,i);
                check_win(grid, fout,i);
            }
            }
        fin.close();
        fout.close();
    }
    return 0;
}

int check_rows(char mat[4][4])
{
    int numX, numO,eflag=0;
    for(int i=0;i<4;i++)
    {
        numX=0,numO=0;
        for(int j=0;j<4;j++)
        {
            if(mat[i][j]=='X' || mat[i][j]=='x')
             numX++;
            else if(mat[i][j]=='O' || mat[i][j]=='o')
             numO++;
             else if(mat[i][j]=='T' || mat[i][j]=='t')
             {
                 if(numX>0 && numO==0)
                  numX++;
                  else if(numO>0 && numX==0)
                  numO++;
                  else if(numX==0 && numO==0)
                  {
                      numX++;
                      numO++;
                  }
                  else
                  j=10; //just to exit j loop without using break
             }
             else
             eflag=1;
        }
        if(numX==4)
         return 1;
        if(numO==4)
         return 2;
    }
    if(eflag==1)
          return -1;
    return 0;
}

int check_col(char mat[4][4])
{
    int numX, numO,eflag=0;
    for(int i=0;i<4;i++)
    {
        numX=0,numO=0;
        for(int j=0;j<4;j++)
        {
            if(mat[j][i]=='X' || mat[j][i]=='x')
             numX++;
            else if(mat[j][i]=='O' || mat[j][i]=='o')
             numO++;
            else if(mat[j][i]=='T' || mat[j][i]=='t')
             {
                 if(numX>0 && numO==0)
                  numX++;
                  else if(numO>0 && numX==0)
                  numO++;
                  else if(numX==0 && numO==0)
                  {
                      numX++;
                      numO++;
                  }
                  else
                  j=10; //just to exit j loop without using break
             }
             else eflag=1;
        }
        if(numX==4)
         return 1;
        if(numO==4)
         return 2;

    }
    if(eflag==1)
          return -1;
    return 0;
}

int check_diag(char mat[4][4])
{
    int numX_p=0, numO_p=0,numX_s=0,numO_s=0;
    for(int i=0;i<4;i++)
    {
        if(mat[i][i]=='X' || mat[i][i]=='x')
        numX_p++;
        if(mat[i][i]=='O' || mat[i][i]=='o')
        numO_p++;
        if(mat[i][i]=='T' || mat[i][i]=='t')
             {
                 if(numX_p>0 && numO_p==0)
                  numX_p++;
                  else if(numO_p>0 && numX_p==0)
                  numO_p++;
                  else if(numX_p==0 && numO_p==0)
                  {
                      numX_p++;
                      numO_p++;
                  }
                  else
                  {

                  }
             }
        if(mat[3-i][i]=='X' || mat[3-i][i]=='x')
        numX_s++;
        if(mat[3-i][i]=='O' || mat[3-i][i]=='o')
        numO_s++;
        if(mat[3-i][i]=='T' || mat[3-i][i]=='t')
             {
                 if(numX_s>0 && numO_s==0)
                  numX_s++;
                  else if(numO_s>0 && numX_s==0)
                  numO_s++;
                  else if(numX_s==0 && numO_s==0)
                  {
                      numX_s++;
                      numO_s++;
                  }
                  else
                  {

                  }
             }
    }
    if(numX_p==4 || numX_s==4)
    return 1;
    else if(numO_p==4 || numO_s==4)
    return 2;
    else
    return 0;
}

void check_win(char mat[4][4],fstream &obj,int test_case)
{
    int xwon=0,owon=0,draw=0,incomplete=0;
    if(check_rows(mat)==0 && check_col(mat)==0 && check_diag(mat)==0)
    {
        draw=1;
    }
    if(check_rows(mat)==-1 && check_col(mat)==-1)
    {
        incomplete=1;
    }
    if(check_rows(mat)==1 || check_col(mat)==1 || check_diag(mat)==1)
    {
        xwon=1;
    }
    if(check_rows(mat)==2 || check_col(mat)==2 || check_diag(mat)==2)
    {
        owon=1;
    }

    if(xwon==1)
    {
        obj<<"Case #"<<test_case<<": X won"<<endl;
        return;
    }
    if(owon==1)
    {
        obj<<"Case #"<<test_case<<": O won"<<endl;
        return;
    }
    if(draw==1)
    {
        obj<<"Case #"<<test_case<<": Draw"<<endl;
        return;
    }
    if(incomplete==1)
    {
        obj<<"Case #"<<test_case<<": Game has not completed"<<endl;
        return;
    }
}

void dump(char mat[4][4],int t)
{
    fstream dumper("dumper.txt",ios::out | ios::app);

        dumper<<"Case "<<t<<endl;
        for(int i=0;i<4;i++)
        {
            for(int j=0;j<4;j++)
             dumper<<mat[i][j];
        }
        dumper<<endl;
  dumper.close();
}
