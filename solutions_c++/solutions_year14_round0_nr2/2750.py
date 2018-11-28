
#include<stdio.h>
#include<cstdlib>
#include<iostream>
#include<fstream>
 double min(  double ma ,  double b) 
{
	return ma<b?ma:b;
}
int main()
{
	int t,count=1;
	freopen("B-large.in","r",stdin);
	freopen("ku2.txt","w",stdout);
	scanf("%d",&t);
	while( t--){
		 double c,x,n,k1,k2,f,ans;
		int i,j,l;
		scanf("%lf%lf%lf",&c,&f,&x);
		 double frst=0.0,last=0.0,prev=0.0,tim=0.0,tim1=0.0;
		frst = (x/2.0)*(1.0);
		last =2.0;
		while( 1 ){
			tim += (c/last)*(1.0);
			last+=f;
			k1 = (x/last)*(1.0);
			k2 = ((c/(last))*(1.0) + (x/(last+f)) *(1.0));
			if( k1 < k2 ) {
				ans = tim + k1;
				break;
				
			} else{ 
			
				continue;
			}
			
		
			 
		}
		 double a1,a2;
		a1 = min( ans , frst );
		printf("Case #%d: %.7lf\n",count++,a1);
		
		
	}
	fclose(stdin);
	fclose(stdout);
	return 0;
}
