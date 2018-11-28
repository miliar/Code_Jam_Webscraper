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

char t[111][55];

void test() {
	int n,l;
	scanf("%d%d", &n, &l);
	FOR(i,n+1) scanf("%s", t[i]);
	FOR(i,n) {
		bool ok=0;
		for (int j=0;t[i][j]; j++) if (t[i][j]=='0') ok=1;
		if (!ok) {
			printf("IMPOSSIBLE\n");
			return;
		}
	}
	printf("10?1");
	FOR(i,l) printf("01");
	printf(" ");
	FOR(i,l-1) printf("?");
	printf("0\n");
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
