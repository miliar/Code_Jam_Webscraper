#include <iostream>
#include <fstream>
using namespace std;
ifstream in ("input");
ofstream out ("output");
int main ()
{   int i,j,k,t,s,sx,so,p,T;
    char b[4][4];
    int x[4][4],o[4][4];
    in>>t;
    for(k=1;k<=t;k++)
    {
        s=p=T=0;
        for(i=0;i<4;i++)
            for(j=0;j<4;j++)
                o[i][j]=x[i][j]=0;
        for(i=0;i<4;i++)
            for(j=0;j<4;j++)
                {
                    in>>b[i][j];
                    if(b[i][j]=='X') x[i][j]=1;
                        else    if(b[i][j]=='O') o[i][j]=1;
                                    else if(b[i][j]=='T') T=1;
                    if(b[i][j]=='.') p=1;
                }
                s=0;
                for(i=0;i<4;i++)
                    {
                        sx=so=0;
                        for(j=0;j<4;j++)    {sx+=x[i][j];so+=o[i][j];}
                        if(sx==4) {out<<"Case #"<<k<<": X won";s=1;}
                            else if(sx==3&&T==1&&b[i][j-1]=='T')  {out<<"Case #"<<k<<": X won";s=1;}
                        if(so==4) {out<<"Case #"<<k<<": O won";s=1;}
                            else if(so==3&&T==1&&b[i][j-1]=='T')  {out<<"Case #"<<k<<": O won";s=1;}
                    }
                if(s!=1)
                    for(i=0;i<4;i++)
                        {
                            sx=so=0;
                            for(j=0;j<4;j++)    {sx+=x[j][i];so+=o[j][i];}
                            if(sx==4) {out<<"Case #"<<k<<": X won";s=1;}
                            else if(sx==3&&T==1&&b[j-1][i]=='T')  {out<<"Case #"<<k<<": X won";s=1;}
                        if(so==4) {out<<"Case #"<<k<<": O won";s=1;}
                            else if(so==3&&T==1&&b[j-i][i]=='T')  {out<<"Case #"<<k<<": O won";s=1;}
                        }
                if(s!=1)
                       {
                        sx=x[0][0]+x[1][1]+x[2][2]+x[3][3];
                        so=o[0][0]+o[1][1]+o[2][2]+o[3][3];
                        if(sx==4) {out<<"Case #"<<k<<": X won";s=1;}
                            else if(sx==3&&T==1&&b[3][3]=='T')  {out<<"Case #"<<k<<": X won";s=1;}
                        if(so==4) {out<<"Case #"<<k<<": O won";s=1;}
                            else if(so==3&&T==1&&b[3][3]=='T')  {out<<"Case #"<<k<<": O won";s=1;}
                       }
                if(s!=1)
                        {
                        sx=x[3][0]+x[2][1]+x[1][2]+x[0][3];
                        so=o[3][0]+o[2][1]+o[1][2]+o[0][3];
                        if(sx==4) {out<<"Case #"<<k<<": X won";s=1;}
                            else if(sx==3&&T==1&&b[0][3]=='T')  {out<<"Case #"<<k<<": X won";s=1;}
                        if(so==4) {out<<"Case #"<<k<<": O won";s=1;}
                            else if(so==3&&T==1&&b[0][3]=='T')  {out<<"Case #"<<k<<": O won";s=1;}
                        }

                if(s==0&&p==0)   out<<"Case #"<<k<<": Draw";
                if(s==0&&p!=0)   out<<"Case #"<<k<<": Game has not completed";
        if(k!=t) out<<endl;
    }
    return 0;
}

