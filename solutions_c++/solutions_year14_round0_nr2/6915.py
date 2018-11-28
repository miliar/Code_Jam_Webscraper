#include <stdio.h>
int maze[5][5];
int main () {
	int T;
//	freopen("B-large.in","r",stdin);
//	freopen("Bl.out","w",stdout);
	scanf ("%d",&T);
	int cas = 0;
	while (T --) {
		cas ++;
		double c,f,x;
		scanf ("%lf%lf%lf",&c,&f,&x);
		double day = 0;
		double p = 2;
		if (c > x) {
			day = x / p;
		} else {
			while (true) {
				day += c / p;
				double t1 = (x - c) / p;
				double t2 = (x) / (p + f);
				if (t2 < t1) {
					p += f;
				} else {
					day += t1;
					break;
				}
			}
		}
		printf("Case #%d: ",cas);
		printf("%.7lf\n",day);
	}
	return 0;
}