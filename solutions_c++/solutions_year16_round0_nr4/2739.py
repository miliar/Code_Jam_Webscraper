// RandomUsername (Nikola Jovanovic)
// GCJ 2016 Q
// D

#include <bits/stdc++.h>
#define DBG false
#define debug(x) if(DBG) printf("(ln %d) %s = %d\n", __LINE__, #x, x);
#define lld long long
#define ff(i,a,b) for(long long i=a; i<=b; i++)
#define fb(i,a,b) for(long long i=a; i>=b; i--)
#define par pair<int, int>
#define fi first
#define se second
#define mid (l+r)/2
#define INF 1000000000LL

using namespace std;

lld t, k, c, s;

int main()
{
    freopen("D-small-attempt0.in", "r", stdin);
    freopen("d.out", "w", stdout);
    scanf("%lld", &t);
    ff(tt, 1, t)
    {
        scanf("%lld %lld %lld", &k, &c, &s);

        printf("Case #%lld: ", tt);
        ff(idx, 1, k)
        {
           printf("%lld ", idx);
        }
        printf("\n");
    }
    return 0;
}
