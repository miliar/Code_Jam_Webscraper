#include <cstdio>
#include <iostream>
#include <vector>
using namespace std;

const int max_n=105;

int HighR[max_n], HighC[max_n];
int H[max_n][max_n];

int i, j;
int T, t, n, m;

void make_empty(){
	for( int i=0; i<max_n; ++i ){
		HighC[i]=HighR[i]=0;
	}
}

void get_max( int &a, int b ){
	if( a<b )
		a=b;
}

int main(){
	freopen("date.in","r",stdin);
	freopen("date.out","w",stdout);

	scanf("%d", &T );
	for( t=1; t<=T; ++t ){
		scanf("%d %d", &n, &m );
		for( i=1; i<=n; ++i )
			for( j=1; j<=m; ++j ){
				scanf("%d", &H[i][j] );
				get_max( HighR[i], H[i][j] );
				get_max( HighC[j], H[i][j] );
			}
		bool ok=true;
		for( i=1; i<=n; ++i )
			for( j=1; j<=m; ++j )
				if( HighR[i] == H[i][j] || HighC[j] == H[i][j] )
					;
				else
					ok=false;
		if( ok )
			printf("Case #%d: YES\n", t);
		else
			printf("Case #%d: NO\n", t);
		make_empty();
	}
	return 0;
}
