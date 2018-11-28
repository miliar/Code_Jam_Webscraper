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

void precalc () {

}

void solve () {
    int n, x;
    cin >> n >> x;

    vector<int> v(n);
    for (int i = 0; i < n; ++i) {
        cin >> v[i];
    }

    sort(v.rbegin(), v.rend());

    int res = 0;

    vector<bool> used(n, false);
    for (int i = 0; i < n; ++i) {
        if (!used[i]) {
            bool found = false;
            for (int j = i + 1; j < n; ++j) {
                if (!used[j] ) {
                    if (v[i] + v[j] <= x) {
                        res++;
                        used[i] = used[j] = true;
                        found = true;
                        break;
                    }
                }
            }
            if (!found) {
                used[i] = true;
                res++;
            }
        }
    }
    cout << res << endl;
}

int main() {
	freopen("A-large.in","r",stdin);
	freopen("output.txt","w",stdout);

    precalc();

	int T;
	cin >> T;
	for (int test = 1; test <= T; ++test) {
        cerr << test << endl;
		cout << "Case #" << test << ": ";
        solve();
	}
	return 0;
}
