#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <algorithm>
#include <cmath>
#include <string>
#include <sstream>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <ctime>

#define inf 0x3f3f3f3f
#define Inf 0x3FFFFFFFFFFFFFFFLL
#define rep(i, n) for (int i = 0; i < (n); ++i)
#define Rep(i, n) for (int i = 1; i <= (n); ++i)
#define clr(x, a) memset(x, (a), sizeof x)
using namespace std;
typedef long long ll;
int const N = 10010;
int a[N];
int main() {
#if 1
	//freopen("A-small-attempt1.in", "r", stdin);
	freopen("A-large.in", "r", stdin);
	freopen("A-large-ans.txt", "w", stdout);
#endif
	int T, ca = 1;
	int n, m;
	for (scanf("%d", &T); T--; ) {
		scanf("%d%d", &n, &m);
		rep(i, n) scanf("%d", &a[i]);
		sort(a, a + n);
		int top = n - 1, ret = 0;
		if (n == 1) {
			ret = 1;printf("Case #%d: %d\n", ca++, ret);
			continue;
		}
		rep(i, n) {
			if (a[i] == -1) {
				for (int j = i; j < n; ++j) ret += a[j] != -1;
				break;
			}
			++ret;
			while (top > i && a[i] + a[top] > m) --top;
			if (top >= i) a[top--] = -1;
		}
		printf("Case #%d: %d\n", ca++, ret);
	}
	return 0;
}

