#include <stdio.h>
#include <string.h>
int main()
{
	int t, i;
	double c, f, x;
	double init_s = 2.0;
	double ans, tmp, speed, cur;
	scanf("%d", &t);
	for(i = 1; i <= t; i++) {
		scanf("%lf %lf %lf", &c, &f, &x);
		speed = init_s;
		cur = 0;
		ans = x/ speed;
		while( 1) {
			tmp = cur + c/ speed + x / (speed + f);
			if(tmp < ans) {
				ans = tmp;
				cur += c/ speed; 
				speed += f;
			} else {
				break;
			}
		}
		printf("Case #%d: %.7lf\n", i, ans);
	}
	return 0;
}
