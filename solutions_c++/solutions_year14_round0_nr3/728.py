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

int n, m, k;

int id(int i, int j, bool normal){
    return normal ? (i * m + j) : (j * n + i);
}

const int NMAX = 1000;

int ans[NMAX][NMAX];
int color(int x, int y, int push = 1){
    int add = 0;
    fori(dx, -1, 1)
        fori(dy, -1, 1){
            int i = x + dx, j = y + dy;
            if(0 <= i && i < n && 0 <= j && j < m && !ans[i][j])
                ans[i][j] = push, add++;
        }
    return add;
}

void go(int& cur, int i, int j){
    if(cur + color(i, j, 0) <= k){
        cur += color(i, j);
    }
}

void solve_test(){
    cin >> n >> m >> k;
    k = n * m - k;

    if(k == 1){
        forn(i, n){
            forn(j, m){
                printf(i == 0 && j == 0 ? "c" : "*");
            }
            puts("");
        }
        return;
    }

    if(n == 1 || m == 1){
        forn(i, n){
            forn(j, m){
                if(id(i, j, m == 1) < k){
                    printf(i == 0 && j == 0 ? "c" : ".");
                }else
                    printf("*");
            }
            puts("");
        }
        return;
    }

    if(n == 2 || m == 2){
        if(k % 2 != 0 || k < 4)
            puts("Impossible");
        else{
            forn(i, n){
                forn(j, m){
                    if(id(i, j, m == 2) < k)
                        printf(i == 0 && j == 0 ? "c" : ".");
                    else
                        printf("*");
                }
                puts("");
            }
        }
        return;
    }

    if(k < 4 || (k % 2 == 1 && k < 9)){
        puts("Impossible");
        return;
    }

    memset(ans, 0, sizeof ans);
    int cur = 0;
    go(cur, 0, 0);
    go(cur, 1, 0);
    go(cur, 0, 1);
    fore(j, 2, m)
        go(cur, 0, j);
    fore(i, 2, n)
        go(cur, i, 0);
    forn(i, n){
        forn(j, m){
            go(cur, i, j);
        }
    }

    assert(cur == k);

    forn(i, n){
        forn(j, m){
            if(ans[i][j])
                printf(i == 0 && j == 0 ? "c" : ".");
            else
                printf("*");
        }
        puts("");
    }
}

int main() {
    #ifdef ssu1
    assert(freopen("input.txt", "rt", stdin));
    assert(freopen("output.txt", "wt", stdout));
    #endif

    int tcases;
    cin >> tcases;
    fori(i, 1, tcases){
        printf("Case #%d:\n", i);
        solve_test();
//        fprintf(stderr, "-- Time for case %d = %.3lf\n\n", i, (((double)clock())/CLOCKS_PER_SEC));
    }

    return 0;
}


