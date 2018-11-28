#include <bits/stdc++.h>

using namespace std;

unordered_map<string, vector<int>> dpmem;

int dp(string s, int from, int mode)
{
	if (dpmem[s].size() && from >= 0 && dpmem[s][from+100*(mode+1)] != 0)
		return dpmem[s][from+100*(mode+1)]-1;

	dpmem[s].resize(210, 0);

	char good = mode?'+':'-';
	char bad = mode?'-':'+';
	//cout << s << ":"<<from<<endl;
	for (; from >= 0; from--) {
		if (s[from] == good)
			continue;
		int sol = 10E6;

		if (s[0] == bad) {
			string s2(s);
			for (int i = from, j = 0; i >= 0; i--, j++)
				s2[i] = s[j]==good?bad:good;
			sol = min(1+dp(s2, from-1, mode), sol);
		}

		sol = min(sol, 1+dp(s, from-1, !mode));
		dpmem[s][from+100*(mode+1)] = sol+1;
		return sol;
	}
	if (from >= 0)
	dpmem[s][from+100*(mode+1)] = 1;
	return 0;
}

void solve()
{
	dpmem.clear();
	string s;
	cin >> s;

	cout << dp(s, s.length()-1, 1);
}

int main()
{
	int T;
	cin >> T;
	for (int i = 1; i <= T; i++) {
		cout << "Case #" << i << ": ";
		solve();
		cout << endl;
	}
}
