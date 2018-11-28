/*
 * By Duck
 */

#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <algorithm>

const int N = 110;

struct PCK{
	int x, y, h;
};
int comp(PCK a, PCK b) {
	return a.h<b.h;
}

int n, m;
int mp[N][N], vis[N][N];
PCK tos[N*N];


int ifok() {
	int cnt = 0, flg;
	for( int i=0; i<n; i++ ) for( int j=0; j<m; j++ ) {
		tos[cnt].x=j;  tos[cnt].y=i;  tos[cnt].h=mp[i][j];
		cnt++;
		vis[i][j] = 0;
	}
	std::sort(tos, tos+cnt, comp);
	
	for( int k=0; k<cnt; k++ )
		if( !vis[tos[k].y][tos[k].x] ) {
			flg = 0;
			for( int i=0; i<n; i++ )
				if( mp[i][tos[k].x]>tos[k].h ) 
					flg = 1;
			if( flg<1 )
				for( int i=0; i<n; i++ )
					vis[i][tos[k].x] = 1; 
			for( int j=0; j<m; j++ ) {
				if( mp[tos[k].y][j]>tos[k].h && (flg&1) )
					return 0;
				else if( mp[tos[k].y][j]>tos[k].h )
					flg |= 2;
			}
			if( !(flg&2) ) 
				for( int j=0; j<m; j++ )
					vis[tos[k].y][j] = 1; 
		}
	return 1;
}

int main(){
	int t;
	scanf("%d", &t);
	for( int r=1; r<=t; r++ ) {
		printf("Case #%d: ", r);
		scanf("%d %d", &n, &m);
		for( int i=0; i<n; i++ ) for( int j=0; j<m; j++ )
			scanf("%d", &mp[i][j]);
		printf("%s\n", ifok()?"YES":"NO");
	}
}

