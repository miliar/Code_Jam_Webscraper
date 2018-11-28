#include <cstdio>
using namespace std;

int main()
{
	int t;
	scanf("%i", &t);
	for (int i = 0; i < t; i++) {
		double c, f, x;
		scanf("%lf%lf%lf", &c, &f, &x);
		double s = 0;
		double p = 2;
		double a = x / p;
		while (1) {
			s += c / p;
			p += f;
			double b = s + x / p;
			if (b > a) break;
			a = b;
		}
		printf("Case #%i: %.7lf\n", i +1, a);
	}
	return 0;
}

