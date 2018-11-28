#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <cmath>
#include <sstream>

using namespace std;

typedef long long LL;
vector<LL> good;

bool check_pal(LL x) {
	stringstream str;
	str << x;
	string s = str.str();
	string r = s;
	reverse(r.begin(), r.end());
	return r == s;
}

bool check_sqr(LL x) {
	LL y = sqrt(0.0 + x) - 1;
	while (y * y <= x) {
		if (y * y == x) return true;
		++y;
	}
	return false;
}

void prep() {
	for (LL x = 1; x < 1 << 24; ++x) {
		if (check_pal(x)) {
			LL y = x * x;
			if (check_pal(y))
				good.push_back(y);
		}
	}

	for (size_t i = 0; i < good.size(); ++i)
		cerr << good[i] << ' ' << sqrt(0.0 + good[i]) << endl;
}

void solve() {
	LL A, B;
	cin >> A >> B;
	static int testid = 0;
	cout << "Case #" << ++ testid << ": ";
	cout << upper_bound(good.begin(), good.end(), B) - lower_bound(good.begin(), good.end(), A) << endl;
}

int main() {
	prep();
	int t;
	cin >> t;
	while (t--) solve();
	return 0;
}
