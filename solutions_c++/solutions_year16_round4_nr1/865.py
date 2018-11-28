#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sstream>
#include <iostream>
#include <math.h>
#include <time.h>
#include <unistd.h>
#include <algorithm>
#include <map>
#include <list>
#include <queue>
#include <stack>
#include <vector>
#include <set>
#include <string>

#ifndef ONLINE_JUDGE
	#define DEBUG(x) cout << '>' << #x << ':' << x << endl;
#else
	#define DEBUG(x) do {} while(0);
#endif

#define pb push_back
#define mp make_pair
#define X first
#define Y second
#define FOR(i, A, N) for(int (i) = (A); (i) < (N); (i)++)
#define REP(i, N) for(int (i) = 0; (i) < (N); (i)++)

using namespace std;
typedef long long ll;
inline bool EQ(double a, double b) { return fabs(a-b) < 1e-9; }

int n,m;
int T;
char vals[10];
int perm[10];

string getopp(string win) {
	if(win == "P")
		return "R";
	else if(win == "R")
		return "S";
	else
		return "P";
}
int ML;

pair<bool, string> gen(string winner, int& r, int& p, int& s, int lev=0) {
//	printf("I %s %d %d %d %d [ML=%d]\n", winner.c_str(), r, p, s, lev, ML);
	if(lev == ML)
		return mp(true, winner);

	if(winner == "P")
		if(r == 0)
			return mp(false, "");
		else
			r--;
	if(winner == "R")
		if(s == 0)
			return mp(false, "");
		else
			s--;
	if(winner == "S")
		if(p == 0)
			return mp(false, "");
		else
			p--;

	string opp = getopp(winner);
	auto h1 = gen(winner, r, p, s, lev+1);
	auto h2 = gen(opp, r, p, s, lev+1);
//	printf("X %s %d %d %d %d\n", winner.c_str(), r, p, s, lev);
	if(h1.first&&h2.first) {
		string S = h1.second + h2.second;
		string S2 = h2.second + h1.second;
		if((lev == 0 && r == 0 && p == 0 && s == 0)
		|| lev > 0)
			return mp(true, min(S, S2));
		else if(lev == 0)
			return mp(false, "");
	}
	return mp(false, "");
}

void solve() {
	int n,r,p,s;
	scanf("%d%d%d%d", &n, &r, &p, &s);
	ML=n;
	string ans = "ZZZZ";
	if(r > 0) {
		int rr = r-1, pp = p, ss = s;
		auto tmp = gen("R", rr, pp, ss);
		if(tmp.first)
			ans = tmp.second;
	}
	if(p > 0) {
		int rr = r, pp = p-1, ss = s;
		auto tmp = gen("P", rr, pp, ss);
		if(tmp.first)
			ans = min(ans, tmp.second);
	}
	if(s > 0) {
		int rr = r, pp = p, ss = s-1;
		auto tmp = gen("S", rr, pp, ss);
		if(tmp.first)
			ans = min(ans, tmp.second);
	}
	if(ans == "ZZZZ")
		ans = "IMPOSSIBLE";
	printf("%s", ans.c_str());
}

int main() {
	scanf("%d", &T);
	REP(testc, T) {
		printf("Case #%d: ", testc+1);
		solve();
		printf("\n");
	}
	return 0;
}
