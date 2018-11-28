#include <algorithm>
#include <iostream>
#include <cstring>
#include <sstream>
#include <cstdlib>
#include <utility>
#include <numeric>
#include <cstdio>
#include <string>
#include <vector>
#include <bitset>
#include <cmath>
#include <queue>
#include <stack>
#include <ctime>
#include <map>
#include <set>
using namespace std;
typedef pair<int, int> PII;
typedef vector<string> VS;
typedef map<int, int> MII;
typedef vector<PII> VPII;
typedef vector<int> VI;
typedef set<int> SI;
typedef long double LD;
typedef long long LL;
#define PB push_back
#define MP make_pair
#define FI first
#define SE second
const int inf = 1073741823;
const int maxint = 0x7fffffff;
const LL  INF = 1152921504606846976ll;
const LD  eps = 1E-9;
const LD  pi = 3.1415926535897932384626433832795;
template <class T> inline T _sqr(T a) {return (a*a);}
template <class T> inline T _abs(T a) {return (a>=0?a:-a);}
template <class T> inline T _lbt(T a) {return (a&(a^(a-1)));}
template <class T> inline T _max(T a, T b) {return (a>b?a:b);}
template <class T> inline T _min(T a, T b) {return (a<b?a:b);}
template <class T> inline T _smax(T a, T b, T c) {return _max(_max(a,b),c);}
template <class T> inline T _smin(T a, T b, T c) {return _min(_min(a,b),c);}
template <class T> inline T _sqrt(T a) {T b,c;for(b = sqrt(a),c=b-2;c<=b+2;c++)if(_sqr(c)<=a)b=c;return b;}
#define rep(i, n) for (int i = 0; i < n; i++)
#define kep(i, n) for (int i = 1; i<= n; i++)
#define ifo(i, l, r) for (int i = l; i <= r; i++)
#define dfo(i, r, l) for (int i = r; i >= l; i--)

LL n, p, m, ans;
int T;

bool check0(LL k, LL p) {
	LL t = k, token = m;
	while (t > 0) {
		token /=2;
		if (p <= token) return false;
		p -= token;
		t = (t - 1) /2;
	}
	return true;
}

bool check1(LL k, LL p) {
	LL t = m - k - 1, token = m;
	while (t > 0) {
		token /= 2;
		t = (t - 1) /2;
	}
	return (p >= token);
}

void find1(LL l, LL r) {
    for (LL mid = (l+r)/2; l<=r; mid = (l+r)/2) {
        if (check1(mid, p)) {
            ans = mid;
            l = mid+1;
        } else r = mid-1;
    }
}

void find0(LL l, LL r) {
    for (LL mid = (l+r)/2; l<=r; mid = (l+r)/2) {
        if (check0(mid, p)) {
            ans = mid;
            l = mid+1;
        } else r = mid-1;
    }
}

void Solution_Production() {
    scanf("%lld%lld", &n, &p);
    m = (1ll << n);
    ans = 0;
    find0(1, (1ll << n) -1);
    cout << ans << " ";
    ans = 0;
    find1(1, (1ll << n) -1);
    cout << ans << endl;
}

int main(){
    freopen("B-large.in", "r", stdin);
    freopen("B-large.out", "w", stdout);
    scanf("%d", &T);
    kep(_, T) {
        printf("Case #%d: ", _);
        Solution_Production();
    }
    return 0;
}

