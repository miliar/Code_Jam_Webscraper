#include<cstdio>

using namespace std;

int main(){
	int t;
	scanf("%d", &t);
	for(int i=1; i<=t; i++){
		double c, f, x;
		scanf("%lf %lf %lf", &c, &f, &x);

		double cash = 0;
		double t = 0;
		double prod = 2.0;
		while(cash < x){
			if (cash >= c && (x-cash+c)/(prod+f) < (x-cash)/prod){
				prod += f;
				cash -= c;
			}
			
			if ((x-cash) <= c){
				t += (x-cash)/prod;
				cash += x-cash;
			}else{
				t += c/prod;
				cash += c;
			}
		}
		printf("Case #%d: %.7f\n", i, t);
	}
	return 0;
}
