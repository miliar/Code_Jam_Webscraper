#include<cstdio>


using namespace std;


int main(){
	int t;
	scanf("%d", &t);
	int index=1;
	
	while (t--) {
		double c,f,x;
		
		scanf("%lf%lf%lf", &c, &f, &x);
		
		double timme=0.0;
		double grad = (x-c)/x;
		double freq=2.0;
		
		
		while (grad>(freq/(freq+f))) {
			timme+=(c/freq);
			freq+=f;
		}
		timme+=(x/freq);
				
		printf("Case #%d: %.7lf\n", index, timme);index++;
		
	}
	
	return 0;
}