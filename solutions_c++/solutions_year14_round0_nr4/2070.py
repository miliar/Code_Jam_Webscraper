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

int N;
vector<double> naomi;
vector<double> ken;

int war() {
	int k = 0; int res = 0;
	REP(n, naomi.size()) {
		while (k<ken.size() && ken[k]<naomi[n]) k++;
		if (k==ken.size()) res++;
		else k++;
	}
	return res;
}

int decwar() {
	int l = 0; int r = ken.size()-1; int res = 0;
	REP(n, naomi.size()) {
		if (naomi[n]>ken[l]) { l++; res++; }
		else { r--; }
	}
	return res;
}

void solve() {
	naomi.clear(); ken.clear();
	scanf("%d", &N);
	REP(i, N) { double x; scanf("%lf", &x); naomi.push_back(x); } sort(naomi.begin(), naomi.end());
	REP(i, N) { double x; scanf("%lf", &x); ken.push_back(x); } sort(ken.begin(), ken.end());
	printf("%d %d\n", decwar(), war());
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
