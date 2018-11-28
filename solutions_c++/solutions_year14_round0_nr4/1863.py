#include <stdio.h>
#include <string.h>
#include <algorithm>
int T , N;
double Nao[1001] , Ken[1001];
int Cheat(){
	int cnt = 0 , lptr = 1;
	for ( int i = 1 ; i <= N; i++ )
		if ( Nao[i] > Ken[lptr] )
			cnt++ , lptr++;	
	return cnt;
}
int Normal(){
	int rptr = N , cnt = 0;
	for ( int i = N ; i >= 1 ; i-- ){
		if ( Ken[rptr] >= Nao[i] ) rptr--;
		else cnt++;	
	}
	return cnt;
}
int main(){
	freopen("D-large.in","r",stdin);
	freopen("outputD.out","w",stdout);
	int C = 1;
	scanf("%d",&T);
	while ( T-- ){
		scanf("%d",&N);
		for ( int i = 1 ; i <= N ; i++ )
			scanf("%lf",&Nao[i]);
		for ( int i = 1 ; i <= N ; i++ )
			scanf("%lf",&Ken[i]);	
		std::sort( Nao+1 , Nao+N+1 );
		std::sort( Ken+1 , Ken+N+1 );
		printf("Case #%d: %d %d\n", C++,Cheat(),Normal());

	}
	
	return 0;	
}
