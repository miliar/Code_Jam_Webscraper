#line 1 "A.cpp"
#include <cstdio>
#include <iostream>
#include <algorithm>
#include <vector>
#include <queue>
#include <deque>
#include <stack>
#include <set>
#include <map>
#include <unordered_set>
#include <unordered_map>
#include <string>
#include <cassert>
#include <cmath>
#include <cstring>
#include <functional>
#include <random>
using namespace std;
typedef vector<int> VI;
typedef pair<int,int> PII;
typedef vector<PII> VPII;
typedef long long ll;
#define REP(i,a,n) for (int i = (a); i < (n); i++)

template<class T> T& setmin(T &a, const T &b) {return a = min(a, b);}
template<class T> T& setmax(T &a, const T &b) {return a = max(a, b);}
template<class T> T MODD(const T &a, const T &b) {T r = a%b; if (r < 0) r += b; return r;}

const int MAXN = 15;

char ch[] = "PRS";

string dp[3][MAXN];

void docase() {
	int N, R, P, S;
	scanf("%d%d%d%d", &N, &R, &P, &S);
	bool found = false;
	string res;
	REP(s,0,3) {
		int Rf = 0, Pf = 0, Sf = 0;
		for (char c : dp[s][N]) {
			if (c == 'R')
				Rf++;
			if (c == 'P')
				Pf++;
			if (c == 'S')
				Sf++;
		}
		if (Rf == R && Pf == P && Sf == S) {
			if (!found || res > dp[s][N]) {
				found = true;
				res = dp[s][N];
			}
		}
	}
	if (found)
		printf("%s\n", res.c_str());
	else
		printf("IMPOSSIBLE\n");
}

int main() {
	REP(s,0,3)
		dp[s][0] = ch[s];
	REP(n,1,MAXN) REP(s,0,3)
		dp[s][n] = min(dp[s][n-1]+dp[(s+1)%3][n-1], dp[(s+1)%3][n-1]+dp[s][n-1]);
	int T;
	scanf("%d ", &T);
	for (int test = 0; test < T; test++) {
		fprintf(stderr, "Test %d/%d\n", test+1, T);
		printf("Case #%d: ", test+1);
		docase();
		fflush(stdout);
		fflush(stderr);
	}
	return 0;
}
