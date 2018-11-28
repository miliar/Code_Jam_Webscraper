#include <iostream>
#include <fstream>
#include <algorithm>
#include <vector>
#include <unordered_map>
#include <stack>
#include <queue>
#include <set>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <climits>
#include <cfloat>
#include <cstdlib>

#ifdef _WIN32
#define LLD "%I64d"
#else
#define LLD "%lld"
#endif

using namespace std;

#define pb push_back
#define mp make_pair
#define fs first
#define sc second

#define ri(X) scanf("%d", &(X))
#define rii(X, Y) scanf("%d%d", &(X), &(Y))
#define riii(X, Y, Z) scanf("%d%d%d", &(X), &(Y), &(Z))
#define all(a) (a).begin(),(a).end()
#define sz(s) ((int) ((s).size()))
#define forn(i, n) for (int i = 0; i < (int)(n); ++i)
#define fornr(i, n) for (int i = (int)(n)-1; i>=0; --i)
#define for1(i, n) for (int i = 1; i <= (int)(n); ++i)
#define for1r(i, n) for (int i = (int)(n); i>0; --i)

#define INF 0x3f3f3f3f
#define INFL 0x3f3f3f3f3f3f3f3fLL

typedef pair<int,int> pii;
typedef vector<int> vi;
typedef long long ll;
typedef vector<ll> vll;

int mod1 = int(1e9) + 7;

#define MX 100100

ll po[11][16];

void main2(){

    printf("\n");

    int n,j;
    rii(n,j);

    forn(i, j) {
        vll d;
        ll x = (1LL << ((n/2)-1)) + 1LL + (i<<1);

        for(int b=2; b<11; b++) {
            ll fac = 0, y=x;
            int p=0;
            while(y>0) {
                if(y%2) fac += po[b][p];
                p++;
                y /= 2;
            }
            d.pb(fac);
        }

        x += x << (n/2);

        vi bits;
        while(x>0) {
            bits.pb(x%2);
            x /= 2;
        }
        reverse(all(bits));

        forn(k,n) {
            printf("%d", bits[k]);
        }
        forn(k,d.size()) {
            printf(" " LLD, d[k]);
        }
        printf("\n");
    }

}


int main(){

    for(ll b=2; b<11; b++) {
        po[b][0] = 1LL;
        for(int p=1; p<15; p++) {
            po[b][p] = po[b][p-1] * b;
        }
    }

    int t;
    ri(t);

    for1(cas,t) {
        printf("Case #%d: ", cas);
        main2();
    }

    return 0;
}
