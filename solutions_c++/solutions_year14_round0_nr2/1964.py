#include <stdio.h>
int main(void){
	int t, flag;
	double c, f, x;
	double v;
	double time;
	scanf("%d", &t);
	for (int i = 0; i < t; i++){
		scanf("%lf%lf%lf", &c, &f, &x);
		flag = 0;
		v = 2;
		if (((x - c) / v) > (x / (v + f))){
			flag = 1;
			time = c / 2;
		}
		while (((x - c) / v) > (x / (v + f))){
			v += f;
			time += c / v;
		}
		if (flag == 1)
			time += (x - c) / v;
		else
			time = x / 2;
		printf("Case #%d: %.7f\n", i + 1, time);
	}
	return 0;
}
