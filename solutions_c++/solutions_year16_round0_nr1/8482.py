//#include <bits/stdc++.h>

#include<cstdio>
#include<cstring>
#include<cctype>
#include<cmath>
#include<cstdlib>

#include<iostream>
#include<string>
#include<algorithm>
#include<vector>
#include<stack>
#include<queue>
#include<set>
#include<map>
#include<bitset>
using namespace std;

#define popc(a) (__builtin_popcount(a))
//ll bigmod(ll a,ll b,ll m){if(b == 0) return 1%m;ll x = bigmod(a,b/2,m);x = (x * x) % m;if(b % 2 == 1) x = (x * a) % m;return x;}
//ll BigMod(ll B,ll P,ll M){ ll R=1%M; while(P>0) {if(P%2==1){R=(R*B)%M;}P/=2;B=(B*B)%M;} return R;} /// (B^P)%M

#define MX 100005
#define inf 100000000

typedef long long ll;
typedef unsigned long long ull;
typedef pair<int,int> pii;
typedef pair<ll,ll> pll;

const ll mod = 1000000007ll;

ll func(int n)
{
    int mask = (1<<10) - 1;
    for(int i = 1; i < 1000000; i++)
    {
        ll t = (ll) n*i;
        while(t>0)
        {
            int now = t%10;
            t/=10;
            mask = mask & (~(1<<now));
        }
        if(mask == 0) return (ll) i*n;
    }
    return -1;
}


int main() {
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
    int ti = 1000000;
    scanf("%d", &ti);
    for(int te = 1; te <= ti; te++)
    {
        int n;
        scanf("%d", &n);
        printf("Case #%d: ", te);
        if(n != 0)
            printf("%lld\n", func(n));
        else
            printf("INSOMNIA\n");

    }
    return 0;
}

