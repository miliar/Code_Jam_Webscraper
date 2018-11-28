#include <iostream>
#include <cstdio>
#include <cmath>
using namespace std;

int main()
{
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
	int NuTest;
	scanf("%d",&NuTest);
	int counter=1;
	double time,divisor;
	while(counter<=NuTest){
		double C,F,X;
		scanf("%lf%lf%lf",&C,&F,&X);
		double min=1000000.0;
		for(int i=1;i<=ceil(X/C);++i){
				time=0;
				divisor=2;
				int j=i;
				while(j>1){
					time+=(C/divisor);
					divisor+=F;
					j-=1; }
				time+=(X/divisor);
				if(time<min)
					min=time;	
					
		}	
		printf("Case #%d: %.7lf\n",counter,min);	
		counter+=1;
	}
}

