#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

int n , t , mask;

int main()
{
    freopen("input.in","r",stdin);
    freopen("output.txt","w",stdout);

    scanf("%d",&t);
    for (int cs = 1; cs <= t; ++cs) {
        scanf("%d",&n);
        if (n == 0) {
            printf("Case #%d: INSOMNIA\n",cs);
            continue;
        }
        mask = 0;
        ll ans;
        for (int i = 1; mask ^ 1023; ++i) {
            ans = n * (i * 1LL);
            while (ans != 0) {
                mask |= (1 << (ans % 10));
                ans /= 10;
            }
            ans = n * (i * 1LL);
        }
        printf("Case #%d: %lld\n",cs,ans);
    }

    return 0;
}
