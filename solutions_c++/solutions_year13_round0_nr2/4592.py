#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cctype>
#include <string>
#include <bitset>
#include <vector>
#include <deque>
#include <algorithm>
#include <functional>
#include <utility>
#include <stack>
#include <queue>
#include <set>
#include <map>
#define Fill(a, b) memset(a, b, sizeof(a))
#define Copy(a, b) memcpy(a, b, sizeof(b))
#define NPOS string::npos
#define For(i, a, b) for (int i = a; i <= b; i++)
#define Dor(i, a, b) for (int i = a; i >= b; i--)
#define Eor(j, a) for (Tedge *j = a; j; j = j -> next)
#define sqr(a) ((a) * (a))
using namespace std;
template<class T> inline void gmin(T &a, T b) { if (a > b) a = b; }
template<class T> inline void gmax(T &a, T b) { if (a < b) a = b; }
typedef long long ll;
typedef unsigned long long ull;
const int INF = 0x3f3f3f3f;
const ll LINF = 0x3f3f3f3f3f3f3f3fll;
const double DINF = 1e10;
const double EPS = 1e-8;
inline int dcmp(const double &a) { return a > EPS ? 1 : (a < -EPS ? -1 : 0); }

const int MAXN = 105;
const int MAXM = 105;

int n, m;
int rmax[MAXN], cmax[MAXM];
int a[MAXN][MAXM];

bool check() {
	For (i, 1, n) For (j, 1, m) if (min(rmax[i], cmax[j]) > a[i][j]) return false;
	return true;
}

int main() {
	freopen("b.in", "r", stdin);
	freopen("b.out", "w", stdout);
	int T;
	scanf("%d", &T);
	For (cas, 1, T) {
		scanf("%d %d", &n, &m);
		Fill(rmax, 0); Fill(cmax, 0);
		For (i, 1, n) For (j, 1, m) scanf("%d", &a[i][j]);
		For (i, 1, n) For (j, 1, m) gmax(rmax[i], a[i][j]), gmax(cmax[j], a[i][j]);
		if (check()) printf("Case #%d: YES\n", cas);
		else printf("Case #%d: NO\n", cas);
	}

	return 0;
}
