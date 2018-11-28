#include <iostream>
#include <string.h>
#include <stdlib.h>
#include <algorithm>
#include <stdio.h>
using namespace std;
int N , X , arr[10005] , T , C = 1;
int main(){
	freopen("A-large.in","r",stdin);
	freopen("outputA.txt","w",stdout);
	scanf("%d",&T);
	while ( T-- ){
		scanf("%d%d",&N,&X);
		for ( int i = 1 ; i <= N ; i++ )
			scanf("%d",&arr[i]);
		std::sort( arr+1 , arr+N+1 );
		int cnt = 0;
		for ( int i = 1 , j = N ; j >= i ;  ){
			if ( arr[i]+arr[j] <= X ) cnt++ , i++ , j--;	
			else cnt++,j--;
		
		}
		printf("Case #%d: %d\n",C++,cnt);	
	}
	return 0;
}
