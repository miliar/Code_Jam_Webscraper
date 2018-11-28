#include <cstdio>
#include <algorithm>

using namespace std;

int main(int argc, char const *argv[])
{
	int t;
	scanf("%d", &t);
	for (int q = 1; q <= t; q++) {
		int n;
		double a[1000];
		double b[1000];

		scanf("%d", &n);
		for (int i = 0; i < n; i++) {
			scanf("%lf", a + i);	
		}	
		for (int i = 0; i < n; i++) {
			scanf("%lf", b + i);
		}

		sort(a, a + n);
		sort(b, b + n);
		
		// for (int i = 0; i < n; i++) printf("%lf ", a[i]);
		// printf("\n");
		// for (int i = 0; i < n; i++) printf("%lf ", b[i]);
		// printf("\n");

		int k = 0;
		for (int i = 0; i < n; i++) {
			if (a[i] > b[k]) k++;
		}

		int p = 0;
		int j;
		for (j = 0; j < n; j++) {
			while (p < n && b[p] < a[j]) p++;
			if (p == n) break;
			p++;
		}			
		printf("Case #%d: %d %d\n", q, k, n - j);
	}

	return 0;
}