#include<bits/stdc++.h>
using namespace std;

int n;
int ar[1005];

int main(){

	freopen( "input.txt"  , "r" , stdin );
	freopen( "output.txt" , "w" , stdout);
	int id,test,i,j,cnt,ans;
	
	scanf( "%d\n" , &test );
	
	for( id=1 ; id<=test ; id++ ){
	
		scanf( "%d" , &n );
		for( i=1 ; i<=n ; i++ )		scanf( "%d" , ar+i );
		
		ans = 1e9;
		
		for( i=1 ; i<=1000 ; i++ ){
		
			cnt=0;
			for( j=1 ; j<=n ; j++ )		cnt += (ar[j]-1)/i;
			ans = min( ans,cnt+i );		
			
		}
		
		printf( "Case #%d: %d\n" , id , ans );
		
	}
	
	return 0;
}
