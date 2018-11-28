#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <algorithm>
#include <string>
#include <vector>
#include <stack>
#include <queue>
#include <set>
#include <map>
#include <time.h>
#include <cctype>
#include <functional>
#include <deque>
#include <iomanip>
#include <bitset>
#include <assert.h>
#include <numeric>
#include <sstream>
#include <utility>

#define pb push_back
#define mp make_pair
#define fi first
#define se second
#define all(a) (a).begin(),(a).end()
#define FOR(i,a,b) for (int i=(a);i<(b);i++)
#define FORD(i,a,b) for (int i=(a); i>=(b); i--)
#define REP(i,b) FOR(i,0,b)
#define ll long long
#define sf scanf
#define pf printf
using namespace std;
const int maxint = -1u>>1;
const double pi = 3.14159265358979323;
const double eps = 1e-8;
typedef pair<int,int> pii;
typedef vector<int> vi;
typedef vector<int>::iterator vit;

ll n, p, all;

ll calc1(ll sum, ll cnt) {
    if (cnt == 0) return 1;
    return sum / 2 + calc1(sum / 2, (cnt - 1) / 2);
}

ll calc2(ll sum, ll cnt) {
    if (cnt == 0) return 0;
    return sum / 2 + calc2(sum / 2, (cnt - 1) / 2);
}

bool check1(ll x) {
    ll rk = calc1(all, x);
    return rk <= p;
}
bool check2(ll x) {
    ll rk = all - calc2(all, all - 1 - x);
    return rk <= p;
}
int main() 
{
    freopen("B-large.in", "r", stdin);
    freopen("b.out", "w", stdout);
    int T, ca = 0;
    cin >>T;
    while (T--) {
        cin >>n >>p;
        all = (1LL << n);
        ll lo = 0, hi = all - 1, mid;
        ll ans1, ans2;
        while (lo <= hi) {
            mid = (lo + hi) >>1;
            if (check1(mid)) ans1 = mid, lo = mid + 1;
            else hi = mid - 1;
        }
        lo = 0, hi = all - 1, mid;
        while (lo <= hi) {
            mid = (lo + hi) >>1;
            if (check2(mid)) ans2 = mid, lo = mid + 1;
            else hi = mid - 1;
        }
        cout <<"Case #" <<++ca <<": " <<ans1 <<" "<<ans2 <<endl;
    }
    return 0;
}

