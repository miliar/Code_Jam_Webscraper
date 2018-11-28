#include <bits/stdc++.h>
using namespace std;
#define SD(a) scanf("%d", &a)
#define SLLD(a) scanf("%lld", &a)
#define ll long long

//If Long Long (mask & (1LL << k))
#define check(mask, k) (mask & (1 << k))
#define set1(mask, k) (mask | (1 << k))
#define set0(mask ,k) (mask & (~(1<<k)))

ll f(ll n)
{
    int mask = 0, i, rem;
    ll temp;
    for(i = 1; i <= 100; i++)
    {
        temp = n * i;
        while(temp != 0)
        {
            rem = temp % 10;
            mask = set1(mask, rem);
            temp /= 10;
        }
        //cout << "de " <<  n << endl;
        if(mask == ((1 << 10) - 1)) return n * i;
    }
    return -1;

}
int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("outputA.txt", "w", stdout);
    int t, tcase;
    SD(tcase);
    ll n;
    for(t = 1; t <= tcase; t++)
    {
        //SD(n);
        SLLD(n);
        ll ret = f(n);

        if(ret == -1) printf("Case #%d: INSOMNIA\n", t);
        else printf("Case #%d: %lld\n", t, ret);
    }
    return 0;
}
