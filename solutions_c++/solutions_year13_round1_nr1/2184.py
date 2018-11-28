#include <cstdio>
#include <cmath>

#define MAX(a, b) (((a) > (b)) ? (a) : (b))

int main(){
	freopen ("a.in", "r", stdin);
	freopen ("a.out", "w", stdout);
	int t, h = 0;
	scanf ("%d", &t);
	while (h < t){
		double r, t;
		scanf ("%lf%lf", &r, &t);
		double b = 2 * r - 1, a = 2, c = -t, d = b * b - 4 * a * c;
		double k1 = (-b - sqrt (d)) / (2 * a);
		double k2 = (-b + sqrt (d)) / (2 * a);
		k1 = MAX(k1, k2);
		printf ("Case #%d: %.0lf\n", ++h, floor(k1));
	}
}
