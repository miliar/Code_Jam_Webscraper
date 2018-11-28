#include<bits/stdc++.h>
using namespace std;

inline void setSeen(int n, bool *seen, int &cntSeen) {
	if (!n) seen[0] = 1;
	while (n) {
		cntSeen += !seen[n % 10];
		seen[n % 10] = 1;
		n /= 10;
	}
}

inline int solve(int n) {
	int cntSeen = 0, curr = n;
	bool seen[10] = { 0 };
	while (cntSeen != 10) {
		setSeen(curr, seen, cntSeen);
		curr += n;
	}
	return curr - n;
}

int main() {
	ios_base::sync_with_stdio(0), cin.tie(0), cout.tie(0);
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);

	int t, n;
	cin >> t;
	for (int cs = 1; cs <= t; ++cs) {
		cin >> n;

		cout << "Case #" << cs << ": ";
		if (!n)
			cout << "INSOMNIA\n";
		else
			cout << solve(n) << '\n';

	}

	return 0;
}
