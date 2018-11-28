#include <bits/stdc++.h>
using namespace std;
#define FOR(i, s, t) for(int i = s, _t = t; i < _t; i++)

const int maxn = 1000 + 5;
int n;
int p[maxn];

int main()
{
    freopen ("B-large.in","r",stdin);
    freopen ("B-large.out","w",stdout);
    int kase;
    scanf("%d", &kase);
    FOR(T, 1, kase + 1)
    {
        scanf("%d", &n);
        int ans = 0;
        FOR(i, 0, n){ scanf("%d", p+i); ans = max(ans, p[i]);}

        int c = 2;
        while(c < ans)
        {
            int sum = c;
            FOR(i, 0, n) sum += (p[i]-1)/c;
            ans = min(ans, sum);
            c++;
        }
        printf("Case #%d: %d\n", T, ans);
    }
    return 0;
}
