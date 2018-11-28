#include<iostream>
#include<cstring>
#include<string>
#include<cstdio>
#include<stdio.h>
#include<algorithm>
#include<cmath>
#include<set>
#include<map>
#include<queue>
using namespace std;


#define inf 0x3f3f3f3f
#define eps 1e-9
#define mod 1000000007
#define FOR(i,s,t) for(int i = s; i < t; ++i )
#define REP(i,s,t) for( int i = s; i <= t; ++i )
#define ULL unsigned long long
#define pii pair<int,int>
#define MP make_pair
#define lson id << 1 , l , mid
#define rson id << 1 | 1 , mid + 1 , r 
#define N ( 200000+100 )
#define M ( 200000+10 )

int a[N];
char s[N];
int g[11][11];

void init () {
	for( int i = 1; i <= 4; ++i )
		g[1][i] = g[i][1] = i;
	for( int i = 2; i <= 4; ++i )
		g[i][i] = 5;
	g[2][3] = 4, g[2][4] = 7;
	g[3][2] = 8, g[3][4] = 2;
	g[4][2] = 3, g[4][3] = 6;
}

int mul ( int a, int b ) {
	int tmp = 0;
	if( a > 4 ) a -= 4, tmp ^= 1;
	if( b > 4 ) b -= 4, tmp ^= 1;
	int c = g[a][b];
	if( c > 4 ) c -= 4, tmp ^= 1;
	if( tmp ) return c + 4;
	else return c;
}

int sum[N];

void build( int id, int l, int r ) {
	if( l == r ) {
		sum[id] = a[l];
		return ;
	}
	int mid = l + r >> 1;
	build( lson ), build( rson );
	sum[id] = mul( sum[id<<1], sum[id<<1|1] );
}

int query( int id, int l, int r, int ll, int rr ) {
	if( ll == l && rr == r ) {

		return sum[id];
	}
	int mid = l + r >> 1;
	if( rr <= mid ) return query( lson , ll, rr );
	else if( ll > mid ) return query( rson, ll, rr );
	else return mul( query( lson, ll, mid ), query( rson, mid + 1, rr ) );
}

void change ( int L ) {
	for( int i = 0; i < L; ++i ) {
		if( s[i] == '1' ) a[i] = 1;
		if( s[i] == 'i' ) a[i] = 2;
		if( s[i] == 'j' ) a[i] = 3;
		if( s[i] == 'k' ) a[i] = 4;
	}
}

vector < int > isi, isk;
bool gao ( int L ) {
	isi.clear();
	isk.clear();
	int w = 1;
	for( int i = 0; i < L; ++i ) {
		w = mul( w, a[i] );
		if( w == 2 ) isi.push_back( i );
	}
	w = 1;
	for( int i = L-1; i >= 0; --i ) {
		w = mul( a[i], w );
		if( w == 4 ) isk.push_back( i );
	}
	build( 1, 0, L-1 );
	for( int i = 0; i < isi.size(); ++i ) {
		for( int j = 0; j < isk.size(); ++j ) {
			int l = isi[i], r = isk[j];
			if( r - 1 < l + 1 ) break;
			if( query( 1, 0, L -1 , l + 1, r - 1 ) == 3 ) return 1;
		}
	}
	return 0;
}

int main () {
	freopen( "in.in", "r", stdin );
	freopen( "out.out", "w", stdout );
	init();
	int T, cas = 1;
	scanf("%d", &T );
	while( T-- ) {
		int X, L;
		scanf("%d%d", &L, &X );
		scanf("%s", s );
		int tmp = L;
		while( 1 ) {
			--X;
			if( X <= 0 ) break;
			for( int i = L; i < L + tmp; ++i ) 
				s[i] = s[i-tmp];
			L += tmp;
		}
		change( L );
		printf("Case #%d: ", cas ++ );
		if( gao ( L )) puts("YES");
		else puts("NO");
	}
}
