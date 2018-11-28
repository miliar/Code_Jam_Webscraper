#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
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
#include <cctype>
#include <string>
#include <cstring>
#include <ctime>
#include <string.h>

using namespace std;

const double pi = acos(-1.0);
const double eps = 1E-7;

typedef long long int64;
typedef unsigned long long uint64;
#define two(X) (1<<(X))
#define twoL(X) (((int64)(1))<<(X))
#define contain(S,X) (((S)&two(X))!=0)
#define containL(S,X) (((S)&twoL(X))!=0)
#define sqr(x) ((x)*(x))
#define Abs(x) ((x) < 0 ? (-(x)) : (x))
typedef pair<int,int> ipair;
#define SIZE(A) ((int)A.size())
#define MP(A,B) make_pair(A,B)
#define PB(X) push_back(X)
#define ME(a) memset((a), 0, sizeof((a)))
#define MM(a, b) memcpy((a), (b), sizeof((a)))
#define FOR(i,n) for (int (i) = 0; (i) < (n); ++(i))
#define REP(i,a,b) for (int (i) = (a); (i) < (b); ++(i))

int P, Q, n;
struct TPoint {
	int x, y;
} a[10005][10];
int d[3005][3005];
int f[10005];
int us[10005];

int main()
{
	freopen("C-large.in", "r", stdin);
	freopen("C-large.out", "w", stdout);

	int Tests, tts = 0;
	for (scanf("%d", &Tests); Tests--; ) {
		scanf("%d%d%d", &P, &Q, &n);
		--P;
		ME(d);
		for (int i = 1; i <= n; ++i) {
			scanf("%d%d%d%d", &a[i][1].x, &a[i][1].y, &a[i][2].x, &a[i][2].y);
			a[i][3].x = a[i][1].x;
			a[i][3].y = a[i][2].y;
			a[i][4].x = a[i][2].x;
			a[i][4].y = a[i][1].y;
			d[i][n + 1] = d[n + 1][i] = a[i][1].x;
			d[i][n + 2] = d[n + 2][i] = P - a[i][2].x;
		}
		d[n + 1][n + 2] = d[n + 2][n + 1] = P + 1;

		for (int i = 1; i <= n; ++i)
			for (int j = i + 1; j <= n; ++j) {
				d[i][j] = 1000000000;
				for (int x = 1; x <= 4; ++x)
					for (int y = 1; y <= 4; ++y) {
						int dis = max(Abs(a[i][x].x - a[j][y].x), Abs(a[i][x].y - a[j][y].y)) - 1;
						d[i][j] = min(d[i][j], dis);
					}
				if ((a[i][1].x < a[j][1].x && a[i][2].x > a[j][1].x) 
				||  (a[i][1].x < a[j][2].x && a[i][2].x > a[j][2].x)
				||  (a[j][1].x < a[i][1].x && a[j][2].x > a[i][1].x)
				||  (a[j][1].x < a[i][2].x && a[j][2].x > a[i][2].x)) {
					d[i][j] = min(Abs(a[i][1].y - a[j][2].y), Abs(a[i][2].y - a[j][1].y)) - 1;
				}
				if ((a[i][1].y < a[j][1].y && a[i][2].y > a[j][1].y) 
				||  (a[i][1].y < a[j][2].y && a[i][2].y > a[j][2].y)
				||  (a[j][1].y < a[i][1].y && a[j][2].y > a[i][1].y)
				||  (a[j][1].y < a[i][2].y && a[j][2].y > a[i][2].y)) {
					d[i][j] = min(Abs(a[i][1].x - a[j][2].x), Abs(a[i][2].x - a[j][1].x)) - 1;
				}
				d[j][i] = d[i][j];
			}

		//for (int i = 1; i <= n + 2; ++i, puts(""))
		//	for (int j = 1; j <= n + 2; ++j)
		//		printf("%d ", d[i][j]);

		ME(us);
		for (int i = 1; i <= n + 2; ++i) f[i] = d[n + 1][i];
		us[n + 1] = 1;
		for (int i = 1; i < n + 2; ++i) {
			int mn = 1000000000;
			int k;
			for (int j = 1; j <= n + 2; ++j)
				if (!us[j] && f[j] < mn) {
					mn = f[j];
					k = j;
				}
			us[k] = 1;
			for (int j = 1; j <= n + 2; ++j)
				if (!us[j] && f[j] > f[k] + d[k][j]) {
					f[j] = f[k] + d[k][j];
				}
		}

		printf("Case #%d: %d\n", ++tts, f[n + 2]);
	}

	return 0;
}