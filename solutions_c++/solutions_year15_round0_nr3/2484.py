#include <iostream>
#include <algorithm>
#include <cstdio>
#include <cstdlib>

using namespace std;

int T,N,K;
int as[5][5];
int ar[10100];
int pre[10100];
int P[10100];

int main(){
	
	as[1][1]=1;
	as[1][2]=2;
	as[1][3]=3;
	as[1][4]=4;
	as[2][1]=2;
	as[2][2]=-1;
	as[2][3]=4;
	as[2][4]=-3;
	as[3][1]=3;
	as[3][2]=-4;
	as[3][3]=-1;
	as[3][4]=2;
	as[4][1]=4;
	as[4][2]=3;
	as[4][3]=-2;
	as[4][4]=-1;

	cin >> T;
	for( int z=1 ; z<=T ; z++ ){
		cin >> N >> K;
		char c;
		int ff=0;
		for( int i=1 ; i<=N ; i++ ){
			scanf(" %c",&c);
			if( c == 'i' ) ar[i]=2;
			if( c == 'j' ) ar[i]=3;
			if( c == 'k' ) ar[i]=4;
		}
		for( int q=1,i=N+1 ; q<K ; q++ )
			for( int j=1 ; j<=N ; j++ , i++ ) ar[i]=ar[j];
		int tt=1,gg=0;
		for( int i=N*K ; i ; i-- ){
			tt=as[ar[i]][tt];
			if( tt < 0 ) tt=-tt,gg=!gg;
			pre[i]=tt; P[i]=gg;
		}
		tt=1,gg=0;
		for( int i=1 ; i<=N*K ; i++ ){
			tt=as[tt][ar[i]];
			if( tt < 0 ) tt=-tt,gg=!gg;
			if( tt == 2 && !gg ){
				int ttt=1,ggg=0;
				for( int j=i+1 ; j<N*K ; j++ ){
					ttt=as[ttt][ar[j]];
					if( ttt < 0 ) ttt=-ttt,ggg=!ggg;
					if( pre[j+1] == 4 && !P[j+1] && ttt== 3 && !ggg ) ff=1;
				}
			}
		}
		printf("Case #%d: ",z);
		if( ff ) printf("YES\n");
		else printf("NO\n");
	}
	

}