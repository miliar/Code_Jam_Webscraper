#include <cstdio>
#include <algorithm>
using namespace std;

using namespace std;

#define REP(i,a,b) for (int i = (a); i <= (b); i++)
#define REPD(i,a,b) for (int i = (a); i >=(b); i--)
#define FORI(i,n) REP(i,1,n)
#define FOR(i,n) REP(i,0,int(n)-1)
#define mp make_pair
#define pb push_back
#define pii pair<int,int>
#define vi vector<int>
#define ll long long
#define SZ(x) int((x).size())
#define DBG(v) cerr << #v << " = " << (v) << endl;
#define FOREACH(i,t) for (auto i = t.begin(); i != t.end(); i++)
#define fi first
#define se second

int s[10100];

void test() {
	int n,x;
	scanf("%d%d", &n, &x);
	FOR(i,n) scanf("%d", &s[i]);
	sort(s,s+n);
	int fst = 0;
	int res = 0;
	for (int i = n-1; i >= fst; i--) {
		if (i != fst && s[i] + s[fst] <= x) {
			fst++;
		}
		res++;
	}
	printf("%d\n", res);
}

int main() {
	int te;
	scanf("%d", &te);
	for (int tt = 1; tt <= te; tt++) {
		printf("Case #%d: ", tt);
		test();
	}
	return 0;
}