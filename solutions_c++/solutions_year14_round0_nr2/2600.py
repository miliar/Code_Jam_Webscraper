#include "iostream"
#include "cstring"
#include "cstdio"
#include "cmath"
using namespace std;
const double eps = 1e-8;
int dbcmp(double x)
{
	if(x > eps){
		return 1;
	}else if(x < -eps){
		return -1;
	}
	return 0;
}
int main(void)
{
	int T, l1, l2;
	freopen("B-large.in","r", stdin);
	freopen("B.out","w", stdout);
	int g = 0;
	scanf("%d", &T);
	double C, F, X;
	while(T --){
		printf("Case #%d: ",++ g);
		cin >> C >> F >> X;
		double v = 2.0;
		double ans = X / v;
		double t = 0;
		while(dbcmp(ans - t) >= 0){
			t += C / v;
			v += F;
			ans = min(ans, t + X / v);
		}
		printf("%.9lf\n", ans);
	}
	return 0;
}
