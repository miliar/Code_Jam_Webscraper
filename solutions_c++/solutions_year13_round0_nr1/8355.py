#include<iostream>
#include<cstdio>
#include<cstring>
using namespace std;
char map[5][5];
int main()
{

    //freopen("A-small-attempt2.in","r",stdin);
    //freopen("A-small-attempt2.out","w",stdout);
    int t,ncase=0;
    cin>>t; getchar();
    while(t--)
    {
        int wflag=0;
        for(int i=0;i<4;i++)
        {
            for(int j=0;j<4;j++)
            {
                scanf("%c",&map[i][j]);
                if(!wflag)
                if(map[i][j]=='.') wflag=1;
            }
            getchar();
        }    //cout<<wflag<<endl;
        getchar();
        bool flag=0;
        char c;
        {
            for(int i=0;i<4;i++)
            {
                c=map[i][0];
                if(c!='.'){
                if((map[i][1]==c || map[i][1]=='T') && (map[i][2]==c || map[i][2]=='T') && (map[i][3]==c || map[i][3]=='T'))
                    {flag=1;goto loop;}
                }
            }
            for(int i=0;i<4;i++)
            {
                c=map[0][i];
                if(c!='.'){
                if((map[1][i]==c || map[1][i]=='T') && (map[2][i]==c || map[2][i]=='T') && (map[3][i]==c || map[3][i]=='T'))
                    {flag=1;goto loop;}
                }
            }
            for(int i=1;;)
            {
                c=map[0][0];
                if(c!='.'){
                if((map[i][i]==c || map[i][i]=='T') && (map[i+1][i+1]==c || map[i+1][i+1]=='T') && (map[i+2][i+2]==c || map[i+2][i+2]=='T'))
                    {flag=1;goto loop;}
                else break;
                }
                else break;
            }
            for(int i=1,j=2;;i++,j--)
            {
                c=map[0][3];
                if(c!='.'){
                if((map[i][j]==c || map[i][j]=='T') && (map[i+1][j-1]==c || map[i+1][j-1]=='T') && (map[i+2][j-2]==c || map[i+2][j-2]=='T'))
                    {flag=1;goto loop;}
                else break;
                }//cout<<"      sdlfjls"<<endl;
                else break;
            }

        }
        if(flag) loop:printf("Case #%d: %c won\n",++ncase,c);
        else
        {
            if(wflag) printf("Case #%d: Game has not completed\n",++ncase);
            else printf("Case #%d: Draw\n",++ncase);
        }
    }
    return 0;
}
