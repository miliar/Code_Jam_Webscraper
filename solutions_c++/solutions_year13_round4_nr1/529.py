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
#define N 111

int n, m, k, t, x, y, p, T, up[N], down[N], card[N], ans, maxn;

void Solution_Production() {
	ans = 0;
	maxn = 0;
	memset(card, 0, sizeof(card));
	memset(up, 0, sizeof(up));
	memset(down, 0, sizeof(down));
    scanf("%d%d", &n, &m);
	rep(i, m) {
		scanf("%d%d%d", &x, &y, &p);
		up[x] += p;
		down[y] += p;
		maxn += p*(21-y+x) * (y-x)/ 2;
	}
	//cout << maxn << endl;
	kep(i, n) {
		card[i] += up[i];
		for (t = down[i], p = i; t; p--) {
			k = min(t, card[p]);
			ans += k * (21-i+p) * (i-p)/ 2;
			t -= k;
            card[p] -= k;
		}
	}
	printf("%d\n", maxn - ans);
}

int main(){
    freopen("a.in", "r", stdin);
    freopen("a.out", "w", stdout);
    scanf("%d", &T);
    kep(_, T) {
        printf("Case #%d: ", _);
        Solution_Production();
    }
    return 0;
}

