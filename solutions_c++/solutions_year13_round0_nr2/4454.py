#include <algorithm>
#include <bitset>
#include <cassert>
#include <cctype>
#include <cmath>
#include <complex>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <deque>
#include <fstream>
#include <functional>
#include <iomanip>
#include <iostream>
#include <list>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <utility>
#include <vector>

#define Abs(x) ((x) >= 0 ? (x) : -(x))
#define Max(a, b) ((a) >= (b) ? (a) : (b))
#define Min(a, b) ((a) <= (b) ? (a) : (b))
#define Size(t) (int(t.size()))
#define Sqr(x) ((x) * (x))

using namespace std;

typedef long long LL;
typedef unsigned int UI;
typedef unsigned long long ULL;
typedef pair <int, int> PII;
typedef set <int> SI;
typedef set <LL> SLL;
typedef vector <int> VI;
typedef vector <double> VD;
typedef vector <VD> VVD;
typedef vector <VI> VVI;

const double ep = 1e-8;
const double pi = 3.141592654;
const int inf = 0x7fffffff;
const long long llinf = 0x7fffffffffffffffLL;

/*Template written by Mashimaru*/

int test;
int m, n, row[105], col[105], a[105][105];

int main()
{
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);
	scanf("%d", &test);
	for (int numCase = 1; numCase <= test; numCase++) {
		scanf("%d %d", &m, &n);
		for (int i = 1; i <= m; i++)
			for (int j = 1; j <= n; j++)
				scanf("%d", &a[i][j]);
		for (int i = 1; i <= m; i++) {
			row[i] = -inf;
			for (int j = 1; j <= n; j++)
				row[i] = Max(row[i], a[i][j]);
		}
		for (int j = 1; j <= n; j++) {
			col[j] = -inf;
			for (int i = 1; i <= m; i++)
				col[j] = Max(col[j], a[i][j]);
		}
		bool ok = true;
		for (int i = 1; i <= m; i++)
			for (int j = 1; j <= n; j++)
				if (a[i][j] < row[i] && a[i][j] < col[j]) {
					ok = false;
					break;
				}
		printf("Case #%d: %s\n", numCase, ok ? "YES" : "NO");
	}
	return 0;
}