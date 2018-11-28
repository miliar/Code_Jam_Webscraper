#include <stdio.h>
#include <string.h>
int T , N , M , map[105][105] , C = 1;
bool wrong;

int main(){
	freopen("B-large.in","r",stdin);
	freopen("output.txt","w",stdout);
	scanf("%d",&T);
	while ( T-- ){
		scanf("%d%d",&N,&M);
		wrong = 0;
		for ( int i = 1 ; i <= N ; i++ )
			for ( int j = 1 ; j <= M ; j++ )
				scanf("%d",&map[i][j]);
		for ( int i = 1 ; i <= N && !wrong ; i++ )
			for ( int j = 1 ; j <= M ; j++ ){
				bool flag = true;
				for ( int x = 1 ; x <= M ; x++ )
					if ( map[i][x] > map[i][j] )
						flag = false;
				if ( !flag ){
					flag = true;
					for ( int x = 1 ; x <= N ; x++ )
						if ( map[x][j] > map[i][j] )
							flag = false;
				}
				if ( !flag ) wrong = true;
				
			}

		if ( !wrong ) printf("Case #%d: YES\n",C++);
		else printf("Case #%d: NO\n",C++);
	}

	return 0;
} 
