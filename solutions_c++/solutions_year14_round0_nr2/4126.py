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

int main() {
	int nt; scanf("%d", &nt); ++nt;
	fr(_,1,nt) {
		double C, X, F, ans = 0, taxa = 2;
		scanf("%lf %lf %lf", &C, &F, &X);
		while (C/taxa + X/(taxa+F) < X/taxa) {
			ans += C/taxa;
			taxa += F;
		}
		ans += X/taxa;
		printf("Case #%d: %.7lf\n", _, ans);
	}
	return 0;
}
