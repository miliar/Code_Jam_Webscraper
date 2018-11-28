#include<iostream>
using namespace std;
int main(){
	int t;
	double c,f,x,withOutFarmPurchaceTime,withFarmPurchaceTime,totalTime = 0.0,ccRate = 2.0;
	
	scanf("%d",&t);
	
	for(int i = 1;i<=t;i++){
		scanf("%lf%lf%lf",&c,&f,&x);
		totalTime = 0.0;
		ccRate = 2.0;
	  while(1){
	  
		withOutFarmPurchaceTime = x/ccRate;
		
		withFarmPurchaceTime = (c/ccRate) + x/(ccRate+f);
		
		if(withFarmPurchaceTime < withOutFarmPurchaceTime){
			totalTime += c/ccRate;
			ccRate += f;
		}
		else{
			totalTime += x/ccRate;
			break;
		}
   	}
   	 
   	 printf("Case #%d: %.12lf\n",i,totalTime);
		
	}
	
}
