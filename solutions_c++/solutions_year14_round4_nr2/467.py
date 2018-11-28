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

int a[1111], b[1111];

void test() {
	int n;
	scanf("%d", &n);
	FOR(i,n) scanf("%d", &a[i]);
	FOR(i,n) b[i] = a[i];
	sort(b,b+n);
	int res = 0;
	FOR(i,n) {
		int le = 0, ri = 0;
		bool fnd = false;
		FOR(j,n) {
			if (a[j] == b[i]) {
				fnd = true;
			} else if (a[j] > b[i]) {
				if (fnd) ri++;
				else le++;
			}
		}
		res += min(le, ri);
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