#include<iostream>
#include<stdio.h>
#include<iomanip>

using namespace std;

int main(){
	int t,cs;
	double c,f,x,tmp,r,sm,pt,t1,t2;
	scanf("%d",&t);
	for(int i=0;i<t;i++){
		pt=0;
		sm=0;
		cs++;
		scanf("%lf %lf %lf",&c,&f,&x);
		r=2;
		while(pt!=x){
			tmp=x/r;
			t1=c/r;
			t2=x/(r+f);
			if((t1+t2)<tmp){
				r+=f;
                sm+=t1;
			}
			else{
				pt=x;
				sm+=tmp;
			}
		}
		printf("Case #%d: %.7lf\n",i+1,sm);
	}
	return 0;
}
