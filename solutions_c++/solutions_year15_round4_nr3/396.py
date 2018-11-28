#include <iostream>
#include <cstdio>
#include <memory.h>
#include <vector>
#include <string>
#include <map>
#include <sstream>

using namespace std;

#define NAME "c"

vector<string> split(string s) {
    stringstream str(s);
    vector<string> ans;
    string t;
    while (str >> t) {
        ans.push_back(t);
    }
    return ans;
}


void solve() {
	int res = 1 << 30;
    int n;
    cin >> n;

    vector<string> f(n);
    getline(cin, f[0]);
    for (int i = 0; i < n; ++i) {
        getline(cin, f[i]);
    }

    map<string, int> w2i;
    vector< vector<int> > v;

    for (int i = 0; i < n; ++i) {
        vector<string> vs = split(f[i]);
        vector<int> id;
        for (int j = 0; j < vs.size(); ++j) {
            string w = vs[j];
            if (w2i.count(w) == 0) {
                int ps = w2i.size();
                w2i[w] = ps;
            }
            id.push_back(w2i[w]);
        }

        v.push_back(id);
    }

    vector<int> ms(w2i.size());
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < v[i].size(); ++j)
            ms[v[i][j]] |= 1 << i;
    }

    for (int m = 0; m < (1 << (n - 2)); ++m) {
        int cur = 0;

        int m2 = (1 << (n - 2)) - 1 - m;

        for (int i = 0; i < ms.size(); ++i) {
            bool en = ms[i] & 1;
            en |= (m & (ms[i] >> 2)) > 0;

            bool fr = ms[i] & 2;
            fr |= (m2 & (ms[i] >> 2)) > 0;

            cur += en && fr;
        }


        res = min(res, cur);
    }

	static int test;
	cout << "Case #" << ++test << ": " << res << endl;
	cerr << "Case #" << test << ": " << res << endl;
}

int main() {
    freopen(NAME".in", "r", stdin);
    freopen(NAME".out", "w", stdout);

	int t;
	cin >> t;
	while (t --> 0)
		solve();
	return 0;
}
