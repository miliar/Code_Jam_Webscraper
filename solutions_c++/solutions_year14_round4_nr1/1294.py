#include "cmath"
#include "cstdio"
#include "algorithm"
#include "map"
#include "numeric"
#include "queue"
#include "set"
#include "string"
#include "utility"
#include "vector"
#include "iostream"
#include "iomanip"

using namespace std;

int d[10100];

int solve() {
    int ans = 0;
    int n, x;
    cin >> n >> x;
    for (int i = 0; i < n; ++i) {
        cin >> d[i];
    }
    sort(d, d + n);
    for (int i = 0, j = n; i < j; ++ans) {
        if (i == j-1) {
            ++i;
        } else
        if (d[i] + d[j-1] > x) {
            --j;
        } else {
            ++i;
            --j;
        }
    }
    return ans;
}

int main() {

	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
//	freopen("A-small-attempt0.log", "w", stderr);

	int T;
	cin >> T;
	for (int t = 1; t <= T; ++t) {

		int ans = solve();
		cout << "Case #" << t << ": " << ans;
		cout << endl;
	}

	return 0;
}
