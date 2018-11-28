# define _USE_MATH_DEFINES
#include <algorithm>
#include <bitset>
#include <cassert>
#include <cctype>
#include <ctime>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <deque>
#include <functional>
#include <fstream>
#include <iostream>
#include <map>
#include <memory.h>
#include <numeric>
#include <queue>
#include <set>
#include <stack>
#include <string>
#include <sstream>
#include <vector>
#include <utility>
#include <cmath>
using namespace std;

#define pb push_back
#define mp make_pair
#define sz(a) (int)(a).size()
#define all(a) (a).begin(), (a).end()

#define forn(i,n) for (int i=0; i<int(n); ++i)

typedef long long ll;
typedef long double ld;
typedef unsigned long long ull;


const int INF = (int) 1e9;
const long long INF64 = (long long) 1e18;
const long double eps = 1e-9;
const long double pi = 3.14159265358979323846;

map <vector <int>, int> ans;

int calc(vector <int> &p) {
    if (sz(p) == 0) return ans[p] = 0;
    if (ans.count(p)!=0) return ans[p];
    int res = INF;
    vector <int> ep, mp;
    forn(i,sz(p))
        if (p[i] > 1)
            ep.pb(p[i]-1);
    sort(all(ep));
    res = min(res, calc(ep));
    int mxi = 0;
    forn(i,sz(p))
        if (p[i] > p[mxi])
            mxi = i;
    if (p[mxi] > 1) {
        for (int j=1; j<=p[mxi]/2; j++){
            vector <int> mp = p;
            mp[mxi] = j;
            mp.pb(p[mxi]-j);
            sort(all(mp));
            res = min(res, calc(mp));
        }
    }
    ans[p] = res + 1;
    return ans[p];
}

int main(){
#ifdef dudkamaster
    freopen("input.txt","rt",stdin);
    freopen("output.txt","wt",stdout);
#endif
    int t;
    scanf("%d", &t);
    forn(test,t) {
        int d;
        scanf("%d", &d);
        vector <int> p(d);
        forn(i,d)
            scanf("%d", &p[i]);
        sort(all(p));
        printf("Case #%d: %d\n", test+1, calc(p));
    }
    return 0;
}
