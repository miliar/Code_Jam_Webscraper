#include <cstdio>
#include <cstdlib>
#include <algorithm>

using namespace std;

typedef long long llint;

llint p, q;

bool ispower(long long a) {
    for(long long i=1; i<=a; i<<=1) {
        if(i==a) return 1;
    }
    return 0;
}

int sol(long long a, long long b) {
    if(a>=b/2) return 1;
    else return 1+sol(a, b/2);
}

int main () {
    int t;
    scanf("%d", &t);
    for(int i=1;i<=t; ++i) {
    scanf("%lld/%lld", &p, &q);
    long long d = __gcd(p,q);
    p/=d;
    q/=d;
    if(!ispower(q)) printf("Case #%d: impossible\n", i);
    else printf("Case #%d: %d\n", i,sol(p,q));
    }
    return 0;
}
