#include<stdio.h>
#include<algorithm>
using namespace std;
int main()
{
	int t,test;
	double C,F,X,prev,curr,A,D;
	double two=2;
	scanf("%d",&t);
	for(test=1;test<=t;test++){
		scanf("%lf%lf%lf",&C,&F,&X);
		prev=X/two;
		A=0;
		for(int s=0;;s++){
			D=F*s+two;
			A=A+C/D;
			D=D+F;
			curr=A+X/D;
			if(curr>prev){
				break;
			}
			else{
				swap(prev,curr);
			}
		}
		printf("Case #%d: %.7lf\n",test,prev);
	}
	return 0;
}
