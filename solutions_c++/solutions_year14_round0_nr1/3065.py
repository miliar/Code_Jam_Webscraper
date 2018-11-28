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
    int a1, a2;
    vector<vector<int> > v1(4), v2(4);
    cin >> a1;
    for (int i = 0; i < 4; ++i) {
        v1[i].resize(4);
        for (int j = 0; j < 4; ++j) {
            cin >> v1[i][j];
        }
    }

    cin >> a2;
    for (int i = 0; i < 4; ++i) {
        v2[i].resize(4);
        for (int j = 0; j < 4; ++j) {
            cin >> v2[i][j];
        }
    }

    --a1;
    --a2;

    set<int> s;
    for (int i = 0; i < 4; ++i) {
        s.insert(v1[a1][i]);
    }

    int found = 0;
    int ans;
    for (int i = 0; i < 4; ++i) {
        if (s.find(v2[a2][i]) != s.end()) {
            ++found;
            ans = v2[a2][i];
        }
    }

    if (found == 1) {
        cout << ans;
    } else if (found == 0) {
        cout << "Volunteer cheated!";
    } else {
        cout << "Bad magician!";
    }
    cout << endl;
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
