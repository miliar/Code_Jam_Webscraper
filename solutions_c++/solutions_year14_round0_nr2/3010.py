#include <cstdio>
#include <algorithm>
using namespace std;

int tn, qt, i;
double c, f, x, ret, spd, carry;

int main () {
	scanf("%d", &tn);
	while (tn--) {
		scanf("%lf %lf %lf", &c, &f, &x);
		spd = 2; 
		ret = 1e50;
		carry = 0;
		for(i = 0; i <= 100000; i++) {
			ret = min(ret, carry + x / spd);
			carry += c / spd;
			spd += f;
		}
		++qt;
		printf("Case #%d: %.10lf\n", qt, ret);
	}
	return 0;
}