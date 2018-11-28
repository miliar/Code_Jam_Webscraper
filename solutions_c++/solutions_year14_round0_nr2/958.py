#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <limits>
#include <cstring>
#include <string>
using namespace std;

#define pairii pair<int, int>
#define llong long long
#define pb push_back
#define sortall(x) sort((x).begin(), (x).end())
#define INFI  numeric_limits<int>::max()
#define INFL  numeric_limits<long>::max()
#define INFLL numeric_limits<llong>::max()
#define INFD  numeric_limits<double>::max()
#define MOD 1000000007
#define PI 3.1415926535897932384626433832795028841971693993751058209749445923
#define FOR(i,s,n) for (llong (i) = (s); (i) < (n); (i)++)
#define FORZ(i,n) FOR((i),0,(n))

typedef long double LD;

void solve() {
    cout << fixed << setprecision(12);
    LD c,f,x; cin >> c >> f >> x;
    llong h = (f*x-f*c-2*c) / (c*f);
    if (h < 0) {
        cout << x/2.0 << endl;
        return;
    }
    if ((x-c)/(2+f*(LD)h) > x/(f+2+f*(LD)h)) h++;
    LD res = 0.0;
    LD k = 2.0;
    FORZ(i, h+1) {
        res += c/k;
        k += f;
    }
    res += (x-c)/(k-f);
    cout << res << endl;
}

int main() {
#ifdef DEBUG
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
#endif
    
    int t; cin >> t;
    FORZ(i,t) {
        cout << "Case #" << i+1 << ": ";
        solve();
    }
    
    return 0;
}
