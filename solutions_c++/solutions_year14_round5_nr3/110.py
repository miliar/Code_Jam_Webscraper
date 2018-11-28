#ifdef ssu1
#define _GLIBCXX_DEBUG
#endif
#undef NDEBUG

#include <algorithm>
#include <functional>
#include <numeric>
#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstring>
#include <cassert>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <bitset>
#include <sstream>

using namespace std;

#define fore(i, l, r) for(int i = int(l); i < int(r); ++i)
#define forn(i, n) fore(i, 0, n)
#define fori(i, l, r) fore(i, l, (r) + 1)
#define forit(i, a) for(typeof((a).begin()) i = (a).begin(); i != (a).end(); ++i)
#define sz(v) int((v).size())
#define all(v) (v).begin(), (v).end()
#define pb push_back
#define mp make_pair
#define X first
#define Y second

template<typename T> inline T abs(T a){ return ((a < 0) ? -a : a); }
template<typename T> inline T sqr(T a){ return a * a; }

typedef long long li;
typedef long double ld;
typedef pair<int, int> pt;

const int INF = (int)1E9 + 7;
const ld EPS = 1E-9;
const ld PI = 3.1415926535897932384626433832795;

map<int, int> idx;
int getIdx(int v){
    if(idx.count(v) == 0){
        int cur = sz(idx);
        idx[v] = cur;
    }
    return idx[v];
}

const int NMAX = 17;
int d[NMAX][1 << NMAX];

int bit(int mask, int i){
    return (mask >> i) & 1;
}

void solve_test(){
    int n;
    cin >> n;
    vector<pt> a(n);
    idx.clear();
    forn(i, n){
        char c;
        cin >> c >> a[i].Y;

        a[i].X = (c == 'E' ? +1 : -1);
        a[i].Y--;

        if(a[i].Y != -1){
            a[i].Y = getIdx(a[i].Y);
        }
    }

    memset(d, 0, sizeof d);

    forn(mask, 1 << n){
        d[0][mask] = 1;
    }

    forn(step, n){
        forn(mask, 1 << n){
            if(!d[step][mask])
                continue;

            if(a[step].X > 0){
                if(a[step].Y == -1){
                    forn(i, n){
                        if(bit(mask, i) == 0)
                            d[step + 1][mask ^ (1 << i)] = 1;
                    }
                }else{
                    if(bit(mask, a[step].Y) == 0)
                        d[step + 1][mask ^ (1 << a[step].Y)] = 1;
                }
            }else{
                if(a[step].Y == -1){
                    forn(i, n){
                        if(bit(mask, i) == 1)
                            d[step + 1][mask ^ (1 << i)] = 1;
                    }
                }else{
                    if(bit(mask, a[step].Y) == 1)
                        d[step + 1][mask ^ (1 << a[step].Y)] = 1;
                }
            }
        }
    }

    int ans = 100;
    forn(mask, 1 << n){
        if(d[n][mask]){
            ans = min(ans, __builtin_popcount(mask));
        }
    }

    if(ans == 100)
        puts("CRIME TIME");
    else
        cout << ans << endl;
}

int main(int argc, char* argv[]) {
    #ifdef ssu1
    const char* filename = argc >= 2 ? argv[1] : "input.txt";
    assert(freopen(filename, "r", stdin));
    #endif

    int tcases;
    cin >> tcases;
    fori(i, 1, tcases){
        printf("Case #%d: ", i);
        solve_test();
        fprintf(stderr, "-- Time for case %d = %.3lf\n\n", i, (((double)clock())/CLOCKS_PER_SEC));
    }

    return 0;
}


