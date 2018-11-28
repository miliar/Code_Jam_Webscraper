#include <iostream>
#include <cstdio>
#include <memory.h>
#include <vector>
#include <string>
#include <set>

using namespace std;

#define NAME "a"

char s[128][128];

void solve() {
	int res = 0;

    int n, m;
    cin >> n >> m;
    for (int i = 0; i < n; ++i) cin >> s[i];

    for (int i = 0; i < n && res >= 0; ++i) {
        for (int j = 0; j < m && res >= 0; ++j) {
            if (s[i][j] == '.') continue;

            bool up = false; for (int ii = 0; ii < i; ++ii) if (s[ii][j] != '.') up = true;
            bool dw = false; for (int ii = i + 1; ii < n; ++ii) if (s[ii][j] != '.') dw = true;
            bool lf = false; for (int jj = 0; jj < j; ++ jj) if (s[i][jj] != '.') lf = true;
            bool rg = false; for (int jj = j + 1; jj < m; ++jj) if (s[i][jj] != '.') rg = true;

            if (!up && !dw && !lf && !rg) res = -1;
            else {
                if (s[i][j] == '^' && !up) res++;
                if (s[i][j] == 'v' && !dw) res++;
                if (s[i][j] == '<' && !lf) res++;
                if (s[i][j] == '>' && !rg) res++;
            }
        }
    }

	static int test;
	if (res >= 0)
        cout << "Case #" << ++test << ": " << res << endl;
	else
        cout << "Case #" << ++test << ": " << "IMPOSSIBLE" << endl;

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
