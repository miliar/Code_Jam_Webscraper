#include <bits/stdc++.h>

using namespace std;

const char LEFT = '<';
const char RIGHT = '>';
const char DOWN = 'v';
const char UP = '^';
const char EMPTY = '.';

void solve(int T)
{
    int n, m;
    vector< string > p;
    cin >> n >> m;
    p.resize(n);
    for (int i = 0; i < n; i++) {
	cin >> p[i];
    }

    vector<vector<set<char> > > canNotBe;
    canNotBe.assign(n, vector<set<char> >(m));

    for (int i = 0; i < n; i++) {
	for (int j = 0; j < m; j++) {
	    canNotBe[i][j].insert(LEFT);
	    if (p[i][j] != EMPTY) {
		break;
	    }
	}

	for (int j = m-1; j >= 0; j--) {
	    canNotBe[i][j].insert(RIGHT);
	    if (p[i][j] != EMPTY) {
		break;
	    }
	}
    }

    for (int i = 0; i < m; i++) {
	for (int j = 0; j < n; j++) {
	    canNotBe[j][i].insert(UP);
	    if (p[j][i] != EMPTY) {
		break;
	    }
	}

	for (int j = n - 1; j >= 0; j--) {
	    canNotBe[j][i].insert(DOWN);
	    if (p[j][i] != EMPTY) {
		break;
	    }
	}
    }

    cout << "Case #" << T + 1 << ": ";
    int ans = 0;
    for (int i = 0; i < n; i++) {
	for (int j = 0; j < m; j++) {
	    if (canNotBe[i][j].size() == 4 && p[i][j] != EMPTY) {
		cout << "IMPOSSIBLE\n";
		return;
	    }

	    if (canNotBe[i][j].count(p[i][j])) {
		ans++;
	    }
	}
    }

    cout << ans << "\n";
}

int main()
{
    ios_base::sync_with_stdio(false);
    int Q;
    cin >> Q;
    for (int T = 0; T < Q; T++) {
	solve(T);
    }
}
