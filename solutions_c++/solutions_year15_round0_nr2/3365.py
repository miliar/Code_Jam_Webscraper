#include <stdio.h>
#include <string.h>
#include <algorithm>
using namespace std;
int T, N, plate[1001]; 
int buf[ 1001 ];
int getStep( int food , int limit ){
	if ( buf[food] != -1 ) return buf[ food ];
	if ( food <= limit ) return buf[food] = 0;
	int smallest = (int)1e9;
	for ( int i = limit ; i < food ; i++ )
		smallest = min( smallest , getStep( i, limit ) + getStep( food-i , limit ) + 1 );
	return buf[food] = smallest;
	
}
int main(){
	freopen("B-large.in","r",stdin);
	freopen("B-output.out","w",stdout);

	int casen = 1;
	scanf("%d",&T);
	while ( T-- ){
		
	
		scanf("%d",&N);
		for ( int i = 1 ; i <= N ; i++ )
			scanf("%d",&plate[i]);
		
		int ans = ( int ) 1e9;
		
		for ( int limit = 1 ; limit <= 1000 ; limit++ ){
			int step = limit;
			memset( buf , -1 , sizeof( buf ) );
			for ( int j = 1 ; j <= N ; j++ )	
				step += getStep( plate[j] , limit );
			
			if ( step < ans )
				ans = step;

		}
		printf("Case #%d: %d\n",casen++,ans);
	
	}
	return 0;
}
