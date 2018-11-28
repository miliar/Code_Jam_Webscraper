#include <iostream>
#include <iomanip>
#include <cstdio>
#include <list>

using namespace std;

int main() {
	int T;
	cin>>T;
	
	double c,f,x,rate;
	
	for(int i=0;i<T;i++) {
		rate = 2.0;
		
		scanf("%lf",&c);
		scanf("%lf",&f);
		scanf("%lf",&x);
		
		double time = x/rate, prev, init;
		prev = time;
		init = time;
		
		time = 0;
		while(1){
			time = time + c/rate;
			rate = rate + f;
			if(prev<time+(x/rate)){
				printf("Case #%d: ",i+1);
				if(init<prev)
					printf("%.7lf\n",init);
				else
					printf("%.7lf\n",prev);
				break;
			}
			else{
				prev = time+(x/rate);
			}
			//printf("time = %lf + %lf = %.7lf\n\n",time,x/rate,(time+(x/rate)));
		}
	}	
}
