#include <iostream>
#include <iomanip>
#include <algorithm>
#include <cstdio>
#include <complex>
#include <sstream>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <cmath>
#include <cstring>

using namespace std;

typedef long double ld;
typedef long long ll;
typedef pair<ll, ll> pii;
typedef complex<ld> pt;

int grid1[5][5], grid2[5][5];
int main() {
	int t; cin >> t;
	for (int ca = 1; ca <= t; ca++) {
		int r1, r2;
		cin >> r1;
		for (int i = 0; i < 4; i++) {
			for (int j = 0; j < 4; j++) {
				int x;
				cin >> x;
				grid1[i][j] = (1<<x);
			}
		}
		
		cin >> r2;
		for (int i = 0; i < 4; i++) {
			for (int j = 0; j < 4; j++) {
				int x; cin >> x;
				grid2[i][j] = (1<<x);
			}
		}
		
		r1--, r2--;
		int c1 = 0, c2 = 0;
		for (int j = 0; j < 4; j++) {
			c1 |= grid1[r1][j];
			c2 |= grid2[r2][j];
		}
		
		int ans = c1&c2;
		int cnt = __builtin_popcount(ans);
		cout << "Case #" << ca << ": ";
		if (cnt > 1) {
			cout << "Bad magician!" << endl;
		} else if (cnt == 0) {
			cout << "Volunteer cheated!" << endl;
		} else {
			for (int i = 0; i < 20; i++) {
				if (ans & (1<<i)) {
					cout << i << endl;
					break;
				}
			}
		}
	}
	return 0;
}