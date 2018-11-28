#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<cmath>
#include<algorithm>
#include<cstring>
#include<vector>
#include<queue>
using namespace std;
int a[20];
int main()
{
#ifndef ONLINE_JUDGE
    freopen("A-large.in", "r", stdin);
    freopen("A-out.out", "w", stdout);
#endif
    int T,k;
    scanf("%d",&T);
    k=0;
    long long n;
    while(T--)
    {
        memset(a,0,sizeof(a));
        scanf("%lld",&n);
        long long m=n;
        k++;
        printf("Case #%d: ",k);
        //int cnt=1;
        for(long long i=1;i<200;i++)
        {
            long long t=n*i;
            m=t;
            //printf("ss%d\n",m);
            int flag=0;
            while(t)
            {
                a[t%10]=1;
                t/=10;
            }
            for(long long j=0;j<=9;j++)
            {
                if(a[j]==0) flag=1;
            }
            if(flag==0) break;
        }
        if(n==0) puts("INSOMNIA");
        else printf("%lld\n",m);
    }
    return 0;
}
