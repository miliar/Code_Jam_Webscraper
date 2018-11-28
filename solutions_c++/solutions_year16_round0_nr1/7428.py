#include<cstdio>
#include<iostream>
#include<cstdlib>
#include<cstring>
#include<algorithm>
using namespace std;

int a[10];

int check(long long u)
{
    int ret=0;
    while (u)
    {
        int v=u%10;
        if (!a[v])
        {
            ret++;
            a[v]=1;
        }
        u/=10;
    }
    return ret;
}

int main()
{
    freopen("1.in","r",stdin);
    freopen("1.out","w",stdout);
    int T;
    scanf("%d",&T);
    for (int tt=1;tt<=T;tt++)
    {
        int n;
        scanf("%d",&n);
        if (n==0)
        {
            printf("Case #%d: INSOMNIA\n",tt);
            continue;
        }
        int ans=0;
        long long q=0;
        memset(a,0,sizeof(a));
        int cnt=0;
        while (cnt<10)
        {
            q+=n;
            cnt+=check(q);
            //printf("%I64d %d\n",q,cnt);
        }
        printf("Case #%d: %I64d\n",tt,q);
    }
    return 0;
}
