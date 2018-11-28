#include <map>
#include <set>
#include <queue>
#include <ctime>
#include <cmath>
#include <string>
#include <cstdio>
#include <vector>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <algorithm>
#define LL long long
#define N 10007
using namespace std;
int a[N],b[N],c[N],d[N],f[N],g[N];
int s2[N];
bool use[N];
int run,n,x,ans;
void add2(int x)
{
    for (int i=x;i;i-=i&(-i)) s2[i]++;
}
int getsum2(int x)
{
    int sum=0;
    for (int i=x;i<=n;i+=i&(-i)) sum+=s2[i];
    return sum;
}
void dfs(int dd)
{
    if (dd>n)
    {
        int cnt=1;
        for (int i=1;i<=n;i++)
            if (use[i]) c[cnt++]=b[i];
        cnt=n;
        for (int i=1;i<=n;i++)
            if (!use[i]) c[cnt--]=b[i];
        cnt=0;
        for (int i=1;i<=n;i++)
            for (int j=1;j<=n;j++)
                if (a[i]==c[j])
                {
                    d[i]=j;
                    break;
                }
        //for (int i=1;i<=n;i++)
            //printf("%d %d %d\n",i,c[i],d[i],a[i]);
        for (int i=0;i<=n;i++) s2[i]=0;
        for (int i=1;i<=n;i++)
        {
            cnt+=getsum2(d[i]);
            add2(d[i]);
        }

        ans=min(ans,cnt);
        return;
    }
    dfs(dd+1);
    use[dd]=true;
    dfs(dd+1);
    use[dd]=false;
}

int main()
{
    freopen("B1.in","r",stdin);
    freopen("A22.txt","w",stdout);

    scanf("%d",&run);
    for (int cas=1;cas<=run;cas++)
    {
        memset(f,0,sizeof f);
        memset(g,0,sizeof f);
        memset(s2,0,sizeof f);
        scanf("%d",&n);
        for (int i=1;i<=n;i++)
        {
            scanf("%d",a+i);
            b[i]=a[i];
        }
        sort(b+1,b+n+1);
        //for (int i=1;i<=n;i++)
            //a[i]=lower_bound(b,b+n,a[i])-b;
        ans=n*n;
        dfs(1);
        printf("Case #%d: %d\n",cas,ans);
    }
    return 0;
}

