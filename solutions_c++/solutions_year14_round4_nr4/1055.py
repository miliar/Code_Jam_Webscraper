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

map <int, int> aa;
vector <string > s;
vector <int> ass;
int nn, cc, n, m;

void gen(int ind) {
    if (ind == m) {
        vector <int> cnt1(n, 0);
        for (int i = 0; i < m; ++i) {
            cnt1[ass[i]]++;
        }
        for (int i = 0; i < n; ++i) {
            if (cnt1[i] == 0) return;
        }

        vector<set<string > > pref(n);
        for (int i = 0; i < m; ++i) {
            for (int j = 0; j <= (int)s[i].size(); ++j) {
                pref[ass[i]].insert(s[i].substr(0, j));
            };
        }
        int nnn = 0;
        for (int i = 0; i < n; ++i) {
            nnn += pref[i].size();
        }
        aa[nnn] = (aa[nnn] + 1) % 1000000007;
        nn = max(nn, nnn);
    } else {
        for (int i = 0; i < n; ++i) {
            ass[ind] = i;
            gen(ind + 1);
        }
    }
}

void solve() {
    aa.clear();
    s.clear();
    string str;
    cin >> m >> n;
    for (int i = 0; i < m; ++i) {
        cin >> str;
		while (str.size() == 0) {
			cin >> str;
		}
        s.push_back(str);
    }

    nn = 0;
    cc = 0;
    ass = vector <int> (m, -1);
    gen(0);

    cout << nn << ' ' << aa[nn];
}

int main() {

	freopen("D-small-attempt0.in", "r", stdin);
	freopen("D-small-attempt0.out", "w", stdout);
//	freopen("A-small-attempt0.log", "w", stderr);

	int T;
	cin >> T;
	for (int t = 1; t <= T; ++t) {

		cout << "Case #" << t << ": ";
		solve();
		cout << endl;
	}

	return 0;
}
