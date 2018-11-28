#include <cstdio>
#include <algorithm>
using namespace std;

int main() {
	int T, casenum=1;
	scanf ("%d", &T);
	while (T--) {
		int n, war=0, dwar=0;
		double naomi[1000], ken[1000];
		scanf ("%d", &n);
		for (int i = 0; i < n; i++)
			scanf ("%lf", &naomi[i]);
		for (int i = 0; i < n; i++)
			scanf ("%lf", &ken[i]);
		sort(naomi, naomi+n);
		sort(ken, ken+n);
		for (int i = n-1, j = n-1; i >= 0; i--) {
			if (naomi[i] > ken[j]) war++;
			else j--;
		}
		for (int i = 0, j = 0; i < n && j < n; ) {
			if (naomi[i] > ken[j]) { dwar++; i++; j++; }
			else i++;
		}
		printf ("Case #%d: %d %d\n", casenum++, dwar, war);
	}
	return 0;
}