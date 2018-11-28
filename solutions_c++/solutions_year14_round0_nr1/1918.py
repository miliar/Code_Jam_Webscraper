#include <stdio.h>
#include <string.h>
#include <stdlib.h>
const int maxn = 5;
int a[ 2 ][ maxn ][ maxn ];
int main(){
	//freopen("in.txt","r",stdin);
	//freopen("out.txt","w",stdout);
	int T;
	scanf("%d",&T);
	int ca = 1;
	while( T-- ){
		int f1,f2;
		scanf("%d",&f1);
		for( int i=1;i<=4;i++ ){
			for( int j=1;j<=4;j++ ){
				scanf("%d",&a[0][i][j]);
			}
		}
		scanf("%d",&f2);
		for( int i=1;i<=4;i++ ){
			for( int j=1;j<=4;j++ ){
				scanf("%d",&a[1][i][j]);
			}
		}
		//
		int cnt = 0;
		int ans ;
		for( int i=1;i<=4;i++ ){
			for( int j=1;j<=4;j++ ){
				if( a[0][f1][i]==a[1][f2][j] ){
					cnt++;
					ans = a[0][f1][i];
				}
			}
		}
		printf("Case #%d: ",ca++);
		if( cnt==0 ) printf("Volunteer cheated!\n");
		else if( cnt==1 ) printf("%d\n",ans);
		else printf("Bad magician!\n");
	}
	return 0;
}
