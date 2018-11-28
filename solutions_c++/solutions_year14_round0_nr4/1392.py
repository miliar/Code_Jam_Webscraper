#include<cstdio>
#include<algorithm>
using namespace std;

int t, cn=1;
int n, i, j, normal, deceitful;
double naomi[1000], ken[1000];

int main() {
	//freopen("D-large.in", "r", stdin);
	//freopen("D-large.out", "w", stdout);
	for (scanf("%d", &t); cn<=t; ++cn) {
		scanf("%d", &n);
		for (i=0; i<n; i++)
			scanf("%lf", naomi+i);
		for (i=0; i<n; i++)
			scanf("%lf", ken+i);
		sort(naomi, naomi+n);
		sort(ken, ken+n);
		normal = deceitful = i = j = 0;
		while (i<n) {
			while (j<n && naomi[i] > ken[j]) ++j;
			if (j == n) break;
			++i; ++j;
		}
		normal = n-i;
		int jmax = n-1; i=j=0;
		while (i<n) {
			if (naomi[i] < ken[j]) --jmax;
			else ++j, ++deceitful;
			++i;
		}
		printf("Case #%d: %d %d\n", cn, deceitful, normal);
	}
	return 0;
}