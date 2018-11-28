#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cstdlib>
#include <vector>
#include <map>
#include <set>
#include <cstring>

#define forn(i, n) for (int i = 0; i < (int)n; ++i)

using namespace std;

void solve()
{
	int n;
	cin >> n;
	vector<double> a(n);
	vector<double> b(n);
	forn(i, n) {
		cin >> a[i];
	}
	forn(i, n) {
		cin >> b[i];
	}
	sort(a.begin(), a.end());
	sort(b.begin(), b.end());
	int ans1 = 0;
	int ans2 = 0;
	int right1 = 0, right2 = b.size() - 1;
	for (int i = a.size() - 1; i >= 0; --i) {
		if (a[i] > b[right2]) {
			++right1;
			++ans2;
		} else {
			--right2;
		}
	}
	int right = 0;
	for (int i = 0; i < (int)a.size();) {
		while (i < (int)a.size() && a[i] < b[right]) {
			++i;
		}
		if (i < (int)a.size()) {
			++i;
			++ans1;
			++right;
		}
	}
	cout << ans1 << ' ' << ans2 << endl;
}


int main()
{
	freopen("D-large.in", "r", stdin);
	freopen("D-large.out", "w", stdout);
	int tt;
	scanf("%d", &tt);
	forn(t, tt)
	{
		cout << "Case #" << (t + 1) << ": ";
		solve();
	}
	return 0;
}
