#include <stdio.h>
int T, N;
char G[1005];
int main(){
	freopen("A-large.in","r",stdin);
	freopen("A-output.out","w",stdout);
	int casen = 1;
	scanf("%d",&T);
	while ( T-- ){
		scanf("%d",&N);
		scanf("%s",G);
		int clap = G[0]-'0' , ans = 0;		
		for ( int i = 1 ; i <= N; i++ ){
			int people = G[i] - '0';
			if ( people == 0 ) continue;
			if ( clap < i )
				ans += i - clap , clap = i;
			clap += people;
		}
		printf("Case #%d: %d\n",casen++,ans);
		
	}
	return 0;
}
