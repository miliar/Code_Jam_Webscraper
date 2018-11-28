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

const int N = 20; 
const int INF = int(1e9) + 1;

int n;
pt e[N];
vector<int> ids;

int z[2][N][N][(1 << 15) + 10];

int solve(bool in, int id, int pos, int mask) {
    if (pos == n) {
        int cnt = (in ? 1 : 0);
        if (id + 1 >= sz(ids))
            return (mask == 0) ? cnt : INF;
        else
            return cnt + min(solve(false, id + 1, 0, mask), solve(true, id + 1, 0, mask));
    }
    
    int& res = z[in][id][pos][mask];
    if (res == -1) {
        if (e[pos].Y != -1 && e[pos].Y != id)
            return res = solve(in, id, pos + 1, mask);
        if (e[pos].Y == id) {
            if (e[pos].X == in)
                return res = solve(!in, id, pos + 1, mask);
            else
                return res = INF;
        }
        
        res = solve(in, id, pos + 1, mask);
        if (((mask >> pos) & 1) && in == e[pos].X) {
            res = min(res, solve(!in, id, pos + 1, mask ^ (1 << pos)));
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
        cin >> n;

        ids.clear();

        forn(i, n){
            char c;
            assert(scanf(" %c %d", &c, &e[i].Y) == 2);
            e[i].Y--;
            e[i].X = (c == 'L') ? 1 : 0;
            
            if (e[i].Y != -1)
                ids.pb(e[i].Y);
        }
        
        sort(all(ids));
        ids.erase(unique(all(ids)), ids.end());
        
        forn(i, n)
            if (e[i].Y != -1)
                e[i].Y = (int) (lower_bound(all(ids), e[i].Y) - ids.begin());
                
        while (sz(ids) < n)
            ids.pb(sz(ids));
        
        int mask = 0;
        forn(i, n)
            if (e[i].Y == -1)
                mask |= (1 << i);
        
        memset(z, -1, sizeof(z));        
        int ans = min(solve(0, 0, 0, mask), solve(1, 0, 0, mask));
        
        printf("Case #%d: ", test + 1);
        if (ans > (INF >> 1))
            puts("CRIME TIME");
        else
            printf("%d\n", ans); 
    }
     
    return 0;
}

