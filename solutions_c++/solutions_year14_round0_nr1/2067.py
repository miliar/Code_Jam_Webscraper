#include <stdio.h>
#include <string.h>
int T , r , map[5][5] , C = 1;
bool app[17];
int main(){
	freopen("A-small-attempt0.in","r",stdin);
	freopen("output.out","w",stdout);
	scanf("%d",&T);
	while ( T-- ){
		int cnt = 0 , ptr;
		memset( app , 0 , sizeof( app ) );
		for ( int Ecx = 1 ; Ecx <= 2 ; Ecx++ ){
			scanf("%d",&r);
			for ( int i = 1 ; i <= 4 ; i++ )
				for ( int j = 1 ; j <= 4 ; j++ )
					scanf("%d",&map[i][j]);
			for ( int i = 1 ; i <= 4 ; i++ ){
				if ( !app[map[r][i]] )
					app[map[r][i]] = true;
				
				else{
					cnt++;
					ptr = map[r][i];
				}
			}
		}
		if ( cnt > 1 ) 
			printf("Case #%d: Bad magician!\n",C++);
		else if ( cnt < 1 ) 
			printf("Case #%d: Volunteer cheated!\n",C++);
		else
			printf("Case #%d: %d\n",C++,ptr);
	}
	return 0;
}
