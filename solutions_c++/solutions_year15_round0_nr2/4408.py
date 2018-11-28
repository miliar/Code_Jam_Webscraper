#include <set>
#include <map>
#include <cmath>
#include <vector>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <algorithm>
using namespace std;

#define pb push_back
#define mp make_pair
#define sz(a) (int)a.size()
#define ms(a, x) memset(a, x, sizeof a)
#define all(a) a.begin(), a.end()
#define forit(i, s) for (__typeof(s.begin()) i = s.begin(); i != s.end(); i++)

typedef long long ll;
typedef pair<int,int> pt;

const int N = 1<<10;
const int inf = 1<<30;

int a[N];

int main() {
	freopen("b.in", "r", stdin);
	freopen("b.out", "w", stdout);

	int tests;
	scanf("%d\n", &tests);
	for (int t = 1; t <= tests; t++) {
		int n;
		scanf("%d", &n);
		for (int i = 0; i < n; i++)
			scanf("%d", a + i);
		int ans = inf;
		for (int x = 1; x <= 1000; x++) {
			int cur = 0;
			for (int i = 0; i < n; i++)
				cur += (a[i]-1) / x;
			ans = min(ans, cur + x);
		}
		printf("Case #%d: %d\n", t, ans);
	}

	return 0;
}