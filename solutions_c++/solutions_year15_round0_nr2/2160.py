#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <vector>
#include <algorithm>
#include <set>
#include <map>
#include <cassert>
#include <ctime>
#include <numeric>

using namespace std;

#define sqr(a) ((a)*(a))
#define two(a) (1 << (a))
#define has(mask, a) ((mask) & two(a) ? 1 : 0)

int n, a[10005];

void load() {
	cin >> n;
	for (int i = 0;i < n;i++) {
		cin >> a[i];
	}
}

void solve(int test) {
	int ans = 1 << 30;                       
	for (int i = 1;i <= 1000;i++) {
		int cur = i;
		for (int j = 0;j < n;j++) {
			if (a[j] > i) {
				cur += (a[j] + i - 1) / i - 1;	
			}
		}
		ans = min(ans, cur);
	}

	printf ("Case #%d: %d\n", test, ans);
}

int main() {
 	freopen ("a.in", "r", stdin);

 	int t;
 	scanf ("%d\n", &t);

 	clock_t start = clock();
 	for (int i = 1;i <= t;i++) {
 		clock_t cur_start = clock();

 		fprintf(stderr, "Test %d:\n", i);
 		load();
 		solve(i);
 		fprintf(stderr, "Done in %.3f\n", (clock() - cur_start) / (double)CLOCKS_PER_SEC);
 	}

 	fprintf(stderr, "Total time: %.3f\n", (clock() - start) / (double)CLOCKS_PER_SEC);

 	return 0;
}