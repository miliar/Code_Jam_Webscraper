#include <algorithm>
#include <iostream>
#include <vector>
#include <cstdio>
#include <string>
#include <queue>
#include <stack>
#include <cmath>
#include <set>
#include <map>
#define ll long long
#define f first
#define s second
#define mp make_pair
#define pb push_back

using namespace std;

int T, n, id;
pair < int, int > a[1000];

void solve() {
	cin >> n;
	int s = 0;
	for (int i = 0; i < n; ++i)	{
		cin >> a[i].f;
		s += a[i].f;
		a[i].s = i;
	}

	cout << "Case #" << ++id << ": ";

	if (s % 2 != 0) {
		sort(a, a + n);
		char x = (char)(65 + a[n - 1].s);
		cout << x << ' ';
		a[n - 1].f--;
		s--;
	}

	while (s > 0) {
		sort(a, a + n);
		char x = (char)(65 + a[n - 1].s);
		char y = (char)(65 + a[n - 2].s);
		if (a[n - 1].f > a[n - 2].f + 1) {
			cout << x << x << ' ';
			a[n - 1].f -= 2;
			s -= 2;
		} else {
			cout << x << y << ' ';
			a[n - 1].f--;
			a[n - 2].f--;
			s -= 2;
		}
	}
	
	cout << endl;
}

int main() {
	#ifdef LOCAL
	freopen("in", "r", stdin);
	freopen("out", "w", stdout);
	#endif
	cin >> T;

	while (T--) {
		solve();
	}

	return 0;
}
                                

