#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cctype>
#include <cstring>
#include <string>
#include <climits>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <stack>
#include <list>
#include <ctime>

#define PI 3.14159265358979
#define EPS 1e-9

using namespace std;

#define REP(i, n) for (int i=0; i<n; i++)
#define FOR(i, m, n) for (int i=m; i<=n; i++)
#define ABS(a) (((a)>0)?(a):(-(a)))
typedef long long ll;
typedef unsigned long long ull;
typedef pair<int,int> ii;

void solve() {
	vector<int> v;
	int cnt = 0; int ans = 0;
	int n; scanf("%d", &n); n--;
	REP (i, 4) REP (j, 4) {
		int x; scanf("%d", &x);
		if (i==n) v.push_back(x);
	}
	scanf("%d", &n); n--;
	REP (i, 4) REP (j, 4) {
		int x; scanf("%d", &x);
		if (i==n) REP (k, 4) if (x==v[k]) { cnt++; ans = x; }
	}
	if (cnt==0) printf("Volunteer cheated!\n");
	else if (cnt==1) printf("%d\n", ans);
	else printf("Bad magician!\n");
}

int main()
{
	int t;
	scanf("%d", &t);
	REP (i, t) {
		printf("Case #%d: ", i+1);
		solve();
	}
	return 0;
}
