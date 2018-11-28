#include <stdio.h>
#include <stdlib.h>
#include <vector>
#include <iostream>
using namespace std;

int main(){
	int t;scanf("%d",&t);
	for(int i=1;i<=t;i++){
		double c,f,x,f1=2.0;
		scanf("%lf %lf %lf",&c,&f,&x);
		double tim=0.0;
		bool b=true;
		while(b){
			if(x/f1 > (c/f1)+(x/(f1+f))){
				tim+=c/f1;
				f1+=f;
				b=true;
			}
			else{
				tim+=x/f1;
				b=false;
				printf("Case #%d: %f\n",i,tim);
			}
		}
	}
}
