#include <bits/stdc++.h>
#define int long long
using namespace std;

const int MAXK = 111;
const int MAXC = 111;

int pos[MAXK][MAXC];

main() {
	freopen("D-small-attempt0.in", "r", stdin);
	freopen("output.txt", "w", stdout);
	int T;
	cin >> T;
	for (int _ = 1; _ <= T; _++) {
		int k, c, s;
		cin >> k >> c >> s;
		for (int i = 0; i < k; ++i)
			pos[i][1] = i;
		for (int j = 2; j <= c; ++j)
			for (int i = 0; i < k; ++i)
				pos[i][j] = k * pos[i][j - 1] + i;
		cout << "Case #" << _ << ": ";
		for (int i = 0; i < k; ++i)
			cout << pos[i][c] + 1 << ' ';
		cout << '\n';
	}
	return 0;
}

