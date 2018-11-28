#pragma comment(linker, "/STACK:16777216")
#include <iostream>
#include <cstdio>
#include <string>
#include <cstring>
#include <ctime>
#include <cstdlib>
#include <vector>
#include <map>
#include <set>
#include <algorithm>
#include <cmath>

#define INF 2000000000

#define forn(i, n) for(int i = 0; i < (int)n; ++i)

using namespace std;

typedef pair<int, int> ii;
typedef long long ll;

const int MAXN = 100100;
int a[MAXN];

void solve(int test) {
	int n, x;
	scanf("%d %d", &n, &x);
	forn(i, n) {
		scanf("%d", a + i);
	}
	sort(a, a + n);
	int res = 0, l = 0;
	for (int r = n - 1; r >= l; --r) {
		++res;
		if (a[r] + a[l] <= x) {
			++l;
		}
	}
	printf("%d\n", res);
}

int main(int argc, char **argv) {
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	int tt;
	scanf("%d\n", &tt);
	forn(i, tt) {
		printf("Case #%d: ", i + 1);
		solve(i + 1);
	}
	return 0;
}
