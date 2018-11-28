#include <stdio.h>

int main()
{
	int tc;
	int cnt = 0;
	scanf("%d", &tc);
	while(cnt++ < tc){
		double c, f, x;
		double p = 2;
		double t = 0;
		double get = 0;
		//c : farmcost, f : farmproductivity, x : goal 
		scanf("%lf %lf %lf", &c, &f, &x);
		
		double ans = 0;
		while(1){
			//double time = c / p;
			if(x / p <= (x / (p + f) + c / p)){
				ans += x / p;
				break;
			}
			ans += c / p;
			p += f;
		}
		printf("Case #%d: %.7lf\n", cnt, ans);
	}
	return 0;
}