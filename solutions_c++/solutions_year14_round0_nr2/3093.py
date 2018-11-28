#include <iostream>
#include <string>
#include <algorithm>
#include <cmath>
#include <set>
#include <map>
#include <vector>
#include <bitset>
#include <cstdio>
#include <queue>

using namespace std;

double c, f, x;
vector<double> sm(500005);

void precalc () {
    for (int i = 1; i < sm.size(); ++i) {
        sm[i] = sm[i - 1] + 1.0 / (2.0 + (i - 1) * f);
    }
}

void solve () {
    cin >> c >> f >> x;

    precalc();

    double ans = 1e18;
    for (int i = 0; i <= 500000; ++i) {
        double t = c * sm[i];
        double g = 2.0 + f * i;
        if (t + x / g < ans) {
            ans = min(ans, t + x / g);
        }
    }

    printf("%.9lf\n", ans);
}

int main() {
	freopen("B-large.in","r",stdin);
	freopen("output.txt","w",stdout);

	int T;
	cin >> T;
	for (int test = 1; test <= T; ++test) {
		cout << "Case #" << test << ": ";
    
    solve();
	}
	return 0;
}
