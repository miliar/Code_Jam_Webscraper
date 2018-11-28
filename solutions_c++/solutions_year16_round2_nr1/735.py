/*
reality, be rent!
synapse, break!
Van!shment Th!s World !!
*/
#include <bits/stdc++.h>
using namespace std;

const int MN = 2020;

char s[MN];

int main() {
	freopen("A-large.in", "r", stdin);
	freopen("output.txt", "w", stdout);
	int T, K = 1;
	scanf("%d", &T);
	string digit[] = {"ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"};
	while (T--) {
		string ans = "";
		int n, i;
		map<char, int> f;

		scanf("%s", s);
		n = strlen(s);

		for (i = 0; i < n; ++i) ++f[s[i]];

		while (f['Z']) {
			ans += '0';
			for (auto &c : digit[0]) --f[c];
		}

		while (f['X']) {
			ans += '6';
			for (auto &c : digit[6]) --f[c];
		}

		while (f['G']) {
			ans += '8';
			for (auto &c : digit[8]) --f[c];
		}

		while (f['H']) {
			ans += '3';
			for (auto &c : digit[3]) --f[c];
		}

		while (f['W']) {
			ans += '2';
			for (auto &c : digit[2]) --f[c];
		}

		while (f['R']) {
			ans += '4';
			for (auto &c : digit[4]) --f[c];
		}


		while (f['O']) {
			ans += '1';
			for (auto &c : digit[1]) --f[c];
		}

		while (f['F']) {
			ans += '5';
			for (auto &c : digit[5]) --f[c];
		}

		while (f['S']) {
			ans += '7';
			for (auto &c : digit[7]) --f[c];
		}


		while (f['E']) {
			ans += '9';
			for (auto &c : digit[9]) --f[c];
		}


		sort(ans.begin(), ans.end());
		printf("Case #%d: %s\n", K, ans.c_str());
		++K;
	}
	return 0;
}
