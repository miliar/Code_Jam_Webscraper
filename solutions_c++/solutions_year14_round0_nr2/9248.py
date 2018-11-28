#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
using namespace std;
double C,F,X,Min;
int main() {
	int T;
	scanf("%d",&T);
	for (int i=1;i<=T;i++){
		 bool cont=1;
		 double cap=2;
		 cin>> C >> F >> X ;
		 Min=0;
		 while(cont){
		 	double MinO= (X/cap);
		 	if (  MinO > (C/cap)+ (X/(cap+F)) ) 	{
		 		Min= Min + (C/cap);
		 		cap=cap+F;cont=true;
		 		}
		 	else {
		 		cont=false; Min=Min+MinO ;
		 	}
		 }
		 printf("Case #%d: %f\n",i,Min); 
	}
	return 0;
}