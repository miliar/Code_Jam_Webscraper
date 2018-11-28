#include <iostream>
#include <assert.h>
using namespace std;
bool fast(double c,double f,double x,double rate){
	if(x/(rate+f)+c/rate <= x/rate)
		return true;
	else
		return false;}
int main(void) {
	int m,n,i,j,farm=0;
	double c,f,x,rate=2,time=0;
	FILE *fp;
	scanf("%d",&n);
	fp=fopen("ans","w");
	assert(fp!=NULL);
	for(m=0;m<n;m++){
		time=0;
		rate=2;
		farm=0;
		cin>>c;
		cin>>f;
		cin>>x;
		while(fast(c,f,x,rate)){
			time += c/(2+f*farm);
			rate += f;
			farm++;
		}
		time += x/(2+f*farm);
		printf("Case #%d: %.7f\n",m+1,time);
		fprintf(fp,"Case #%d: %.7f\n",m+1,time);
	}
}
