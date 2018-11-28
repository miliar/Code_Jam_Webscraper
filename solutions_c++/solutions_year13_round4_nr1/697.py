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

#define forn(i, n) for(int i = 0; i < int(n); ++i)
#define for1(i, n) for(int i = 1; i <= int(n); ++i)
#define ford(i, n) for(int i = int(n) - 1; i >= 0; --i)
#define fore(i, l, r) for(int i = int(l); i < int(r); ++i)
#define sz(v) int((v).size())
#define all(v) (v).begin(), (v).end()
#define pb push_back
#define mp make_pair
#define X first
#define Y second

typedef long long li;
typedef long double ld;
typedef pair<li, li> pt;

template<typename T> T abs(T a) { return a < 0 ? -a : a; }
template<typename T> T sqr(T a) { return a*a; }

const int INF = (int)1e9;
const ld EPS = 1e-9;
const ld PI = 3.1415926535897932384626433832795;

const int N = 2010;
const int M = 1000002013;

li n, m;
li lf[N], rg[N], cnt[N];

set< pair<pt, li> > s;
vector< pair<pt, li> > evs;

inline li score(li dist){
    if(dist == 0)
        return 0;
    return (n * 1ll * dist - ((dist * 1ll * (dist - 1)) >> 1)) % M;
}

int main(){
    #ifdef ssu1
        freopen("input.txt", "rt", stdin);
        //freopen("output.txt", "wt", stdout);
    #endif

    int tests;
    cin >> tests;
    forn(test, tests){
        printf("Case #%d: ", test + 1);

        cin >> n >> m;
        forn(i, m)
            cin >> lf[i] >> rg[i] >> cnt[i];
        
        li sum = 0;
        forn(i, m){
            sum = (sum + cnt[i] * score(rg[i] - lf[i])) % M;
            
            evs.pb(mp(pt(lf[i], -1), cnt[i]));
            evs.pb(mp(pt(rg[i], 1), cnt[i]));
        }
            
        li opt = 0;
        
        sort(all(evs));
        
        forn(i, sz(evs)){
            if(evs[i].X.Y == -1){
                s.insert(mp(pt(evs[i].X.X, evs[i].Y), i));
            }else{
                li nc = evs[i].Y;
                while(nc > 0){
                    pair<pt, int> r = (*s.rbegin());
                    s.erase(--s.end());
                    
                    li c = min(nc, r.X.Y);
                    opt = (opt + score(evs[i].X.X - r.X.X) * c) % M;
                                        
                    nc -= c;
                    r.X.Y -= c;
                    if(r.X.Y > 0)
                        s.insert(r);
                }
            }  
        }

        evs.clear();   
        s.clear();
        
        cout << ((sum - opt) % M + M) % M << endl;
    }
    
    return 0;
}
