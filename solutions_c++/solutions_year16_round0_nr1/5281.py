#define _USE_MATH_DEFINES
#define _CRT_SECURE_NO_DEPRECATE
#define _SECURE_SCL 0
#include <algorithm>
#include <bitset>
#include <cassert>
#include <cctype>
#include <ctime>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <deque>
#include <iostream>
#include <list>
#include <map>
#include <memory.h>
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

int n;

bool read(){
    return scanf("%d", &n) == 1;
}

void solve(int test){
    printf("Case #%d: ", test);
    set <int> c;
    ll cur = n;
    ll ans = -1;
    forn(i,1000000) {
        ll tcur = cur;
        while (tcur > 0) {
            c.insert(tcur % 10);
            tcur /= 10;
        }
        if (sz(c) == 10) {
            ans = cur;
            break;
        }
        cur += n;
    }
    if (ans == -1) {
        cout << "INSOMNIA" << endl;
    } else {
        cout << ans << endl;
    }
}

int main(){
#ifdef dudkamaster
    freopen("input.txt","rt",stdin);
    freopen("output.txt","wt",stdout);
#endif
    int t;
    scanf("%d", &t);
    for (int tt = 1; tt <= t; tt++) {
        read();
        solve(tt);
    }
    return 0;
}
