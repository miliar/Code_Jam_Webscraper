#include<iostream>
#include<cstdio>
#include<fstream>
using namespace std;

int main()
{
    int test,i,j,k,state=0,flag,noleft;
    char mat[5][5];
    char ch;
    int matx[4][4],mato[4][4],row[4],col[4];
    ifstream ifile;
    ofstream ofile;
    ifile.open("in.txt");
    ofile.open("out.txt");
    ifile>>test;
    for(i=1;i<=test;i++)
    {
        state=0;
        noleft=0;
        for(j=0;j<4;j++)
            row[j]=col[j]=0;
        for(j=0;j<4;j++)
            for(k=0;k<4;k++)
               matx[j][k]=mato[j][k]=0;
        for(j=0;j<4;j++)
            for(k=0;k<4;k++)
            {
                ifile>>ch;
                mat[j][k]=ch;
                {
                if(mat[j][k]=='X')
                    matx[j][k]=1;
                if(mat[j][k]=='O')
                    mato[j][k]=1;
                if(mat[j][k]=='T')
                    mato[j][k]=matx[j][k]=1;
                if(mat[j][k]=='.')
                    noleft++;
                }
            }
        flag=0;
        for(j=0;j<4;j++)
            for(k=0;k<4;k++)
             {
                if(matx[j][k]==1)
                 {
                     row[j]+=1;
                     col[k]+=1;
                 }

             }
        for(j=0;j<4;j++)
            if(row[j]==4 || col[j]==4)
                flag=1;
        if(matx[0][0]==1&&matx[1][1]==1&&matx[2][2]==1&&matx[3][3]==1)
            flag=1;
        if(matx[3][0]==1&&matx[2][1]==1&&matx[1][2]==1&&matx[0][3]==1)
            flag=1;
        if(flag==1)
            state=1;
        else
        {
           flag=0;
           for(j=0;j<4;j++)
             row[j]=col[j]=0;
           for(j=0;j<4;j++)
              for(k=0;k<4;k++)
              {
                if(mato[j][k]==1)
                 {
                     row[j]+=1;
                     col[k]+=1;
                 }

               }
           for(j=0;j<4;j++)
             if(row[j]==4 || col[j]==4)
                 flag=1;
           if(mato[0][0]==1&&mato[1][1]==1&&mato[2][2]==1&&mato[3][3]==1)
              flag=1;
           if(mato[3][0]==1&&mato[2][1]==1&&mato[1][2]==1&&mato[0][3]==1)
             flag=1;
           if(flag==1)
             state=2;
            else
                if(noleft==0)
                   state=3;
                 else
                    state=4;
        }
      /*  for(j=0;j<4;j++)
            {
            for(k=0;k<4;k++)
                cout<<matx[j][k]<<" ";
            cout<<endl;
            }

        for(j=0;j<4;j++)
           cout<<col[j]<<endl;
        for(j=0;j<4;j++)
           cout<<row[j]<<endl;*/

        ofile<<"Case #"<<i<<": ";
        if(state==1)
            ofile<<"X won";
        else if(state==2)
               ofile<<"O won";
        else if(state==3)
               ofile<<"Draw";
        else if(state==4)
               ofile<<"Game has not completed";
        ofile<<endl;
    }

    ofile.close();
    ifile.close();
    return 0;
}
