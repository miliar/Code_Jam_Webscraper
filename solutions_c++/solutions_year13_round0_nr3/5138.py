#include <iostream>
#include <algorithm>
#include <numeric>
#include <functional>
#include <cmath>
#include <ctime>
#include <cstring>
#include <cassert>
#include <cstdio>
#include <cstdlib>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <deque>
#include <sstream>
#include <list>
#include <bitset>

using namespace std;

#define forn(i, n) for(int i = 0; i < int(n); ++i)
#define for1(i, n) for(int i = 1; i <= int(n); ++i)
#define fore(i, l, r) for(int i = int(l); i < int(r); ++i)
#define ford(i, n) for(int i = int(n) - 1; i >= 0; --i)
#define forit(i, s) for(typeof((s).begin()) i = (s).begin(); i != (s).end(); ++i)
#define X first
#define Y second
#define pb push_back
#define mp make_pair
#define all(v) (v).begin(), (v).end()
#define sz(v) int((v).size())

template<typename T> T abs(T a) { return a < 0 ? -a : a; }
template<typename T> T sqr(T a) { return a * a; }

typedef long long li;
typedef long double ld;
typedef pair<int, int> pt;

const int INF = int(1e9) + 7;
const ld EPS = 1e-9;
const ld PI = acos(-1.0);

vector<li> ans;

int st[20], szst;
bool pal(li val){
    szst = 0;
    while(val > 0){
        st[szst++] = val % 10;
        val /= 10;
    }
    
    forn(i, szst)
        if(st[i] != st[szst - i - 1]){
            return false;
        }
    return true;
}

int main(){
    #ifdef ssu1
    freopen("input.txt", "r", stdin);
//    freopen("output.txt", "w", stdout);
    #endif
    
    for1(val, 11000000){
        if(pal(val) && pal(val*li(val))){
            ans.pb(val * li(val));
        }
    }
    
    int t;
    cin >> t;
    forn(ti, t){
        li lf, rg;
        cin >> lf >> rg;
        
        int i1 = lower_bound(all(ans), lf) - ans.begin();
        int i2 = upper_bound(all(ans), rg) - ans.begin();
        
        printf("Case #%d: %d\n", ti + 1, max(0, i2 - i1));
    }
    return 0;
}
