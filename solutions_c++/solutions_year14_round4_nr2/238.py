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

int n, a[1005], b[1005];

void load() {
	cin >> n;
	for (int i = 0;i < n;i++) {
		cin >> a[i];
		b[i] = a[i];
	}
	sort (b, b + n);
}

void solve(int test) {
	int ans = 0;
	for (int i = 0;i < n;i++) {
		int pos = 0;
		for (;pos < n;pos++) {
			if (a[pos] == b[i]) break;
		}

		int l = 0, r = 0;
		for (int j = 0;j < pos;j++) {
			if (a[j] > a[pos]) l++;
		}
		for (int j = pos + 1;j < n;j++) {
			if (a[j] > a[pos]) r++;
		}
		ans += min (l, r);
	}
	
	printf ("Case #%d: %d\n", test, ans);
}

int main() {
 	freopen ("a.in", "r", stdin);

 	int t;
 	scanf ("%d\n", &t);

 	for (int i = 1;i <= t;i++) {
 		load();
 		solve(i);
 	}

 	return 0;
}