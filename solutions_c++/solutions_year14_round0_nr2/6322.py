#include <iostream>
#include<stdio.h>
int main(){
	int r;
	double c,f,x,tn,tn1;
	freopen("B-large.in", "r", stdin);
	freopen("A-small-practice.out", "w", stdout);
	scanf("%d",&r);
	
	for(int ii=0;ii<r;ii++){
		scanf("%lf %lf %lf",&c,&f,&x);
		tn=x/2;tn1=0;
		for(int n=0;;n++){
			tn1+=c/(2+n*f);
			if(tn>(tn1+x/(2+n*f+f))){
				tn=tn1+x/(2+n*f+f);
			}else{
				printf("Case #%d: %0.7lf\n",ii+1,tn);
				break;
			}
		}
		
	}
}