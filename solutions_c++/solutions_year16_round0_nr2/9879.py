#include <bits/stdc++.h>
using namespace std;
string reduced(string s) {
	string sreduced;
	for (int i=0;i<(int)s.size();i++)if(i==0||s[i]!=s[i-1])sreduced+=s[i];
	if (sreduced.back() == '+') sreduced = sreduced.substr(0, sreduced.length()-1);
	return sreduced;
}
int main() {
	map<string, int> M;
	M[""] = 0;
	for (int length=1; length<=100; length++) {
		string s; for (int i=0;i<length;i++) s += (i%2==length%2)?'+':'-';
		if (M.count(s)) continue;
		M[s] = 1e9;
		// flip
		for (int k=1; k<=(int)s.size(); k++) {
			string s2;
			for (int i=0;i<k;i++)s2+='+'+'-'-s[k-1-i];
			s2 += s.substr(k);
			if (reduced(s2) == s) continue;
			M[s] = min(M[s], M[reduced(s2)] + 1);
		}
	}
	int T; cin >> T;
	for (int tc=1; tc<=T; tc++) {
		string s; cin >> s;
		printf("Case #%d: %d\n", tc, M[reduced(s)]);
	}
}
