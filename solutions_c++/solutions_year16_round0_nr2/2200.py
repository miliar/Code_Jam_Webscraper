#include <cstdio>
#include <iostream>
#include <string>

using namespace std;

#define FOR(i,a,b) for(int i=int(a);i<=int(b);++i)
#define REP(i,n) FOR(i,0,(n)-1)

int main() {
	int cN, tN, x;
	cin >> tN;
	FOR(cN, 1, tN) {
		string s;
		cin >> s;
		s += "+";
		int ans = 0;
		REP(i, s.size()-1) if (s[i] != s[i+1]) ++ans;
		if (s[s.size()-1] == '-') ++ans;
		printf("Case #%d: %d\n", cN, ans);
	}
}
