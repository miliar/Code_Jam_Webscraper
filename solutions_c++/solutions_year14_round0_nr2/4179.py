#include <iostream>
#include <string>
#include <string.h>
#include <stdio.h>
#include <queue>
#include <map>
#include <stack>
#include <vector>
#include <algorithm>
using namespace std;
double C,F,X;
int main(){

	freopen("B-large.in","r",stdin);
	freopen("output23.out","w",stdout);

	
	int t;
	
	scanf("%d",&t);
	
	
	for(int c=0;c<t;c++){
		scanf("%lf %lf %lf",&C,&F,&X);
		
		if(X<=C){
			printf("Case #%d: %.07lf\n",c+1,X/2.0);
		}else{
		
			double t=C/2.0;
			double can=C;
			double div=2.0;
			double res=X-can;
			while(true){
				double tn=res/div;
				double tm=X/(div+F);
				
				if(tn<tm){
					t=t+tn;
					break;
				}else{
					div=div+F;
					t=t+C/div;
				}
				
			}
		
			printf("Case #%d: %.07lf\n",c+1,t);
		
		
		}
		
		
		
		
	}
	
	
}