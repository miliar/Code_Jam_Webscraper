#include <cstdio>
#include <cmath>
using namespace std;
double c, f, x;
double solve(){
	if(c*(2+f) >= x*f) return x/2;//t1<=t2
	double n = (f*x/c-2)/f;// n>1
	double ns = floor(n) + 1;//best point, >=2
	double res = 0;
	for (int j = 0; j <= ns-2; j++) {
		res += c/(2+j*f);
	}
	res += x/(2+(ns-1)*f);
	return res;
}
int main(int argc, const char *argv[])
{
	int T;
	scanf("%d", &T);
	for (int i = 1; i <= T; i++) {
		scanf("%lf%lf%lf", &c, &f, &x);
		//printf("%f,%f,%f\n", c, f, x);
		double res = solve();
		printf("Case #%d: %.8f\n", i, res);
	}
	return 0;
}
