#include<bits/stdc++.h>
using namespace std;

int n,ok;

int usep[10],usem[10];

int dfs(int st,int d)
{
    if(d==n)return 1;
    int fg;
    for(int i=0;i<n;i++)
    {
        if(!usep[i])
        {
            usep[i]=1;
            fg=0;
            for(int j=0;j<n;j++)
            {
                if(!usem[j]&&(st&(1<<(i*n+j)))!=0)
                {
                    fg=1;
                    usem[j]=1;
                    if(!dfs(st,d+1))return 0;
                    usem[j]=0;
                }
            }
            if(fg==0)return 0;
            usep[i]=0;
        }
    }
    return 1;
}

int solver(int st)
{
    int ret=0;
    for(int i=0;i<n*n;i++)
    {
        if(((1<<i)&st)==0&&((1<<i)&ok)!=0)
            return 1000;
        if(((1<<i)&st)!=0&&((1<<i)&ok)==0)
            ret++;
    }
    memset(usep,0,sizeof(usep));
    memset(usem,0,sizeof(usem));

    int t=dfs(st,0);
    //printf("%d %d\n",st,t);
    if(!t)return 1000;
    return ret;
}
char str[10];

int main()
{
    freopen("D-m.in","r",stdin);
    freopen("D-m.out","w",stdout);
    int T;
    scanf("%d",&T);
    for(int tcnt=1;tcnt<=T;tcnt++)
    {
        scanf("%d",&n);
        int x;
        ok=0;
        for(int i=0;i<n;i++)
        {
            scanf("%s",str);
            for(int j=0;j<n;j++)
                ok=ok*2+(str[j]-'0');
        }
        //printf("%d!!\n",ok);
        int ans=1000;
        for(int i=0;i<(1<<(n*n));i++)
            ans=min(ans,solver(i));
        printf("Case #%d: %d\n",tcnt,ans);
    }
    return 0;
}
