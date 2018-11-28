#include <cstdio>

int main(){
	int t;
	scanf("%d", &t);
	for(int x = 1; x <= t; x++){
		printf("Case #%d: ", x);
		double c, f, x, t = 0.0, r = 2.0;
		scanf("%lf %lf %lf", &c, &f, &x);
		while(1){
			double nt = (c/r);
			if((x/(f+r))+nt > x/r){
				printf("%lf\n", t + x/r);
				break;
			}
			t += nt;
			r += f;
		}
	}

	return 0;
}
