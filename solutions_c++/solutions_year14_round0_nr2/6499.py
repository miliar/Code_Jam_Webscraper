#include <stdio.h>

int main(){
  int nTestCases =0;
  scanf("%d",&nTestCases);
  for(int i=0;i<nTestCases;++i){
	double c,f,y;
	scanf("%lf %lf %lf",&c,&f,&y);
	double oldSeconds=y/2;
	double curSeconds=oldSeconds;
	//double tempSeconds=oldSeconds;
	int j=1;
	do{
	  oldSeconds=curSeconds;
	  curSeconds = oldSeconds + (y/(j*f+2) + (c-y)/((j-1)*f + 2));
	  ++j;
	}while(oldSeconds > curSeconds);
	//printf("%d ",j);
	printf("Case #%d: %.7lf\n",i+1,oldSeconds);
  }
}
