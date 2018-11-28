#include <bits/stdc++.h>
#define fr(i,a,b) for (int i = (a), __ = (b); i < __; ++i)
#define st first
#define nd second
#define dbg(x) cout << #x << " " << x << endl
using namespace std;

const double eps = 1e-7;
const int inf = 0x3f3f3f3f;
typedef pair<int,int> ii;
typedef long long ll;

double naomi[1005], ken[1005];
int markken[1005], passo = 0;

int cmp(double a, double b) {
	if (fabs(a-b) < eps) return 0;
	return a < b ? -1 : 1;
}

int main() {
	int nt; scanf("%d", &nt); ++nt;
	fr(_,1,nt) {
		int n, dec = 0, war = 0;
		scanf("%d", &n);
		fr(i,0,n) scanf("%lf", &naomi[i]);
		fr(i,0,n) scanf("%lf", &ken[i]);
		sort(ken, ken+n);
		++passo;
		fr(i,0,n) {
			int a = upper_bound(ken, ken+n, naomi[i]) - ken;
			while (a < n && markken[a] == passo) ++a;
			if (a == n) ++war;
			else markken[a] = passo;
		}
		
		sort(naomi, naomi+n, greater<double>());
		reverse(ken, ken+n);
		
		int naomiFim = n-1;
		int naomiS = 0, kenS = 0;
		while (n--) {
			if (naomiS <= naomiFim && cmp(naomi[naomiS], ken[kenS]) > 0) {
				naomiS++; kenS++; ++dec;
			} else {
				++kenS; --naomiFim;
			}
		}
		
		printf("Case #%d: %d %d\n", _, dec, war);
	}
	return 0;
}

