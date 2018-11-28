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

const int N = 10;
const int MOD = 1000000007;
const int INF = int(1e9) + 7;

int getCnt(const vector<string>& s) {
    set<string> st;
    forn(i, sz(s))
        forn(j, sz(s[i]) + 1)
            st.insert(s[i].substr(0, j));
    return sz(st);
}

int n, m;
string s[N];
int cnt[(1 << N) + 1];

pt z[N][(1 << N) + 1];

pt solve(int lf, int mask) {
    if (mask == 0)
        return pt(0, 0);        
    if (lf == 1)
        return pt(cnt[mask], 1);
    pt& res = z[lf][mask];
    if (res.X == -1) {
        res.X = 0;
        res.Y = 0;
        
        for (int smask = (mask - 1) & mask; smask > 0; smask = (smask - 1) & mask) {
            pt cur = solve(lf - 1, mask ^ smask);
            cur.X += cnt[smask];
            if (cur.Y == 0)
                continue;
                
            if (cur.X > res.X) {
                res.X = cur.X;
                res.Y = 0;
            }
            
            if (cur.X == res.X)
                res.Y += cur.Y;
                
            if (res.Y >= MOD)
                res.Y -= MOD;
        }
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
        cin >> n >> m;
        forn(i, n)
            cin >> s[i];    
            
        forn(mask, (1 << n)) {
            vector<string> st;
            forn(i, n)
                if ((mask >> i) & 1)
                    st.pb(s[i]);
            cnt[mask] = getCnt(st);
        }
        
        memset(z, -1, sizeof(z));
        
        pt res = solve(m, (1 << n) - 1);
        printf("Case #%d: %d %d\n", test + 1, res.X, res.Y);
    }
 
    return 0;
}

