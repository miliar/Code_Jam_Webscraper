#include      <algorithm>
#include      <cmath>
#include      <cstdarg>
#include      <cstdio>
#include      <cstdlib>
#include      <iomanip>
#include      <iostream>
#include      <iterator>
#include      <limits>
#include      <list>
#include      <map>
#include      <set>
#include      <queue>
#include      <vector>
#define endl '\n'
#define each(c, e) for (typeof(c.begin()) e = c.begin(); e != c.end(); ++e)
using namespace std;
typedef long long ll;
typedef long double ld;
typedef pair<int, int> pii;

int sizes[100000];

void solve() {
	int nDisks, nCapacity;
	cin >> nDisks >> nCapacity;
	for (int i = 0; i < nDisks; i += 1) cin >> sizes[i];
	sort(sizes, sizes + nDisks);
	for (int i = 0; i < nDisks; i += 1) if (sizes[i] > nCapacity) sizes[i] = -1;
	int r = 0;

	for (int c = nDisks - 1; c >= 0; c -= 1) if (sizes[c] != -1) {
		for (int o = c - 1; o >= 0; o -= 1) if (sizes[o] != -1) {
			if (sizes[c] + sizes[o] <= nCapacity) {
				sizes[c] = sizes[o] = -1;
				r += 1;
				break;
			}
		}
	}

	pair<int, int> have = make_pair(0, 0);
	for (int c = 0; c < nDisks; c += 1) if (sizes[c] != -1) {
		have.first += 1;
		have.second += sizes[c];
		if (have.second > nCapacity) {
			have = make_pair(1, sizes[c]);
			r += 1;
		}
		if (have.first == 2) {
			have = make_pair(0, 0);
			r += 1;
		}
	}
	r += have.first != 0;

	cout << r << endl;
}

int main(int argc, char **argv) {
	ios_base::sync_with_stdio(false), cin.tie(0);
	int T;
	cin >> T;
	for (int t = 1; t <= T; t += 1) {
		cout << "Case #" << t << ": ";
		solve();
	}
	
	return 0;
}
