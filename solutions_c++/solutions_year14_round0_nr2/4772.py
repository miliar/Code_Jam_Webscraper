#include <cstdio>
#include <iostream>

using namespace std;

double cost[10000] ;

int main(){
	
	int T , CASE = 0 ; 
	scanf("%d",&T) ;
	while( T-- ){
		double c , f , x ; 
		cin >> c >> f >> x ; 
		
		cost[0] = 2 ;	
		double ans = x / cost[0]; 
		//double tmp = 0;
		int add = 1 ;
		while( 1 ){
			double buySecond = 0 ;
			for(int i=0;i<add;++i)
			 	buySecond += ( c / cost[i] )  ;	
			cost[add] = cost[add-1] + f ; 
			buySecond += x / ( cost[add] ) ; 
			add++ ;
			
			//printf("%lf\n",buySecond);
			
			if( buySecond <= ans )	ans = buySecond ; 
			else break; 		
		}
		printf("Case #%d: %.7lf\n",++CASE,ans);
	}	
	
	return 0; 	
}
