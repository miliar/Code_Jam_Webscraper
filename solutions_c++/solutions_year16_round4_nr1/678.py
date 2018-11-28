#include <iostream>
#include <algorithm>
#include <string>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <stack>
#include <sstream>
#include <cmath>
#include <cstdio>
#include <cstring>
#include <cstdlib>

using namespace std;

char winner(char a, char b) {
	if (a == b)
		return 0;
	if (a == 'R' && b == 'S')
		return a;
	if (b == 'R' && a == 'S')
		return b;
	if (a == 'P' && b == 'S')
		return b;
	if (b == 'P' && a == 'S')
		return a;
	if (a == 'R' && b == 'P')
		return b;
	if (b == 'R' && a == 'P')
		return a;
}

bool checkans(string cur)
{
	if (cur.size() == 1)
		return true;

	string newcur = "";
	for (int i = 0; i < cur.size(); i += 2) {
		char w = winner(cur[i], cur[i + 1]);
		if (!w)
			return false;
		newcur += w;
	}
	return checkans(newcur);
}

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int t;
	cin >> t;

	for (int test = 1; test <= t; test++) {
		cout << "Case #" << test << ": ";
		int n, r, p, s;
		cin >> n >> r >> p >> s;
		string ans = "";

		int N = 1 << n;
		vector <int> per(N + 1);
		while (!per[N]) {
			per[0]++;
			int i = 0;
			while (per[i] > 2) {
				per[i++] = 0;
				per[i]++;
			}
			
			string cur = "";
			int R = r, P = p, S = s;
			for (int i = 0; i < N; i++) {
				if (per[i] == 0) R--, cur += "R";
				if (per[i] == 1) P--, cur += "P";
				if (per[i] == 2) S--, cur += "S";
			}
			if (!R && !P && !S)
				if (checkans(cur))
					if (ans == "" || ans > cur)
						ans = cur;					
			
		}

		if (ans == "")
			ans = "IMPOSSIBLE";

		cout << ans << endl;
	}

	return 0;
}