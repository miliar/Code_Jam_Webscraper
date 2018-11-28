/*
author:jxy
lang:C/C++
university:China,Xidian University
**If you need to reprint,please indicate the source**
*/
#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <queue>
#define INF 1E9
using namespace std;
char map[4][4];
char win;
bool judge(int i,bool f)//1:col 0:row
{
    char t,fir=f?map[0][i]:map[i][0];
    int num=0;// cout<<fir<<" "<<i<<" "<<f<<endl;
    if(fir=='T')num++;
    if(fir=='.')return 0;
    for(int j=1;j<4;j++)
    {
        t=f?map[j][i]:map[i][j];
       // cout<<t<<" ";
        if(fir=='T')fir=t;
        if(t!=fir&&t!='T')return 0;
        if(t=='T')num++;
    }
   // cout<<endl;
    if(fir=='.')return 0;
    if(num>1)return 0;
    win=fir;
    return 1;
}
int main()
{  // freopen("1.txt","w",stdout);
    int T,i,j,C=0;
    scanf("%d",&T);
    int flag=-1;

    while(T--)
    {while(getchar()!='\n');
        flag=-1;
        win=0;
        for(i=0;i<4;i++,getchar())
          for(j=0;j<4;j++)
          {
              map[i][j]=getchar();
              if(map[i][j]=='.')flag=0;
             // cout<<map[i][j]<<endl;
          }
       // cout<<flag<<endl;
        for(i=0;i<4;i++)
        {
            if(judge(i,0)||judge(i,1))
            {
                flag=1;
                break;
            }
            //cout<<"-----------"<<i<<endl;
        }
       // cout<<flag<<endl;
        if(flag<1)
        {
            int num=0;
            char t,fir=map[0][0];
            if(fir=='T')num++;
            if(fir!='.')
            for(i=1;i<4;i++)
            {
                t=map[i][i];
                if(fir=='T')fir=t;
                if(t!=fir&&t!='T')break;
                if(t=='T')num++;
            }
            if(fir!='.'&&num<=1&&i==4) win=fir,flag=1;
            if(!win)
            {
                num=0;
                fir=map[0][3];
                if(fir=='T')num++;
                if(fir!='.')
                for(i=1;i<4;i++)
                {
                    t=map[i][3-i];
                    if(fir=='T')fir=t;
                    if(t!=fir&&t!='T')break;
                    if(t=='T')num++;
                }
                if(fir!='.'&&num<=1&&i==4) win=fir,flag=1;
               // cout<<fir<<" "<<win<<" "<<num<<endl;
            }
        }
        printf("Case #%d: ",++C);
        if(flag<0)printf("Draw");
        else if(flag)printf("%c won",win);
        else printf("Game has not completed");
        puts("");
    }
}
