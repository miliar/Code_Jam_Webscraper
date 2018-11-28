#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <set>
 
using namespace std;
 
#define For(i,l,r) for (i = l; i <= r; i++)
#define FOR(i, n) for (int i = 0; i < n; i++)
#define for1(i,n) for (int i = 1; i <= n; i++)

int test_count;
long double c, f, x, ans, p, v, t;

long double min(long double a, long double b) {
	return a < b ? a : b;
}

void init() {
	cin >> c >> f >> x;
}

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	cin >> test_count;

	for1(tt, test_count) {
		int i = 0;
		init();
		v = 2.0;
		ans = x/v;
		t = 0;
		/*
		FOR(i, 10000) {
			t += c/v;
			v += f;
			ans = min(ans, t + x/v);
		}*/
		while (t < ans) {
			t += c/v;
			v += f;
			ans = min(ans, t + x/v);
		}

		//cout << "Case #" << tt << ": " << ans << endl;
		printf("Case #%d: %1.8f\n", tt, ans);
	}


	//system("PAUSE");
	return 0;
}