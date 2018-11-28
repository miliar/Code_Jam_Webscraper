#include<iostream>
#include<fstream>
using namespace std;
int main()
{
    ifstream fin;
    ofstream fout;
    string useless;
    fin.open("A-small-attempt2.in");
    fout.open("output");
    int a;
    fin>>a;
    for(int k=1;k<=a;k++)
    {
                     bool incomplete=false;
                     char tic[4][4];
                     for(int i=0;i<4;i++)
                     for(int j=0;j<4;j++)
                     {
                             fin>>tic[i][j];
                     }
                     for(int i=0;i<4;i++)
                     for(int j=0;j<4;j++)
                     {
                             if(tic[i][j]=='.')
                             {
                             incomplete=true;
                             }            
                     }

                     int xcount=0;
                     int ocount=0;
                     bool xwon=false;
                     bool owon=false;
                     for(int i=0;i<4;i++)
                     {
                             if((tic[0][i]=='X' || tic[0][i]=='T'))
                             {
                                                xcount++;
                             }
                     }
                     if(xcount==4)
                     {
                                  xwon=true;
                     }
    else
    {
        xcount=0;
    }
    for(int i=0;i<4;i++)
    {
            if((tic[1][i]=='X' || tic[1][i]=='T'))
            {
                               xcount++;
            }
    }
    if(xcount==4)
    {
                 xwon=true;
    }
    else
    {
        xcount=0;
    }

    for(int i=0;i<4;i++)
    {
            if((tic[2][i]=='X' || tic[2][i]=='T'))
            {
                               xcount++;
            }
    }
    if(xcount==4)
    {
                 xwon=true;
    }
    else
    {
        xcount=0;
    }

    for(int i=0;i<4;i++)
    {
            if((tic[3][i]=='X' || tic[3][i]=='T'))
            {
                               xcount++;
            }
    }
    if(xcount==4)
    {
                 xwon=true;
    }
    else
    {
        xcount=0;
    }
    for(int i=0;i<4;i++)
    {
            if((tic[i][0]=='X' || tic[i][0]=='T'))
            {
                               xcount++;
            }
    }
    if(xcount==4)
    {
                 xwon=true;
    }
    else
    {
        xcount=0;
    }
    for(int i=0;i<4;i++)
    {
            if((tic[i][1]=='X' || tic[i][1]=='T'))
            {
                               xcount++;
            }
    }
    if(xcount==4)
    {
                 xwon=true;
    }
    else
    {
        xcount=0;
    }
    for(int i=0;i<4;i++)
    {
            if((tic[i][2]=='X' || tic[i][2]=='T'))
            {
                               xcount++;
            }
    }
    if(xcount==4)
    {
                 xwon=true;
    }
    else
    {
        xcount=0;
    }
    for(int i=0;i<4;i++)
    {
            if((tic[i][3]=='X' || tic[i][3]=='T'))
            {
                               xcount++;
            }
    }
    if(xcount==4)
    {
                 xwon=true;
    }
    else
    {
        xcount=0;
    }
    if((tic[0][0]=='X' || tic[0][0]=='T')&&(tic[1][1]=='X' || tic[1][1]=='T')&&(tic[2][2]=='X' || tic[2][2]=='T')&&(tic[3][3]=='X' || tic[3][3]=='T'))
    {
                       xwon=true;
    }
    if((tic[0][3]=='X' || tic[0][3]=='T')&&(tic[1][2]=='X' || tic[1][2]=='T')&&(tic[2][1]=='X' || tic[2][1]=='T')&&(tic[3][0]=='X' || tic[3][0]=='T'))
    {
                       xwon=true;
    }

    for(int i=0;i<4;i++)
    {
            if((tic[0][i]=='O' || tic[0][i]=='T'))
            {
                               ocount++;
            }
    }
    if(ocount==4)
    {
                 owon=true;
    }
    else
    {
        ocount=0;
    }
    for(int i=0;i<4;i++)
    {
            if((tic[1][i]=='O' || tic[1][i]=='T'))
            {
                               ocount++;
            }
    }
    if(ocount==4)
    {
                 owon=true;
    }
    else
    {
        ocount=0;
    }

    for(int i=0;i<4;i++)
    {
            if((tic[2][i]=='O' || tic[2][i]=='T'))
            {
                               ocount++;
            }
    }
    if(ocount==4)
    {
                 owon=true;
    }
    else
    {
        ocount=0;
    }

    for(int i=0;i<4;i++)
    {
            if((tic[3][i]=='O' || tic[3][i]=='T'))
            {
                               ocount++;
            }
    }
    if(ocount==4)
    {
                 owon=true;
    }
    else
    {
        ocount=0;
    }
    for(int i=0;i<4;i++)
    {
            if((tic[i][0]=='O' || tic[i][0]=='O'))
            {
                               ocount++;
            }
    }
    if(ocount==4)
    {
                 owon=true;
    }
    else
    {
        ocount=0;
    }
    for(int i=0;i<4;i++)
    {
            if((tic[i][1]=='O' || tic[i][1]=='T'))
            {
                               ocount++;
            }
    }
    if(ocount==4)
    {
                 owon=true;
    }
    else
    {
        ocount=0;
    }
    for(int i=0;i<4;i++)
    {
            if((tic[i][2]=='O' || tic[i][2]=='T'))
            {
                               ocount++;
            }
    }
    if(ocount==4)
    {
                 owon=true;
    }
    else
    {
        ocount=0;
    }
    for(int i=0;i<4;i++)
    {
            if((tic[i][3]=='O' || tic[i][3]=='T'))
            {
                               ocount++;
            }
    }
    if(ocount==4)
    {
                 owon=true;
    }
    else
    {
        ocount=0;
    }
    if((tic[0][0]=='O' || tic[0][0]=='T')&&(tic[1][1]=='O' || tic[1][1]=='T')&&(tic[2][2]=='O' || tic[2][2]=='T')&&(tic[3][3]=='O' || tic[3][3]=='T'))
    {
                       owon=true;
    }
    if((tic[0][3]=='O' || tic[0][3]=='T')&&(tic[1][2]=='O' || tic[1][2]=='T')&&(tic[2][1]=='O' || tic[2][1]=='T')&&(tic[3][0]=='O' || tic[3][0]=='T'))
    {
                       owon=true;
    }
    if(xwon)
    fout<<"Case #"<<k<<": X won"<<endl;
    else if(owon)
    fout<<"Case #"<<k<<": O won"<<endl;
    if((!xwon)&&(!owon)&&(incomplete))
    {
                                      fout<<"Case #"<<k<<": Game has not completed"<<endl;
    }
    if((!xwon)&&(!owon)&&(!incomplete))
    {
                                       fout<<"Case #"<<k<<": Draw"<<endl;
    }
    getline(fin,useless);
}
    system("pause");
    return 0;
}
