#include <bits/stdc++.h>

using namespace std;
typedef long long ll;
typedef long double ld;

const int MAXN = 1007;
const double EPS = 0.00000005;

double naomi[MAXN], ken[MAXN];

bool dCompare(double a, double b){
	return a > b;
}

int main(){
	freopen("d.in", "r", stdin);
	freopen("d.out", "w", stdout);

	int t;
	scanf("%d", &t);
	for (int tcase = 1; tcase <= t; ++tcase){
		memset(naomi, 0, sizeof(naomi));
		memset(ken, 0, sizeof(ken));
		printf("Case #%d: ", tcase);
		int n;
		scanf("%d", &n);
		for (int i = 0; i < n; ++i)
			scanf("%lf", &naomi[i]);
		for (int j = 0; j < n; ++j)
			scanf("%lf", &ken[j]);
		sort(naomi, naomi + n);
		sort(ken, ken + n);
		int y = 0, z = 0;
		int l = 0, r = n - 1;
		for (int i = 0; i < n; ++i){
			if (naomi[i] - ken[l] < EPS)
				--r;
			else
				++l;
		}

		y = r + 1;
		r = 0;
		z = n;
		for (int i = 0; i < n && r < n; ++i){
			while (r < n && naomi[i] - ken[r] > EPS)
				++r;
			if (r < n)
				z--;
			++r;
		}
//		printf("\n");
//		for (int i = 0; i < n; ++i)
//			printf("%.3lf ", naomi[i]);
//		printf("\n");
//		for (int i = 0; i < n; ++i)
//			printf("%.3lf ", ken[i]);
//		printf("\n");
		printf("%d %d\n", y, z);
	}
	return 0;
}
