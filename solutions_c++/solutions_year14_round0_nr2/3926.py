#include<stdio.h>
#include<stdlib.h>

using namespace std;

int main(void){
	double c,f,x;
	int n;
	scanf("%d\n",&n);
	for (int i = 1;i <= n; i++){
		scanf("%lf %lf %lf\n",&c,&f,&x);
		double t,g,m;
		m = t = 0;
		g = 2;
		while(m < x){
			double t1,t2;
			t1 = (x/g);
			t2 = (c/g) + (x/(g+f));
			if (t1 < t2){
				t += t1;
				m += g*t;
			} else {
				t += (c/g);
				g += f;
			}	
		}
		printf("Case #%d: %.7lf\n",i,t);
	}
}
