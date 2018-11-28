#include <iostream>
#include<stdio.h>
using namespace std;

int main() {
	// your code goes here
	int t=1,T,farms;
	float C,F,X,time=0.0;
	scanf("%d",&T);
	while(t<=T)
	{
		time=0.0;
		scanf("%f %f %f",&C,&F,&X);
		farms=(X/C)-(2.0/F);
		if(farms<0) farms=0;
		for(int i=1;i<=farms;i++)
		time=time+(C/(2+(i-1)*F));
		time=time+(X/(2+farms*F));
		printf("Case #%d: %.07f\n",t,time);
		t++;
	}
	return 0;
}
