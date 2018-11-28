#include <bits/stdc++.h>

using namespace std;

#define INP "inp.txt"
#define OUT "out.txt"

int T;
string s;

int solve() {
	int cnt = 0;
	reverse(s.begin(), s.end());
	
	for(int i = 0; i < s.size(); i++) {
		int a = (s[i] == '+') ? 0 : 1;
		if((a + cnt) % 2 == 0) continue;
		cnt++;
	}
	return cnt;
}

int main () {
	freopen(INP, "r", stdin);
	freopen(OUT, "w", stdout);

	scanf("%d ", &T);
	for(int tt = 1; tt <= T; tt++) {
		cin >> s;

		cout << "Case #" << tt << ": " << solve() << endl;
	}
	return 0;
}