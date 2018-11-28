#include <cstdlib>
#include <cstdio>
#include <algorithm>
#include <cassert>

using namespace std;

const int MAXN = (int)1e5 + 100;

int t;
double c, f, x, tot[MAXN];

void solve(int t) {
	scanf("%lf%lf%lf", &c, &f, &x);
	tot[0] = 0.0;
	double best = 1e200;

	for (int k = 0 ; k <= x ; k ++) {
		if (k)
			tot[k] = tot[k-1] + c/(2. + (k - 1)*f);
		best = min(best, tot[k] + x/(2. + (k)*f) );
	}
	printf("Case #%d: %.12lf\n", t, best);

}

int main() {
	//assert(freopen("input.txt", "r", stdin));
	//assert(freopen("output.txt", "w", stdout));
	scanf("%d", &t);
	for (int i = 1 ; i <= t ; i ++) solve(i); 
		
	return 0;
}