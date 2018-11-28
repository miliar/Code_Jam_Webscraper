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

void load() {
}

void solve(int test) {
	int n;
	string s;
	cin >> n >> s;
	int ans = 0, cur = 0;

	for (int i = 0;i <= n;i++) {
		int c = s[i] - '0';
		if (c > 0 && cur < i) {
			ans += i - cur;
			cur = i;
		}
		cur += c;
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