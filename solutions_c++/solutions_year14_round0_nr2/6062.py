#include <stdio.h>

int casos;
double c,x,f,timeX,timeTX,timeC,timeTC,timeA,tf;

int main(){
	freopen("in.txt","r",stdin);
	scanf("%d",&casos);
	for(int i = 0;i < casos;i++){
		tf = 0;
		scanf("%lf %lf %lf",&c,&f,&x);
		timeX = x/(2+tf);
		timeC = c/(2+tf);
		timeTX = timeX;
		timeTC = timeC;
		timeA = 100000000;
		while(timeA > timeTX){
			tf += f;
			timeA = timeTX;
			timeX = x/(2+tf);
			timeC = c/(2+tf); 
			timeTX = timeTC + timeX;
			timeTC += timeC;
		}
		printf("Case #%d: %.7lf\n",i+1,timeA);
	}
	return 0;
}
