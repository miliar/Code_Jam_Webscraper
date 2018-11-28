#include<cstring>
#include<set>
#include<stdio.h>
#include<cstdlib>
#include<iostream>
#include<fstream>
 double minimum(  double x ,  double y) 
{
	return x<y?x:y;
}
int main()
{
	int test,count=1;
	freopen("B-large .in","r",stdin);
	freopen("pad2.txt","w",stdout);
	scanf("%d",&test);
	while( test--){
		 double C,X,K1,K2,F,ans;
		int i,j,l,p;
		scanf("%lf%lf%lf",&C,&F,&X);
		double first=0.0,lst=0.0,prv=0.0,ti=0.0,ti1=0.0;
		first = (X/2.0)*(1.0);
		lst =2.0;
		while( 1 ){
			ti  += (C/lst)*(1.0);
			lst +=F;
			K1 = (X/lst)*(1.0);
			K2 = ((C/(lst))*(1.0) + (X/(lst+F)) *(1.0));
			if( K1 < K2 ) {
				ans = ti + K1;
				break;
				
			} else{ 
			
				continue;
			}
			
		
			 
		}
		double ans2,a2;
		ans2 = minimum( ans , first );
		printf("Case #%d: %.7lf\n",count++,ans2);
		
		
	}
	fclose(stdin);
	fclose(stdout);
	return 0;
}
