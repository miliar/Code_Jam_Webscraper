#include <iostream>
#include <fstream>
#include <set>
#include <map>
#include <string>
#include <vector>
#include <bitset>
#include <algorithm>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <cassert>
#include <queue>


typedef long long ll;
typedef long double ld;

using namespace std;

ld p[300];

ld run(vector<ld> a) {
	int n = a.size();
	for (int i = 0; i <= n; ++i)
		p[i] = 0;
	p[0] = 1;
	for (int i = 0; i < n; ++i) {
		for (int j = n; j > 0; --j) {
			p[j] = (1 - a[i]) * p[j] + a[i] * p[j - 1];
		}
		p[0] *= (1 - a[i]);
	}
	return p[n / 2];
}

ld a[300];
int n, k;


ld solve() {
	cin >> n >> k;
	for (int i = 0; i < n; ++i)
		cin >> a[i];
	sort(a, a + n);
	ld ans = 0;
	for (int i = 0; i <= n; ++i)
		for (int j = 0; j <= n; ++j) {
			if (i + j == k) {
				vector<ld> b;
				for (int i1 = 0; i1 < i; ++i1)
					b.push_back(a[i1]);
				for (int i1 = n - j; i1 < n; ++i1)
					b.push_back(a[i1]);
				ans = max(ans, run(b));
			}
		}
	return ans;
}


int main() {
	int tt;
	scanf("%d", &tt);
	cout.setf(ios::fixed);
	cout.precision(8);
	for (int i = 0; i < tt; ++i) {
		cout << "Case #" << i + 1 << ": " << solve() << "\n";
	}
	return 0;
}


