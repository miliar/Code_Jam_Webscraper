#include <bits/stdc++.h>

using namespace std;

const int MAXN = 1010;

int t, n, a[MAXN], ps[MAXN];

int main() {
	ifstream fin("test.in");
	ofstream fout("test.out");

	fin >> t;
	for (int i = 0; i < t; i++) {
		fin >> n; n++;
		string s; fin >> s;
		for (int j = 0; j < n; j++) {
			a[j] = s[j] - '0';
		}

		fill(ps, ps + n, 0);
		int ans = 0;

		ps[0] = a[0];
		if (ps[0] == 0) {
			ps[0]++;
			ans++;
		}
		for (int j = 1; j < n; j++) {
			if (ps[j - 1] < j) {
				int inv = j - ps[j - 1];
				ps[j - 1] += inv;
				ans += inv;
			} 
			ps[j] = a[j] + ps[j - 1];
		}

		fout << "Case #" << i + 1 << ": " << ans << '\n';
	}


	fin.close();
	fout.close();
	return 0;
}