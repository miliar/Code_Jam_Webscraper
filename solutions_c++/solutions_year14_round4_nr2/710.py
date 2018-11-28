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

int buble(vector<int>& v, int n) {
    int res = 0;

    for (int i = n; i > 0; --i) {
        if (v[i] < v[i - 1]) {
            ++res;
            swap(v[i], v[i - 1]);
        }
    }
    return res;
}

vector<int> fun(vector<int> v) {
    int n = v.size();

    vector<int> res(n, 0);
    for (int i = 1; i < n; ++i) {
        res[i] = buble(v, i) + res[i - 1];
    }
    return res;
}

void solve1 () {
    int n;
    cin >> n;

    vector<int> v(n);
    for (int i = 0; i < n; ++i) {
        cin >> v[i];
    }

    vector<int> l = fun(v);

    reverse(v.begin(), v.end());
    vector<int> r = fun(v);

    int res = min(l[n - 1], r[n - 1]);
    for (int i = 0; i < n - 1; ++i) {
        res = min(res, l[i] + r[n - 2 - i]);
    }
    cout << res << endl;
}

void solve () {
    int n;
    cin >> n;

    vector<int> v(n);
    for (int i = 0; i < n; ++i) {
        cin >> v[i];
    }

    int res = 0;
    while (!v.empty()) {
        int x = 1e9 + 1e8;
        int pos = -1;
        for (int i = 0; i < v.size(); ++i) {
            if (v[i] < x || pos == -1) {
                x = v[i];
                pos = i;
            }
        }
        res += min(pos, (int)v.size() - 1 - pos);
        v.erase(v.begin() + pos);
    }
    cout << res << endl;
}

int main() {
	freopen("B-large.in","r",stdin);
	freopen("output.txt","w",stdout);

    precalc();

	int T;
	cin >> T;
	for (int test = 1; test <= T; ++test) {
		cout << "Case #" << test << ": ";
        //solve1();
        cerr << test << endl;
        solve();
	}
	return 0;
}
