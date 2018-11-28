#include <iostream>
#include <cstdio>
#include <cstdlib>

using namespace std;

int main(){
	int n;
	
	scanf("%d",&n);
	
	for(int k=1;k <= n;k++){
		double P, C, F, X;
		double minTime,farmTime;
		P = 2.0;
		scanf("%lf %lf %lf",&C,&F,&X);
		minTime = X/P;
		farmTime = 0.0; 
	
		while(true){
			farmTime += C/P;
			P+=F;
			
			double timeAtual = farmTime + X/P;
			
			if(timeAtual < minTime){
				minTime = timeAtual;
			}else{
				break;
			}
		}
		
		printf("Case #%d: %.7lf\n",k,minTime);
	}
	
	return 0;
}
