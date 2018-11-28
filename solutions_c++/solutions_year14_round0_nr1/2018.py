#include <algorithm>
#include <cmath>
#include <cstdio>
#include <ctime>
#include <iostream>
#include <map>
#include <set>
#include <string>
#include <vector>
using namespace std;


#define FOR(i, n) for(int i = 0; i < n; ++i)


void solve(int t, int fan, int san, int *far, int *sar) {
	int f = 0, s = 0, r = 0, a = 0;
	FOR(i, 4) {
		f |= 1 << far[(fan - 1) * 4 + i];
	}
	FOR(i, 4) {
		s |= 1 << sar[(san - 1) * 4 + i];
	}
	FOR(i, 17) {
		if ((f & s) & (1 << i)) {
			r += 1;
			a = i;
		}
	}
	cout << "CASE #" << t << ": ";
	if (!r) cout << "Volunteer cheated!" << endl;
	if (r == 1) cout << a << endl;
	if (r > 1) cout << "Bad magician!" << endl;
}


int main() {
    int t = 1, tn, fan, san, far[16], sar[16];
    cin >> tn;
    while (t <= tn) {
        cin >> fan;
        FOR(i, 16) cin >> far[i];
        cin >> san;
        FOR(i, 16) cin >> sar[i];
        solve(t++, fan, san, far, sar);
    }
    return 0;
}
