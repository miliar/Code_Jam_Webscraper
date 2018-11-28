#include <cstdio>
using namespace std;

int main(){
	int T;
	double C,F,X,time,rate,cookies;
	scanf("%d",&T);
	for (int i=1;i<=T;i++){
		scanf("%lf%lf%lf",&C,&F,&X);
		time=0;
		rate=2;
		cookies=0;
		//time taken to make at current rate / time taken to create farm and make
		while (X/rate>(C/rate+(X/(rate+F)))){
			time+=C/rate;
			rate+=F;
		}
		time+=X/rate;
		printf("Case #%d: %lf\n", i,time);
	}
}