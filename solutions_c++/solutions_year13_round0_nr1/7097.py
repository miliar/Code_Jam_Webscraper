#include<iostream>
#include<conio.h>
#include<stdio.h>
using namespace std;
char winner='0';
int check(char [4],int);
int main()
{
    int ca,cas=1,i,j,dot,flag=0;
    char ttt[4][4];
    char pass[4];
    freopen( "A-large.in", "r", stdin );
	freopen( "output.txt", "w", stdout );
    cin>>ca;
    //cout<<ca;
    string str;

    while(cas<=ca)
    {
    flag=0;
    dot=0;
    for(i=0; i<4;i++)
    {
             for(j=0; j<4;j++)
             {
                      cin>>ttt[i][j];
                      //cout<<ttt[i][j];
                      if (ttt[i][j]=='.') dot=1;
             }
             if(flag!=1)flag=check(ttt[i], cas);

    }
    //to check rowwise
    /*for(i=0;i<4;i++)
    {
                    flag=check(ttt[i],cas);
                   if (flag==1) break;
    }*/
    //to check columnwise
    if(flag!=1)
    {
    for(i=0;i<4;i++)
    {
                    for(j=0; j<4; j++)
                    pass[j]=ttt[j][i];
                    //cout<<pass;
                    flag=check(pass,cas);
                    if (flag==1) break;
    }
    }
    if(flag!=1)
    {
     char pass[]={ttt[0][0], ttt[1][1], ttt[2][2], ttt[3][3]};
     flag=check(pass,cas);
    }
    if(flag!=1)
    {
    char pass[]={ttt[0][3], ttt[1][2], ttt[2][1], ttt[3][0]};
     flag=check(pass,cas);
    }
if(flag==1)
{
    cout<<"Case #"<<cas<<": "<<winner<<" won"<<endl;
}
    if(flag==0)
    {if(dot==0)
    cout<<"Case #"<<cas<<": Draw"<<endl;
    else
    cout<<"Case #"<<cas<<": Game has not completed"<<endl;
    }

    cas++;
}

    return 0;
}
int check(char ttt[4], int ca)
{
    //cout<<"entered"<<endl;
    //cout<<ttt[0]<<ttt[1]<<ttt[2]<<ttt[3]<<endl;
    int flag=0;
    if(ttt[0]!='.')
                    {
                    if(ttt[0]=='T'&& ttt[1]!='.')
                    {
                            if((ttt[1]==ttt[2])&&(ttt[2]==ttt[3]))
                            {
                                  //cout<<"Case #"<<ca<<": "<<ttt[2]<<"won"<<endl;
                                  winner=ttt[2];
                                  flag=1;
                            }
                    }
                    else if(ttt[0]==ttt[1]||ttt[1]=='T')
                    {
                         if(ttt[1]==ttt[2]||(ttt[1]=='T'&&ttt[2]==ttt[0])||ttt[2]=='T')
                         {
                                   if(ttt[2]==ttt[3]||(ttt[2]=='T'&&ttt[3]==ttt[0])||ttt[3]=='T')
                                   {//cout<<"Case #"<<ca<<": "<<ttt[1]<<" won"<<endl;
                                       winner=ttt[0];
                                   flag=1;}
                         }
                    }

                    }
                    return flag;
}
