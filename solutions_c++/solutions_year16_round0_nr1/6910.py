#include<map>
#include<set>
#include<cmath>
#include<queue>
#include<bitset>
#include<math.h>
#include<cstdio>
#include<vector>
#include<string>
#include<cstring>
#include<iostream>
#include<algorithm>
#pragma comment(linker, "/STACK:102400000,102400000")
using namespace std;
const int N=100010;
const int MAX=151;
const int mod=100000000;
const int MOD1=100000007;
const int MOD2=100000009;
const double EPS=0.00000001;
typedef long long ll;
const ll MOD=1000000009;
const ll INF=10000000010;
typedef double db;
typedef unsigned long long ull;
int get(ll x) {
    int ret=0;
    while (x) { ret|=(1<<(x%10));x/=10; }
    return ret;
}
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    int i,j,t,w;
    ll n,m;
    scanf("%d", &t);
    for (i=1;i<=t;i++) {
        scanf("%lld", &n);
        if (!n) printf("Case #%d: INSOMNIA\n", i);
        else {
            w=get(n);m=n;
            if (w==1023) printf("Case #%d: %lld\n", i, n);
            for (j=1;j<=2000000;j++) {
                m+=n;w|=get(m);
                if (w==1023) break ;
            }
            printf("Case #%d: %lld\n", i, m);
        }
    }
    return 0;
}

/*
5
0
1
2
11
1692
*/





























