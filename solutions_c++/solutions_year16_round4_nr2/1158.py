#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <string>
#include <cstring>
#include <cmath>
#include <algorithm>
using namespace std;
const int maxn=20;
const int maxm=100100;

int n,K,tot,s[maxm],vis[maxn];
double ans,P[maxn],A[maxn];

int count(int x)
{
    int cnt=0;
    for(;x;x>>=1) if(x&1) cnt++;
    return cnt;
}

void init()
{
     scanf("%d %d",&n,&K);
     for(int i=1;i<=n;i++) scanf("%lf",&P[i]);
     int FULL=(1<<K)-1; tot=0;
     for(int i=1;i<=FULL;i++)
         if(count(i)==K/2) s[++tot]=i;
};

double calc()
{
       int cnt=0; double Tas=0;
       for(int i=1;i<=n;i++)
           if(vis[i]) A[++cnt]=P[i];
       for(int i=1;i<=tot;i++)
       {
           int j=1; double sum=1;
           for(int x=s[i];x;x>>=1,j++)
               if(x&1) sum*=A[j]; else sum*=(1-A[j]);
           for(;j<=K;j++) sum*=(1-A[j]);
           Tas+=sum;
       }
       return Tas;
}

void dfs(int p,int k)
{
     if(k>K)
     {
        ans=max(ans,calc());
        return;
     }
     for(int i=p;i<=n;i++)
     {
         vis[i]=1;
         dfs(i+1,k+1);
         vis[i]=0;
     }
}

void work()
{
     ans=0;
     memset(vis,0,sizeof(vis));
     dfs(1,1);
     printf("%lf\n",ans);
}

int main()
{
    //freopen("B.in","r",stdin);
    //freopen("B.out","w",stdout);
    int TT=0;
    scanf("%d",&TT);
    for(int i=1;i<=TT;i++)
    {
        printf("Case #%d: ",i);
        init();
        work();
    }
    return 0;
}
