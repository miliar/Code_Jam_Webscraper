#ifdef ssu1
#define _GLIBCXX_DEBUG
#define _DEBUG_ 1
#else
#define _DEBUG_ 0
#endif

#include <iostream>
#include <algorithm>
#include <numeric>
#include <functional>
#include <cmath>
#include <ctime>
#include <cstring>
#include <cassert>
#include <cstdlib>
#include <cstdio>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <deque>
#include <list>
#include <bitset>
#include <sstream>

using namespace std;

#define fore(i, l, r) for(int i = (l); i < (r); ++i)
#define forn(i, n) fore(i, 0, n)
#define fori(i, l, r) fore(i, l, (r) + 1)
#define X first
#define Y second
#define sz(v) ((int)(v).size())
#define all(v) (v).begin(), (v).end()
#define pb push_back
#define mp make_pair
#define db(x) if(_DEBUG_){ cout << __FUNCTION__ << "(" << __LINE__ << "): " << #x << " = " << x << endl; }
#define dbi(x, y) if(_DEBUG_){ cout << __FUNCTION__ << "(" << __LINE__ << "): [" << #x << "] ~ [" << #y << "]\n"; for(typeof(x) i = x; i != y; ++i) { cout << *(i) << " "; } cout << endl; }

typedef long long li;
typedef long double ld;
typedef pair<int, int> pt;

const int INF = int(1e9) + 7;
const ld PI = acosl(ld(-1));
const ld EPS = 1e-9;

const int MAGIC = 100000;

ld c, f, x;

int main(){
    #ifdef ssu1
    assert(freopen("input.txt", "r", stdin));
    #endif

    int tests;
    cin >> tests;
    
    cout.precision(10);
    cout << fixed;
    
    forn(test, tests) {        
        printf("Case #%d: ", test + 1);
        cin >> c >> f >> x;
        
        ld ans = x / 2;
        
        ld bf = 0;        
        for (int fc = 0; fc <= MAGIC; ++fc) {
            ans = min(ans, bf + x / (2  + fc * f));
            bf += c / (2 + fc * f);
        }
        
        cout << ans << endl;
    }

    return 0;
}
