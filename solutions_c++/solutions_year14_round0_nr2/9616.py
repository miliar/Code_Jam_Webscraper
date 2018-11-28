#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<string.h>
#include<algorithm>
#include<cmath>

using namespace std;

double c,x,f;

double produce(int j){
	double ret=x/(2+j*f);
		double aux=0;
		
		for (int i = 0; i < j; i++) {
			aux+=(1/(2+i*f));
		}
		aux*=c;
		ret+=aux;
		return ret;
}
int main(void){

	int cases;
	scanf("%d",&cases);
	for(int i=1;i<=cases;i++){
		scanf("%lf %lf %lf",&c,&f,&x);
		double min=produce(0);
		for(int j=1;j<=x;j++){
			min=fmin(min,produce(j));
		}
		printf("Case #%d: %0.7lf\n",i,min);
	}
	
return 0;
}

