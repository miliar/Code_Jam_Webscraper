#include <bits/stdc++.h>

#define ll long long

using namespace std;

int t;
ll n;

int main()
{
    freopen("A-large.out", "w", stdout);
    scanf("%d", &t);
    for(int i=1; i<=t; i++)
    {
        scanf("%lld", &n);
        if(n==0)
        {
            printf("Case #%d: INSOMNIA\n", i);
            continue;
        }
        int state = 0;
        ll sum2 = n;
        int ans = 0;
        while(state!=1023)
        {
            ll sum = sum2;
            ans = sum;
            while(sum>0)
            {
                int digi = sum % 10;
                if(state>>digi & 1)
                {
                    sum/=10;
                    continue;
                }
                else
                {
                    state += (1<<digi);
                    sum /=10;
                }
            }
            sum2 += n;
        }
        printf("Case #%d: %d\n", i,ans);
    }
    return 0;
}
