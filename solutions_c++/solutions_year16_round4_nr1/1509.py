#include <bits/stdc++.h>
using namespace std;

int T, i, N, R, P, S;

bool solve(string s)
{
	if (s.length() == 1) 
		return true;
	string s1;
	for (int i=0; i<s.length(); i+=2)
		if (s[i] == 'P' && s[i+1] == 'R' || s[i+1] == 'P' && s[i] == 'R') s1 += 'P';
		else if (s[i] == 'P' && s[i+1] == 'S' || s[i+1] == 'P' && s[i] == 'S') s1 += 'S';
		else if (s[i] == 'R' && s[i+1] == 'S' || s[i+1] == 'R' && s[i] == 'S') s1 += 'R';
		else return false;
	return solve(s1);
}

int main() {
	cin >> T;
	for (int t=1; t<=T; t++) {
		cin >> N >> R >> P >> S;
		int NN = 1 << N;
		string s = string(P, 'P') + string(R, 'R') + string(S, 'S');
		string ans = "X";
		do {
			if (solve(s) && s < ans) ans = s;
		} while (next_permutation(s.begin(), s.end()));

		if (ans == "X") ans = "IMPOSSIBLE";
		cout << "Case #" << t << ": " << ans << endl;
	}
}
