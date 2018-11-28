#include <stdio.h>
#include <algorithm>
using namespace std;

struct A {
	double l, temp;
} a[99];

int main() {
	freopen("input.txt", "r", stdin);
	//freopen("output.txt", "w", stdout);
	FILE *fp2 = fopen("output.txt", "w");

	int test;
	scanf("%d", &test);

	for (int t = 1; t <= test; t++) {
		int n;
		double l, temp;
		scanf("%d %lf %lf", &n, &l, &temp);

		for (int i = 1; i <= n; i++) {
			scanf("%lf %lf", &a[i].l, &a[i].temp);
		}

		if (n == 1) {
			if (temp == a[1].temp) {
				fprintf(fp2, "Case #%d: %.10lf\n", t, l / a[1].l);
			}
			else {
				//printf("%lf %lf\n", l, temp);
				//printf("%lf %lf\n\n", a[1].l, a[1].temp);
				fprintf(fp2, "Case #%d: IMPOSSIBLE\n", t);
			}
		}
		else {
			if (a[1].temp > a[2].temp) {
				swap(a[1].temp, a[2].temp);
				swap(a[1].l, a[2].l);
			}
			if (a[1].temp == a[2].temp && a[1].l > a[2].l) {
				swap(a[1].l, a[2].l);
			}

			if (temp > a[2].temp || temp < a[1].temp) {
				//printf("%lf %lf\n", l, temp);
				//printf("%lf %lf\n", a[1].l, a[1].temp);
				//printf("%lf %lf\n\n", a[2].l, a[2].temp);

				fprintf(fp2, "Case #%d: IMPOSSIBLE\n", t);
				//printf("\n");
			}
			else {
				if (a[1].temp == a[2].temp) {
					//printf("%lf %lf\n", l, temp);
					//printf("%lf %lf\n", a[1].l, a[1].temp);
					//printf("%lf %lf\n", a[2].l, a[2].temp);
					fprintf(fp2, "Case #%d: %.10lf\n", t, l / (a[1].l + a[2].l));
				}

				else if (a[1].temp == temp) {
					fprintf(fp2, "Case #%d: %.10lf\n", t, l / a[1].l);
				}
				else if (a[2].temp == temp) {
					fprintf(fp2, "Case #%d: %.10lf\n", t, l / a[2].l);
				}
				else {
					double total = a[2].temp - a[1].temp;

					double t1 = l * (a[2].temp - temp) / (total * a[1].l);
					double t2 = l * (temp - a[1].temp) / (total * a[2].l);

					//printf("%.3lf %.3lf\n", r1, r2);
					//printf("%.3lf %.3lf\n", l1, l2);
					//printf("%.3lf %.3lf\n", t1, t2);

					fprintf(fp2, "Case #%d: %.10lf\n", t, t1 > t2 ? t1 : t2);
					printf("Case #%d: %.10lf\n", t, t1 > t2 ? t1 : t2);
				}
			}
		}
	}
	return 0;
}