#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <bitset>
#include <sstream>
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

using namespace std;

#define forn(i, n) for(int i = 0; i < int(n); ++i)
#define for1(i, n) for(int i = 1; i <= int(n); ++i)
#define ford(i, n) for(int i = int(n) - 1; i >= 0; --i)
#define fore(i, l, r) for(int i = int(l); i < int(r); ++i)
#define forit(i, v) for(typeof((v).begin()) i = (v).begin(); i != (v).end(); ++i)
#define sz(v) int((v).size())
#define all(v) (v).begin(), (v).end()
#define pb push_back
#define X first
#define Y second
#define mp make_pair
template<typename T> inline T abs(T a){ return ((a < 0) ? -a : a); }
template<typename T> inline T sqr(T a){ return a * a; }

typedef long long li;
typedef long double ld;
typedef pair<li, li> pt;

const int INF = (int)1E9 + 7;
const ld EPS = 1E-9;
const ld PI = 3.1415926535897932384626433832795;

const li mod = 1000002013;

struct rec{
    int x, y, p;
    rec(){}
};

bool operator < (const rec& a, const rec& b){
    return a.x < b.x || (a.x == b.x && a.y < b.y);
}

li n;

inline li dist(li x){
    if(x == 0) return 0;
    return ((x * (n+1)) % mod - ((x*(x+1))>>1) % mod + mod) % mod;
}

bool inter(rec& a, rec& b){
    return max(a.x, b.x) <= min(a.y, b.y);
}

bool in(rec& a, rec& b){
    return a.x <= b.x && b.y <= a.y;
}

li cost(rec& a){
    assert(a.x <= a.y);
    return (dist(a.y - a.x) * a.p) % mod;
}

int main() {
    #ifdef myproject
    freopen("input.txt", "rt", stdin);
    //freopen("output.txt", "wt", stdout);
    #endif

    int tests;
    cin >> tests;
    forn(testsit, tests){
        printf("Case #%d: ", testsit+1);

        int m;
        cin >> n >> m;

        vector<rec> a(m);
        
        li ans = 0;

        forn(i, sz(a)){
            cin >> a[i].x >> a[i].y >> a[i].p;
            ans += cost(a[i]);
            ans %= mod;
        }

        while(true){
            sort(all(a));

            bool was = false;

            int sza = sz(a);
            forn(i, sza){
                forn(j, i){
                    if(inter(a[i], a[j]) && !(in(a[i], a[j]) || in(a[j], a[i]))){
                        was = true;

                        int cnt = min(a[i].p, a[j].p);

    //                    li scost = cost(a[i]) + cost(a[j]);
                        a[i].p -= cnt;
                        a[j].p -= cnt;

                        {
                            rec f;
                            f.x = min(a[i].x, a[j].x);
                            f.y = max(a[i].y, a[j].y);
                            f.p = cnt;
                            a.pb(f);
                        }

                        {
                            rec s;
                            s.x = max(a[i].x, a[j].x);
                            s.y = min(a[i].y, a[j].y);
                            s.p = cnt;
                            a.pb(s);
                        }
    //                    assert(scost >= cost(a[i]) + cost(a[j]) + cost(a.back()) + cost(a[sz(a)-2]));
                    }
                }
            }

            if(!was) break;

            vector<rec> na;
            forn(i, sz(a)){
                if(a[i].p > 0)
                    na.pb(a[i]);
            }
            a = na;
        }

        li cur = 0;
        forn(i, sz(a)){
            cur += cost(a[i]);
            cur %= mod;
        }

//        cerr << ans << " " << cur << " " << (ans>cur) << endl;

        cout << (ans-cur+mod) % mod << endl;
        cerr << "testsit=" << testsit+1 << " " << clock() << endl;
    }
    return 0;
}


