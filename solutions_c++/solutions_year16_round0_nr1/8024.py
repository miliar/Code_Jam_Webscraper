#include <bits/stdc++.h>

using namespace std;

#define xx first
#define yy second
#define pb push_back

int tc;
long long n;

int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("AAA.out", "w", stdout);
    cin >> tc;
    int tt = 0;
    while(tc--)
    {
        int cnt = (1 << 10) - 1;
        scanf("%lld", &n);
        if(n == 0)
        {
            printf("Case #%d: INSOMNIA\n", ++tt);
            continue;
        }
        long long ans;
        long long i = 1;
        while(cnt > 0)
        {
            ans = n * i;
            long long t = ans;
            while(t > 0)
            {
                int x = (int) (t % 10LL);
                t /= 10LL;
                cnt = (cnt & (~(1 << x)));
            }
            i++;
        }
        printf("Case #%d: %lld\n", ++tt, ans);
    }
    return 0;
}
