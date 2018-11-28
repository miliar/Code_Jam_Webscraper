#include <iostream>
using namespace std;

int main() {
	// your code goes here
	float time=0;
	float cookie=0;
	float rate=2;
	int i,t;
	float c,f,x;
	scanf("%d",&t);
	for(i=0;i<t;i++){
		scanf("%f %f %f",&c,&f,&x);
		//printf("%f %f %f",c,f,x);
		time=0;
		rate=2;
		if(x<c){
			time=x/rate;
			printf("Case #%d: %f\n",i+1,time);
		}
		else{
			while(x/rate > (c/rate + x/(rate+f))){
				time=time+c/rate;
				//printf("%f\n",time);
				rate=rate+f;
			}
			time=time+x/rate;
			printf("Case #%d: %f\n",i+1,time);
		}
	}
	return 0;
}