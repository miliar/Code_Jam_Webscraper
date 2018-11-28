#include<bits/stdc++.h>
using namespace std;
#define mem(x,y) memset(x,y,sizeof(x));
int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("Aoutputlarge.out", "w", stdout);
    long long int t, n, i, j, k, cnt, num, ans, d;
    scanf("%lld",&t);
    for(i=1; i<=t; i++)
    {
        long long int a[15];
        int rem;
        cnt=0;
        num=1;
        scanf("%lld",&n);
        printf("Case #%lld: ",i);
        if(n==0)
        {
            printf("INSOMNIA\n");
        }
        else
        {
            mem(a,0);
            while(cnt<10)
            {
                d=num*n;
                ans=d;
                while(d!=0)
                {
                    rem=d%10;
                    d=d/10;
                    if(a[rem]==0)
                    {
                        a[rem]=1;
                        cnt++;
                    }
                }
                num++;
            }
            printf("%lld\n",ans);
        }
    }
    return 0;
}
