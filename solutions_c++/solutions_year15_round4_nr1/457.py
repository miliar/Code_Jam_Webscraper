#include <bits/stdc++.h>

using namespace std;
char s[110][110];
bool mark[110][110];
int r,c;
bool smetadole(int x,int y)
{
    x++;
    while(x<r)
    {
        if(s[x][y]!='.')return false;
        x++;
    }
    return true;
}
bool smetagore(int x,int y)
{
    x--;
    while(x>=0)
    {
        if(s[x][y]!='.')return false;
        x--;
    }
    return true;
}
bool smetalevo(int x,int y)
{
    y--;
    while(y>=0)
    {
        if(s[x][y]!='.')return false;
        y--;
    }
    return true;
}
bool smetadesno(int x,int y)
{
    y++;
    while(y<c)
    {
        if(s[x][y]!='.')return false;
        y++;
    }
    return true;
}
int ans=0;
bool postavi(int x,int y)
{
    bool smeta=false;
    if(s[x][y]=='<')smeta|=smetalevo(x,y);
    if(s[x][y]=='>')smeta|=smetadesno(x,y);
    if(s[x][y]=='^')smeta|=smetagore(x,y);
    if(s[x][y]=='v')smeta|=smetadole(x,y);
    if(smeta)ans++;
    else return true;
    if(!smetalevo(x,y)||!smetadesno(x,y)||!smetagore(x,y)||!smetadole(x,y))return true;
    return false;
}
int main()
{
    int t;
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    int idx=1;
    scanf("%d",&t);
    while(t--)
    {
        ans=0;
        scanf("%d%d",&r,&c);
        for(int i=0;i<r;i++)
            scanf("%s",s[i]);
            bool printed=false;
        for(int i=0;i<r;i++)
        {
            for(int j=0;j<c;j++)
            {
                if(printed)continue;
               if(!postavi(i,j))
                {
                 printf("Case #%d: IMPOSSIBLE\n",idx++);
                 printed=true;
                 break;
                }
            }
        }
        if(!printed)printf("Case #%d: %d\n",idx++,ans);
    }
    return 0;
}
