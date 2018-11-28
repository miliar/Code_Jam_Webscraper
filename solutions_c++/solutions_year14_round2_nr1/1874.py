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
    int n;
    cin >> n;

    vector< vector< pair<char, int> > > v(n);
    for (int i = 0; i < n; ++i) {
        string s;
        cin >> s;

        char last = 0;
        for (int j = 0; j < s.size(); ++j) {
            if (s[j] != last) {
                last = s[j];
                v[i].push_back(make_pair(s[j], 1));
            } else {
                v[i].rbegin()->second++;
            }
        }
    }

    int m = v[0].size();
    for (int i = 0; i < n; ++i) {
        if (v[i].size() != m) {
            cout << "Fegla Won" << endl;
            return;
        }
        for (int j = 0; j < m; ++j) {
            if (v[i][j].first != v[0][j].first) {
                cout << "Fegla Won" << endl;
                return;
            }
        }
    }

    int ans = 0;
    for (int i = 0; i < m; ++i) {
        int sum = 0;
        for (int j = 0; j < n; ++j) {
            sum += v[j][i].second;
        }
        int mid = sum / n;

        int res = 1e9;

        int cur = 0;
        for (int j = 0; j < n; ++j) {
            cur += abs(v[j][i].second - mid);
        }
        res = min(res, cur);

        cur = 0;
        for (int j = 0; j < n; ++j) {
            cur += abs(v[j][i].second - mid - 1);
        }
        res = min(res, cur);

        ans += res;
    }
    cout << ans << endl;
}

int main() {
	freopen("A-small-attempt0.in","r",stdin);
	freopen("output.txt","w",stdout);

  precalc();

	int T;
	cin >> T;
	for (int test = 1; test <= T; ++test) {
		cout << "Case #" << test << ": ";
    
    solve();
	}
	return 0;
}
