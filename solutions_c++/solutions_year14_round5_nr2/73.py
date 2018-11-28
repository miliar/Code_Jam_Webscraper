#undef NDEBUG
#ifdef ssu1
#define _GLIBCXX_DEBUG
#endif

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

const int N = 1010;
const int INF = int(1e9);

int n, p, q;
int h[N], g[N];

int z[N], d[2][N][N];

int getFree(int hp) {
    if (hp <= 0)
        return -INF;
        
    int& res = z[hp];
    if (res == -1) {
        res = -INF;
        if (hp <= p)   
            res = 0;
        res = max(res, getFree(hp - q) + 1);
        res = max(res, getFree(hp - p - q));
        
        if (res < 0)
            res = -INF;
            
        //cerr << "z " << hp << " " << res << endl;
    }
    
    return res;
}

int solve(int pl, int idx, int x) {
    if (idx >= n)
        return 0;
    int& res = d[pl][idx][x];
    if (res == -1) {
        int hp = h[idx];
        if (pl)
            hp = max(0, hp - q);
    
        res = solve(0, idx + 1, x + (hp + q - 1) / q);
            
        for (int cnt = 0; cnt <= x; cnt++) {
            int left = h[idx] - cnt * p;
            if (left <= 0) {
                res = max(res, g[idx] + solve(pl, idx + 1, x - cnt));
                break;
            }
            
            if (pl) {
                left -= q;
                if (left <= 0)
                    continue;
            }
                        
            if (getFree(left) >= 0) {
                int cur = g[idx] + solve(1, idx + 1, x - cnt + getFree(left));
                if (cur > res) 
                    res = cur;                     
            }
        }
        
        //cerr << "d " << pl << " " << idx << " " << x << " " << res << endl;;        
    }
    
    return res;
}

int main() {
    #ifdef ssu1
    assert(freopen("input.txt", "rt", stdin));
    #endif

    int tests;
    cin >> tests;
    
    forn(test, tests) {
        cin >> p >> q >> n;
        
        forn(i, n)
            cin >> h[i] >> g[i];
        
        memset(z, -1, sizeof(z));            
        memset(d, -1, sizeof(d));

        printf("Case #%d: ", test + 1);        
        cout << solve(0, 0, 0) << endl;                    
    }
 
    return 0;
}

