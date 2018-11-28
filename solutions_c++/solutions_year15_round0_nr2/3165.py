#include <iostream>
#include <cstdio>
#include <cstdlib>

using namespace std;

int n;
int d[10000];

int f(int m) {
	int ans = m;
	for (int i = 0; i < n; i++) {
		ans += (d[i] + m - 1) / m - 1;
	}
	return ans;
}

int search(int ll, int rr) {

	int ans = f(ll);
	for (int i = ll; i <= rr; i++) {
		if (f(i) < ans)
			ans = f(i);
//		cerr << "\t" << f(i) << endl;
	}
	
/*
	int l = ll;
	int r = rr;
	while (l + 2 < r) {
		int m1 = l + (r - l) / 3;
		int m2 = l + (r - l) * 2 / 3;
		if (f(m1) < f(m2))
			r = m2;
		else if (f(m1) > f(m2))
			l = m1;
		else {
			l = m1;
			r = m2;
		}
	}

	int m1 = l + (r - l) / 3;
	int m2 = l + (r - l) * 2 / 3;
	int ans = f(r);
	ans = f(l) < ans ? f(l) : ans;
	ans = f(m1) < ans ? f(m1) : ans;
	ans = f(m2) < ans ? f(m2) : ans;
*/

	return ans;
}

int main() {
	ios::sync_with_stdio(false);

	int test_num;
	cin >> test_num;
	for (int itest = 0; itest < test_num; itest++) {
		cin >> n;
		int l = 1;
		int r = 1;
		for (int i = 0; i < n; i++) {
			cin >> d[i];
			if (d[i] > r)
				r = d[i];
		}

		int ans = search(l, r);
//		cerr << l << "(" << f(l) << ") -- " << r << "(" << f(r) << ")" << endl;

		cout << "Case #" << itest + 1 << ": " <<  ans << endl;
	}

	return 0;
}
