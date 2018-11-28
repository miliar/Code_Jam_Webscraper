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
int a[3005];

int main()
{
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);

	int Tests, tts = 0;
	for (scanf("%d", &Tests); Tests--; ) {
		scanf("%d", &n);
		int mx = 0, p;
		for (int i = 1; i <= n; ++i) 
			scanf("%d", &a[i]);

		int u = 1, v = n;
		int ans = 0;
		for (int i = 1; i <= n; ++i) {
			int mn = a[u], p = u;
			for (int j = u + 1; j <= v; ++j)
				if (a[j] < mn) {
					mn = a[j];
					p = j;
				}
			if (Abs(p - u) < Abs(p - v)) {
				ans += Abs(p - u);
				for (int j = p - 1; j >= u; --j)
					a[j + 1] = a[j];
				++u;
			} else {
				ans += Abs(p - v);
				for (int j = p; j < v; ++j)
					a[j] = a[j + 1];
				--v;
			}
		}
			

		printf("Case #%d: %d\n", ++tts, ans);
	}
	return 0;
}