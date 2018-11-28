#include <cstdio>
#include <string>
#include <algorithm>
using namespace std;
string m;
string g(string s) {
	if( s.size() == 1 )
		return s;
	string a = s.substr(0, s.size()/2);
	string b = s.substr(s.size()/2, s.size()/2);
	a = g(a);
	b = g(b);
	if( a < b )
		return a + b;
	return b + a;
}

string f(int dep, string s) {
	if( dep == 0 ) 
		return s;
	string r;
	for(auto &c : s) {
		if( c == 'P' ) {
			r += "PR";
		}
		if( c == 'R' ) {
			r += "RS";
		}
		if( c == 'S' ) {
			r += "PS";
		}
	}
	return f(dep-1, r);
}

bool ok(string z, int R, int P, int S) {
	for(auto &c : z) {
		if( c == 'P' ) {
			--P;
		}
		if( c == 'R' ) {
			--R;
		}
		if( c == 'S' ) {
			--S;
		}
	}
	return P == 0 && R == 0 && S == 0;
}

int main() {
	int T, ics = 0;
	scanf("%d", &T);
	while(T--) {
		int N, R, P, S;
		scanf("%d%d%d%d", &N, &R, &P, &S);
		string a = g(f(N, "R"));
		string b = g(f(N, "P"));
		string c = g(f(N, "S"));
		string ans = "Z";
		if( ok(a, R, P, S) && a < ans )
			ans = a;
		if( ok(b, R, P, S) && b < ans )
			ans = b;
		if( ok(c, R, P, S) && c < ans )
			ans = c;
		printf("Case #%d: ", ++ics);
		if( ans[0] == 'Z' )
			printf("IMPOSSIBLE\n");
		else
			printf("%s\n", ans.c_str());
	}
	return 0;
}