#include <algorithm>
#include <cassert>
#include <complex>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <map>
#include <queue>
#include <set>
#include <sstream>
#include <vector>
using namespace std;

#define FR(i,a,b) for(int i=(a);i<(b);++i)
#define FOR(i,n) FR(i,0,n)
#define CLR(x,a) memset(x,a,sizeof(x))
#define setmin(a,b) a = min(a,b)
#define PB push_back
#define FORALL(i,v) for(typeof((v).end())i=(v).begin();i!=(v).end();++i)
#define MP make_pair
#define A first
#define B second
#define RF(i,a,b) for(int i=(a)-1;i>=(b);--i)
#define BEND(v) (v).begin(),(v).end()
#define SZ(v) int((v).size())
#define FORI(i,v) FOR(i,SZ(v))
typedef long double ld;
typedef long long ll;

int K, C, S;

void doit(int cas)
{
    scanf(" %d %d %d", &K, &C, &S);
    assert(1 <= K && K <= 100);
    assert(1 <= C && C <= 100);
    assert(1 <= S && S <= K);

    printf("Case #%d:", cas);

    if (K > S*C) {
        printf(" IMPOSSIBLE\n");
        return;
    }

    int count = 0;
    bool done = false;
    int d = 0;
    while (!done) {
        ll x = 0;
        FOR(i,C) {
            x *= K;
            x += d;
            d = (d + 1) % K;

            if (d == 0) done = true;
        }

        printf(" %lld", x+1);
        ++count;
    }

    printf("\n");

    assert(count == (K + C - 1) / C);
}

int T;
int main() {
    scanf(" %d", &T);
    assert(1 <= T && T <= 100);
    FOR(cas,T) doit(cas+1);
    return 0;
}
