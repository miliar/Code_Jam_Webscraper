#include <bits/stdc++.h>

#define rep(i,n) for(i=0; i<n; i++)
#define repl(i,n) for(i=1; i<=n; i++)

#define sz(x) (int) x.size()
#define pb push_back
#define all(x) x.begin(),x.end()
#define uu first
#define vv second
#define mem(x, y) memset(x, y, sizeof(x))
#define un(x) x.erase(unique(all(x)), x.end())

#define sdi(x) scanf("%d", &x)
#define sdii(x, y) scanf("%d %d", &x, &y)
#define sdiii(x, y, z) scanf("%d %d %d", &x, &y, &z)
#define sdl(x) scanf("%lld", &x)
#define sdll(x, y) scanf("%lld %lld", &x, &y)
#define sdlll(x, y, z) scanf("%lld %lld %lld", &x, &y, &z)
#define sds(x) scanf("%s", x)
#define pfi(x) printf("%d\n", x)
#define pfii(x, y) printf("%d %d\n", x, y)
#define pfiii(x, y, z) printf("%d %d %d\n", x, y, z)
#define pfl(x) printf("%lld\n", x)
#define pfll(x, y) printf("%lld %lld\n", x, y)
#define pflll(x, y, z) printf("%lld %lld %lld\n", x, y, z)

#define eps 1e-9
#define OK cerr << "ok\n"
#define DB(x) cerr << #x << " = " << x << endl

using namespace std;

typedef long long LL;
typedef unsigned long long ULL;
typedef long double LD;
typedef pair <int, int> pii;

inline int setBit(int N, int pos) { return N=N | (1<<pos); }
inline int resetBit(int N, int pos) { return N= N & ~(1<<pos); }
inline bool checkBit(int N, int pos) { return (bool)(N & (1<<pos)); }

//int kx[] = {+2, +1, -1, -2, -2, -1, +1, +2};
//int ky[] = {+1, +2, +2, +1, -1, -2, -2, -1}; //Knight Direction
//int fx[] = {+0, +0, +1, -1, -1, +1, -1, +1};
//int fy[] = {-1, +1, +0, +0, +1, +1, -1, -1}; //Four & Eight Direction

const int MAX = 10000;
int n, k;
char str[MAX];

inline int solve() {
    char now[MAX];
    int i, j, ret=0;
    strcpy(now, str);
    rep(i, n) {
        if(now[i] == '+') continue;
        else if(i+k<=n) {
            for(j=i; j<i+k; j++) {
                if(now[j] == '+') now[j] = '-';
                else now[j] = '+';
            }
            ret++;
        }
    }
    rep(i, n) if(now[i] == '-') return -1;
    return ret;
}

int main() {
//    assert(freopen("in.txt","r",stdin));
//    assert(freopen("out.txt","w",stdout));
//    assert(freopen("A-large.in","r",stdin));
//    assert(freopen("A-large.out","w",stdout));

    int test, kase=1, i;

    sdi(test);
    while(test--) {
        sds(str);
        sdi(k);
        n = strlen(str);
        printf("Case #%d: ", kase++);
        int ret = solve();
        reverse(str, str+n);
        ret = min(ret, solve());
        if(ret == -1) puts("IMPOSSIBLE");
        else pfi(ret);
    }

    return 0;
}
