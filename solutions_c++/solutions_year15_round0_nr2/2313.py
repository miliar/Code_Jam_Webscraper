#include<bits/stdc++.h>
 
using namespace std;

#define 	INF 		(int(1e9))
#define N	5010

int P[N];

int main(){
	#ifndef ONLINE_JUDGE
		freopen("in.txt","r",stdin);
		freopen("out.txt","w",stdout);
	#endif
	int T,D;
	scanf("%d",&T);
	for( int qq = 1 ; qq <= T ; qq++ ){
		
		scanf("%d",&D);
		
		int maxx = 0;
		
		for( int i = 0 ; i < D ; i++ ){
			scanf("%d",&P[i]);
			maxx = max( maxx , P[i] );
		}
		
		int ans = INF;
		
		for( int i = 1 ; i <= maxx ; i++ ){
			int cur = 0;
			for( int j = 0 ; j < D ; j++ ){
				cur += (P[j] - 1)/i;
			}
			cur += i;
			ans = min( ans , cur );
		}
		
		printf("Case #%d: %d\n",qq,ans);
	}
	return 0;
}       
