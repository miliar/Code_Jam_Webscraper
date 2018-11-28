#include <bits/stdc++.h>
using namespace std;

int T,N;
char ar[5][5];
int a[5], b[5];
int main(){
	cin>>T;
	for(int t=1; t<=T; t++){
		cin>>N;
		for(int i=0; i<N; i++)
			cin>>ar[i];
		for(int i=0; i<N; i++) a[i] = b[i] = i;
		int ans = 987654321;
		do{
			do{
				int br[5][5]={0,}, sm[5];
				for(int i=0; i<N; i++){
					for(int j=0; j<N; j++){
						br[i][j] = ar[ a[i] ][ b[j] ] == '1';
//						printf("%d ",br[i][j]);
					}
					sm[i] = i;
//					printf("\n");
				}
				int c = 0;
				for(int i=0; i<N; i++){
					if( br[i][i] == 0 ) { c++; br[i][i] = 1; }
					int l = i;
					for(int j=0; j<=i; j++)
						if( br[i][j] || br[j][i] ){
							for(int k=j; k<=i; k++)
								l = min( l, sm[k] );
							break;
						}
					sm[i] = l;
					for(int j=l; j<=i; j++)
						for(int k=l; k<=i; k++){
							if( br[j][k] == 0 ) { c++; br[j][k] = 1; }
						}
				}
				if( ans > c && 0 ){
					for(int i=0; i<N; i++){
						for(int j=0; j<N; j++)
							printf("%d ", br[i][j] );// ar[a[i]][b[j]] == '1');
						printf("\n");
					}
				}
				ans = min( ans, c );
			}while( next_permutation( b, b+N) );
		}while( next_permutation( a, a+N ) );
		printf("Case #%d: %d\n",t,ans);
	}
	return 0;
}
