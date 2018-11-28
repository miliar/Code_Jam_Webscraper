#include <cstdio>

int main(){
	long t;
	scanf("%ld",&t);
	for(long g=1; g<=t; g++){
		long double c,f,x,v=2,time=0,temp;
		scanf("%Lf %Lf %Lf",&c,&f,&x);
		temp = x/2;
		while(1){
			time += c/v;
			v += f;
			if(temp>time+x/v) temp = time+x/v;
			else break;
		}
		printf("Case #%ld: %0.7Lf\n",g,temp);
	}
	return 0;
}
