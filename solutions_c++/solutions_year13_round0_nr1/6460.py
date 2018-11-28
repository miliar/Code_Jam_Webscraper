#include <iostream>
#include <cstdio>
#include <fstream>
#include <string>
using namespace std;

int result(int j, int s);
ofstream fout ("A-large.out");
ifstream fin ("A-large.in");
int main()
{
    char tic[4][4];
    int T,s;

    fin >> T;
    for(int j=1; j<=T; j++)
    {
        s=0;
        for(int k=0; k<=3;k++)
        {
            for(int l=0; l<=3; l++)
            {
                fin >> tic[k][l];
            }
        }
                if( (tic[0][0]=='X'|| tic[0][0]=='T')&& (tic[0][1]=='X'|| tic[0][1]=='T') && (tic[0][2]=='X'|| tic[0][2]=='T') && (tic[0][3]=='X'|| tic[0][3]=='T') )
                    s=1;
                else if( (tic[1][0]=='X'|| tic[1][0]=='T')&& (tic[1][1]=='X'|| tic[1][1]=='T') && (tic[1][2]=='X'|| tic[1][2]=='T') && (tic[1][3]=='X'|| tic[1][3]=='T') )
                    s=1;
                else if( (tic[2][0]=='X'|| tic[2][0]=='T')&& (tic[2][1]=='X'|| tic[2][1]=='T') && (tic[2][2]=='X'|| tic[2][2]=='T') && (tic[2][3]=='X'|| tic[2][3]=='T') )
                    s=1;
                else if( (tic[3][0]=='X'|| tic[3][0]=='T')&& (tic[3][1]=='X'|| tic[3][1]=='T') && (tic[3][2]=='X'|| tic[3][2]=='T') && (tic[3][3]=='X'|| tic[3][3]=='T') )
                    s=1;
                else if( (tic[0][0]=='X'|| tic[0][0]=='T')&& (tic[1][0]=='X'|| tic[1][0]=='T') && (tic[2][0]=='X'|| tic[2][0]=='T') && (tic[3][0]=='X'|| tic[3][0]=='T') )
                    s=1;
                else if( (tic[0][1]=='X'|| tic[0][1]=='T')&& (tic[1][1]=='X'|| tic[1][1]=='T') && (tic[2][1]=='X'|| tic[2][1]=='T') && (tic[3][1]=='X'|| tic[3][1]=='T') )
                    s=1;
                else if( (tic[0][2]=='X'|| tic[0][2]=='T')&& (tic[1][2]=='X'|| tic[1][2]=='T') && (tic[2][2]=='X'|| tic[2][2]=='T') && (tic[3][2]=='X'|| tic[3][2]=='T') )
                    s=1;
                else if( (tic[0][3]=='X'|| tic[0][3]=='T')&& (tic[1][3]=='X'|| tic[1][3]=='T') && (tic[2][3]=='X'|| tic[2][3]=='T') && (tic[3][3]=='X'|| tic[3][3]=='T') )
                    s=1;
                else if( (tic[0][0]=='X'|| tic[0][0]=='T')&& (tic[1][1]=='X'|| tic[1][1]=='T') && (tic[2][2]=='X'|| tic[2][2]=='T') && (tic[3][3]=='X'|| tic[3][3]=='T') )
                    s=1;
                else if( (tic[0][3]=='X'|| tic[0][3]=='T')&& (tic[1][2]=='X'|| tic[1][2]=='T') && (tic[2][1]=='X'|| tic[2][1]=='T') && (tic[3][0]=='X'|| tic[3][0]=='T') )
                    s=1;
                else if( (tic[0][0]=='O'|| tic[0][0]=='T')&& (tic[0][1]=='O'|| tic[0][1]=='T') && (tic[0][2]=='O'|| tic[0][2]=='T') && (tic[0][3]=='O'|| tic[0][3]=='T') )
                    s=2;
                else if( (tic[1][0]=='O'|| tic[1][0]=='T')&& (tic[1][1]=='O'|| tic[1][1]=='T') && (tic[1][2]=='O'|| tic[1][2]=='T') && (tic[1][3]=='O'|| tic[1][3]=='T') )
                    s=2;
                else if( (tic[2][0]=='O'|| tic[2][0]=='T')&& (tic[2][1]=='O'|| tic[2][1]=='T') && (tic[2][2]=='O'|| tic[2][2]=='T') && (tic[2][3]=='O'|| tic[2][3]=='T') )
                    s=2;
                else if( (tic[3][0]=='O'|| tic[3][0]=='T')&& (tic[3][1]=='O'|| tic[3][1]=='T') && (tic[3][2]=='O'|| tic[3][2]=='T') && (tic[3][3]=='O'|| tic[3][3]=='T') )
                    s=2;
                else if( (tic[0][0]=='O'|| tic[0][0]=='T')&& (tic[1][0]=='O'|| tic[1][0]=='T') && (tic[2][0]=='O'|| tic[2][0]=='T') && (tic[3][0]=='O'|| tic[3][0]=='T') )
                    s=2;
                else if( (tic[0][1]=='O'|| tic[0][1]=='T')&& (tic[1][1]=='O'|| tic[1][1]=='T') && (tic[2][1]=='O'|| tic[2][1]=='T') && (tic[3][1]=='O'|| tic[3][1]=='T') )
                    s=2;
                else if( (tic[0][2]=='O'|| tic[0][2]=='T')&& (tic[1][2]=='O'|| tic[1][2]=='T') && (tic[2][2]=='O'|| tic[2][2]=='T') && (tic[3][2]=='O'|| tic[3][2]=='T') )
                    s=2;
                else if( (tic[0][3]=='O'|| tic[0][3]=='T')&& (tic[1][3]=='O'|| tic[1][3]=='T') && (tic[2][3]=='O'|| tic[2][3]=='T') && (tic[3][3]=='O'|| tic[3][3]=='T') )
                    s=2;
                else if( (tic[0][0]=='O'|| tic[0][0]=='T')&& (tic[1][1]=='O'|| tic[1][1]=='T') && (tic[2][2]=='O'|| tic[2][2]=='T') && (tic[3][3]=='O'|| tic[3][3]=='T') )
                    s=2;
                else if( (tic[0][3]=='O'|| tic[0][3]=='T')&& (tic[1][2]=='O'|| tic[1][2]=='T') && (tic[2][1]=='O'|| tic[2][1]=='T') && (tic[3][0]=='O'|| tic[3][0]=='T') )
                    s=2;
                else
                {
                         for(int k=0; k<=3;k++)
                            {
                                for(int l=0; l<=3; l++)
                                {
                                    if(tic[k][l]=='.')
                                    {
                                        s=4;
                                            break;
                                    }
                                }
                            }
                            if(s!=4)
                                s = 3;
                }
                result(j, s);
    }
    return 0;
}
int result(int j,int s)
{
    if(s==1)
        fout <<"Case #"<<j<<": X won"<<endl;
    else if(s==2)
        fout <<"Case #"<<j<<": O won"<<endl;
    else if(s==3)
        fout <<"Case #"<<j<<": Draw"<<endl;
    else if(s==4)
        fout <<"Case #"<<j<<": Game has not completed"<<endl;
    return 0;
}
