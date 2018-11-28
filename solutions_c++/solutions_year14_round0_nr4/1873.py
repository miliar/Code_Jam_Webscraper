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

int n;
double a[1005], b[1005];
int c[1005];

int main() 
{
	freopen("D-large.in", "r", stdin);
	freopen("D-large.out", "w", stdout);
	int tts, Tests;
	tts = 0;
	for (scanf("%d", &Tests); Tests--; ) {
		printf("Case #%d: ", ++tts);

		scanf("%d", &n);
		for (int i = 0; i < n; ++i) scanf("%lf", &a[i]);
		for (int j = 0; j < n; ++j) scanf("%lf", &b[j]);

		sort(a, a + n); sort(b, b + n);

		//puts("");
		//for (int i = 0; i < n; ++i) printf("%.3lf ", a[i]); puts("");
		//for (int i = 0; i < n; ++i) printf("%.3lf ", b[i]); puts("");


		int ans = 0;
		for (int i = 0, j = 0, k = n - 1; i < n; ++i) {
			if (a[i] > b[j]) {
				++ans;
				++j;
			} else --k;
		}
		printf("%d ", ans);
		ans = n;
		for (int i = 0, j = 0; i < n; ++i) {
			for (; j < n && b[j] < a[i]; ++j);
			if (j < n) {
				--ans;
				++j;
			} else break;
		}
		printf("%d\n", ans);
	}
	return 0;
}