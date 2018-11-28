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
typedef pair<int, int> pt;

const int INF = (int)1E9 + 7;
const ld EPS = 1E-9;
const ld PI = 3.1415926535897932384626433832795;

const int NMAX = 100;

int n;
int a[NMAX], b[NMAX];

int c[NMAX], u[NMAX], l[NMAX], tmp[NMAX], cb[NMAX];

void build(int a[NMAX], int res[NMAX]){
    memset(tmp, 63, sizeof(int) * (n + 2));
    tmp[0] = -INF;

    forn(i, n){
        int ptr = lower_bound(tmp, tmp + n, a[i]) - tmp;
        ptr--;

        tmp[ptr + 1] = a[i];
        res[i] = ptr + 1;
    }
}

bool brute(int idx){
    if(idx == n){
        reverse(c, c + n);
        build(c, cb);

        bool ok = true;
        forn(i, n){
            if(b[i] != cb[i]){
                ok = false;
                break;
            }
        }
        reverse(c, c + n);

        return ok;
    }

    forn(val, n){
        if(u[val])
            continue;
        u[val] ^= 1;

        int ptr = lower_bound(l, l + n, val) - l;
        ptr--;

        if(a[idx] == ptr+1){
            int lval = l[ptr+1];
            l[ptr+1] = val;

            c[idx] = val;

            if(brute(idx + 1))
                return true;

            l[ptr+1] = lval;
        }

        u[val] ^= 1;
    }

    return false;
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

        cin >> n;
        forn(i, n)
            cin >> a[i];
        forn(i, n)
            cin >> b[i];

        memset(u, 0, sizeof u);
        memset(c, -1, sizeof c);
        memset(l, 63, sizeof l); l[0] = -INF;
        reverse(b, b + n);

        if(brute(0)){
            forn(i, n)
                cout << c[i]+1 << " ";
            cout << endl;
        }else{
            cout << "fuck!!!" << endl;
        }
            
        cerr << "testsit=" << testsit+1 << " " << clock() << endl;
    }
    return 0;
}


