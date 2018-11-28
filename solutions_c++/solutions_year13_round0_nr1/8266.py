#include<iostream>
#include<stdio.h>
#define intin(a) scanf("%d",&a)
using namespace std;
int main()
{
    freopen("A-small-attempt1.in","r",stdin);
    freopen("Aoutput.txt","w",stdout);
    int i,j,cases,x=0,dot;
    char s[5][5],ch;
    intin(cases);
    while(++x<=cases)
    {
        for(i=0;i<4;i++)
            scanf("%s",s[i]);

        dot=0;
        //row check
        for(i=0;i<4;i++)
        {   ch=s[i][0];
            for(j=0;j<4;j++)
            {   if(s[i][j]=='.')dot=1;
                if(s[i][j]!='T' && ch!=s[i][j])
                    break;
            }
            if(ch!='.'&&j==4)goto lab1;
        }
        //col check
        for(j=0;j<4;j++)
        {   ch=s[0][j];if(ch=='.')continue;
            for(i=1;i<4;i++)
            {   if(s[i][j]!='T' && ch!=s[i][j])
                    break;
            }
            if(ch!='.'&&i==4)goto lab1;
        }
        //diagonal check
        ch=s[0][0];
        for(i=0;i<4;i++)
            if(s[i][i]!='T' && ch!=s[i][i]) break;
        if(ch!='.'&&i==4)goto lab1;
        ch=s[0][3];
        for(i=1;i<4;i++)
            if(s[i][3-i]!='T' && ch!=s[i][3-i]) break;
        if(ch!='.'&&i==4)goto lab1;

        if(dot==1)printf("Case #%d: Game has not completed\n",x);
        else printf("Case #%d: Draw\n",x);
        continue;
        lab1:printf("Case #%d: %c won\n",x,ch);;
    }
}
