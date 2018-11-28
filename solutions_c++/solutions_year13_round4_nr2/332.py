#include <cstdio>
using namespace std;

typedef long long ll;
ll n, p;

ll cl(ll n, ll k)
{
    if(n == 0LL)
        return 0LL;
    else if(k == (1LL << n) - 1LL)
        return (1LL << n) - 1LL;
    else
        return cl(n - 1LL, (k + 1LL) >> 1LL);
}

ll cu(ll n, ll k)
{
    if(n == 0LL)
        return 0LL;
    else if(k == 0LL)
        return 0LL;
    else
        return (1LL << (n - 1LL)) | cu(n - 1LL, (k - 1LL) >> 1LL);
}

int main()
{
    int T; scanf("%d", &T);
    for(int t = 1; t <= T; t++)
    {
        scanf("%lld %lld", &n, &p);
        printf("Case #%d:", t);

        ll lb, ub;

        lb = 0LL, ub = (1LL << n) - 1LL;
        while(lb < ub)
        {
            ll md = ub - (ub - lb) / 2LL;
            if(cu(n, md) < p)
                lb = md;
            else
                ub = md - 1LL;
        }
        printf(" %lld", lb);

        lb = 0LL, ub = (1LL << n) - 1LL;
        while(lb < ub)
        {
            ll md = ub - (ub - lb) / 2LL;
            if(cl(n, md) < p)
                lb = md;
            else
                ub = md - 1LL;
        }
        printf(" %lld\n", lb);
    }
    return 0;
}
