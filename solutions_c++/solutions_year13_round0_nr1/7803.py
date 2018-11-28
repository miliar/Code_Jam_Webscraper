#include<iostream>
//#include<conio.h>
using namespace std;
int main()
{
    int t,i,j,k,x,o,tt,y=0,p=0;
    char a[4][4];
    freopen( "A-large.in", "r", stdin );
	freopen( "output.out", "w", stdout );
    cin >> t;
    for(i=0;i<t;i++)
    {
                    for(j=1;j<=4;j++)
                    {
                                     for(k=1;k<=4;k++)
                                     {
                                                      cin >> a[j][k];
                                     }
                    }
                    for(j=1;j<=4;j++){
                    o=0;x=0;tt=0;
                    for(k=1;k<=4;k++){
                                     if(a[j][k]=='X')
                                     x++;
                                     if(a[j][k]=='T')
                                     tt++;
                                     if(x==3&&tt==1||x==4)
                                     y=1;
                                     }
                                     }
                    for(j=1;j<=4;j++){
                    x=0;o=0;tt=0;
                    for(k=1;k<=4;k++){
                                     if(a[j][k]=='O')
                                     o++;
                                     if(a[j][k]=='T')
                                     tt++;
                                     if(o==3&&tt==1||o==4)
                                     y=2;
                                     }
                                     }
                    for(j=1;j<=4;j++){
                    o=0;x=0;tt=0;
                    for(k=1;k<=4;k++){
                                     if(a[k][j]=='X')
                                     x++;
                                     if(a[k][j]=='T')
                                     tt++;
                                     if(x==3&&tt==1||x==4)
                                     y=1;
                                     }
                                     }
                    for(j=1;j<=4;j++){
                    x=0;o=0;tt=0;
                    for(k=1;k<=4;k++){
                                     if(a[k][j]=='O')
                                     o++;
                                     if(a[k][j]=='T')
                                     tt++;
                                     if(o==3&&tt==1||o==4)
                                     y=2;
                                     }
                                     }
                    x=0;o=0;tt=0;
                    for(j=1;j<=4;j++){
                                     if(a[j][j]=='O')
                                     o++;
                                     if(a[j][j]=='T')
                                     tt++;
                                     if(o==3&&tt==1||o==4)
                                     y=2;
                                     }
                    x=0;o=0;tt=0;
                    for(j=1;j<=4;j++){
                                     if(a[j][j]=='X')
                                     x++;
                                     if(a[j][j]=='T')
                                     tt++;
                                     if(x==3&&tt==1||x==4)
                                     y=1;
                                     }
                    x=0;o=0;tt=0;
                    for(j=1;j<=4;j++){
                    for(k=1;k<=4;k++){
                    if(j+k==5){
                                     if(a[j][k]=='X')
                                     x++;
                                     if(a[j][k]=='T')
                                     tt++;
                                     if(x==3&&tt==1||x==4)
                                     y=1;
                                     }
                                     }
                                     }
                    x=0;o=0;tt=0;
                    for(j=1;j<=4;j++){
                    for(k=1;k<=4;k++){
                    if(j+k==5)
                                     {if(a[j][k]=='O')
                                     o++;
                                     if(a[j][k]=='T')
                                     tt++;
                                     if(o==3&&tt==1||o==4)
                                     y=2;
                                     }
                                     }
                                     }
                    x=0;o=0;tt=0;
                    for(j=1;j<=4;j++){
                    for(k=1;k<=4;k++){
                                     if(a[j][k]=='.')
                                     {p=1;}
                                     }
                                     } 
                    if(p==1 && y==0)
                                    {cout <<"Case #" <<i+1 <<": "<<"Game has not completed" <<endl;}
                    else if(y==1)
                            {cout <<"Case #" <<i+1 <<": "<<"X won" <<endl;}
                    else if(y==2)
                                 {cout <<"Case #" <<i+1 <<": "<<"O won" <<endl;}
                    else if(y!=1 && y!=2)
                        {cout <<"Case #" <<i+1 <<": "<<"Draw" <<endl;}
                    y=0;
                    p=0;
    }
    //getch();
    return 0;
}
