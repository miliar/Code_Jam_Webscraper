#include <bits/stdc++.h>
using namespace std;
#define REP(i,a,b) for (int i = (a); i <= (b); ++i)
#define REPD(i,a,b) for (int i = (a); i >= (b); --i)
#define FORI(i,n) REP(i,1,n)
#define FOR(i,n) REP(i,0,int(n)-1)
#define mp make_pair
#define pb push_back
#define pii pair<int,int>
#define vi vector<int>
#define ll long long
#define SZ(x) int((x).size())
#define DBG(v) cerr << #v << " = " << (v) << endl;
#define FOREACH(i,t) for (typeof(t.begin()) i=t.begin(); i!=t.end(); i++)
#define fi first
#define se second

const int maxn = 100100;

char s[maxn];
char qc[maxn];
int dp[1010][1010];

void test() {
	int n=0, qn = 0;
	scanf("%s", s);
	for (int i = 0; s[i]; i++) {
		if (qn == 0 || qc[qn-1] != s[i]) {
			qc[qn] = s[i];
			qn++;
		} else {
			qn--;
		}
		n++;
	}
	int res=0;
	if (qn == 0) res = n*5;
	else if (qn == 2) res = n*5-5;
	else res = n*5-10;
	res = n*5 - qn/2*5;
	
	printf("%d\n", res);
	
	/*
	for (int i = 0; i < n; i++) dp[i][i+1] = -1e9;
	for (int i = 0; i < n; i++) dp[i][i+2] = s[i]==s[i+1] ? 10 : 5;
	for (int l = 3; l <= n; l++) {
		for (int x = 0; x+l <= n; x++) {
			int y = x+l;
			dp[x][y] = (s[x] == s[y-1] ? 10 : 5) + dp[x+1][y-1];
			for (int m = x+1; m < y; m++) {
				dp[x][y] = max(dp[x][y], dp[x][m] + dp[m][y]);
			}
		}
	}
	printf("%d %d %s\n", dp[0][n], res, dp[0][n] == res ? "" : "!!!!!!");*/
}

int main() {
	int ttn;
	scanf("%d", &ttn);
	for (int i = 1; i <= ttn; i++) {
		printf("Case #%d: ", i);
		test();
	}
	return 0;
}
