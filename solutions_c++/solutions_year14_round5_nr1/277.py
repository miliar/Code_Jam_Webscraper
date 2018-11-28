#include <iostream>
#include <cstdio>
#include <algorithm>
using namespace std;

#define left Left
#define right Right

int tn, ti, n, p, q, r, s, a[1000000 + 5], i, j;
long long tot, f[1000000 + 5], lose, left, right, center;
double ans;

long long maxg (int i, int j) {
	++i; ++j;
	left = f[i - 1];
	right = f[n] - f[j];
	center = f[j] - f[i - 1];
	return max(left, max(right, center));
}

int main (int argc, char * const argv[]) {
	freopen("input.txt", "r", stdin);
	scanf("%d", &tn);
	for(ti = 1; ti <= tn; ti++) {
		scanf("%d %d %d %d %d", &n, &p, &q, &r, &s);
		tot = 0;
		for(i = 0; i < n; i++) {
			a[i] = (i * 1LL * p + q) % r + s;
			tot += a[i];
		}
		for(i = 0; i < n; i++) f[i + 1] = f[i] + a[i];
		lose = tot;
//		printf("%d\n", maxg(4, 5));
		
//		for(i = 0; i < n; i++) 
//			for(j = i; j < n; j++) lose = min(lose, maxg(i, j));
		
		for(i = j = 0; i < n; i++) {
			while (j < i && maxg(j, i) > maxg(j + 1, i)) ++j;
			lose = min(lose, maxg(j, i));
		}
		ans = 1.0 * (tot - lose) / (double)(tot);
		printf("Case #%d: %.10lf\n", ti, ans);
	}
    return 0;
}
