// RandomUsername (Nikola Jovanovic)
// GCJ 2016 Q
// A

#include <bits/stdc++.h>
#define DBG false
#define debug(x) if(DBG) printf("(ln %d) %s = %d\n", __LINE__, #x, x);
#define lld long long
#define ff(i,a,b) for(long long i=a; i<=b; i++)
#define fb(i,a,b) for(int i=a; i>=b; i--)
#define par pair<int, int>
#define fi first
#define se second
#define mid (l+r)/2
#define INF 2000000000
#define MAXT 105
#define MAXLEN 10000005
#define EPS 1e-6
#define MAXN 85

using namespace std;

bool is[20];
lld t, n;
lld pts;
lld orig;

void process(lld n)
{
    if(n == 0) return;
    if(!is[n%10])
    {
        is[n%10] = true;
        pts++;
    }
    process(n/10);
}

int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("a.out", "w", stdout);
    scanf("%lld", &t);
    ff(tt, 1, t)
    {
        scanf("%lld", &n);
        if(n == 0)
        {
            printf("Case #%lld: INSOMNIA\n", tt);
            continue;
        }
        orig = n;

        ff(i, 0, 9)
            is[i] = false;
        pts = 0;
        while(true)
        {
            process(n);
            if(pts == 10) break;
            n += orig;
        }
        printf("Case #%lld: %lld\n", tt, n);
    }
    return 0;
}
