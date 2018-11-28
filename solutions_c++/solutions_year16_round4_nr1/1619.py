#include <iostream>
#include <string>
#include <algorithm>
using namespace std;

bool check(string s, int N) {
	if (!N) return true;
	else {
		string tmp = "";
		for (int i=0; i<(int)s.size(); i+=2) {
			if (s[i] == s[i+1]) return false;
			
			if ((s[i] == 'R' && s[i+1] == 'P') || (s[i] == 'P' && s[i+1] == 'R')) tmp += 'P';
			else if ((s[i] == 'R' && s[i+1] == 'S') || (s[i] == 'S' && s[i+1] == 'R')) tmp += 'R';
			else if ((s[i] == 'P' && s[i+1] == 'S') || (s[i] == 'S' && s[i+1] == 'P')) tmp += 'S';
		}
		return check(tmp, N-1);
	}
}

int main() {
	int T, t, N, R, P, S, i;

	cin >> T;
	for (t=1; t<=T; t++) {
		cin >> N >> R >> P >> S;
		
		string cur = "";
		for (i=0; i<P; i++) cur += "P";
		for (i=0; i<R; i++) cur += "R";
		for (i=0; i<S; i++) cur += "S";
		
		bool flag = false;
		do {
			flag = check(cur, N);
		} while (!flag && next_permutation(cur.begin(), cur.end()));
		
		cout << "Case #" << t << ": ";
		if (flag) cout << cur << endl;
		else cout << "IMPOSSIBLE" << endl;
	}

	return 0;
}
