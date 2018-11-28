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

ld r[200];
ld t[200];

vector<pair<ld, ld> > vv1;
vector<pair<ld, ld> > vv2;

const ld eps = 1e-9;




ld solve() {
	int n;
	ld v, x;
	cin >> n >> v >> x;
	int fl1 = 0;
	int fl2 = 0;
	ld r0 = 0;
	ld rtl = 0;
	ld rtr = 0;
	vv1.clear();
	vv2.clear();
	for (int i = 0; i < n; ++i) {
		cin >> r[i] >> t[i], t[i] -= x;
		if (abs(t[i]) < eps)
			fl1 = fl2 = 1, r0 += r[i];
		else if (t[i] < 0) {
			fl1 = 1;
			rtl -= r[i] * t[i];
			vv1.push_back(make_pair(-t[i], r[i]));
		}
		else if (t[i] > 0) {
			fl2 = 1;
			rtr += r[i] * t[i];
			vv2.push_back(make_pair(t[i], r[i]));
		}
	}
	if (!fl1 || !fl2)
		return -1;
	ld mn = min(rtl, rtr);
	sort(vv1.begin(), vv1.end());
	sort(vv2.begin(), vv2.end());
	ld now = 0;
	for (int i = 0; i < (int)vv1.size(); ++i) {
		if (now + vv1[i].first * vv1[i].second <= mn)
			now += vv1[i].first * vv1[i].second, r0 += vv1[i].second;
		else if (abs(now - mn) < eps)
			break;
		else {
			r0 += (mn - now) / vv1[i].first;
			break;
		}
	}
	now = 0;
	for (int i = 0; i < (int)vv2.size(); ++i) {
		if (now + vv2[i].first * vv2[i].second <= mn)
			now += vv2[i].first * vv2[i].second, r0 += vv2[i].second;
		else if (abs(now - mn) < eps)
			break;
		else {
			r0 += (mn - now) / vv2[i].first;
			break;
		}
	}
	return v / r0;
}


int main() {
	int tt;
	scanf("%d", &tt);
	cout.setf(ios::fixed);
	cout.precision(10);
	for (int i = 0; i < tt; ++i) {
		ld ans = solve();
		if (ans >= 0)
			cout << "Case #" << i + 1 << ": " << ans << "\n";
		else
			cout << "Case #" << i + 1 << ": " << "IMPOSSIBLE" << "\n";
	}
	return 0;
}


