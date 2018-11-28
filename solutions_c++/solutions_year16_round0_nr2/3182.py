/*
 */
#include <cassert>
#include <iostream>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <queue>
#include <set>
using namespace std;
#define MASK(k) (BIT(k)-1ULL)
#define BIT(k) (1ULL<<(k))
#define Q BIT(21)
#define enc(x,y,k) ((x)|((y)<<6)|((k)<<12))
#define target enc(0,1,1)

unsigned int d[Q];
queue<unsigned int> q;

unsigned int 
bfs( unsigned int src, int N ) {
	unsigned int u,v;
	int m,n,i,j,k;
	memset(d,0xff,sizeof d);
	for ( q.push(src), d[src] = 0; !q.empty(); ) {
		u=q.front(),q.pop(),m=(u&MASK(6)),n=((u>>6)&MASK(6)),k=(u>>12);
		if ( u == target ) break ;
		for ( i = 0; i < m+n-1; i += 2 ) 
			if ( m-(k^1) >= 0 && n-k >= 0 && d[v = enc(m-(k^1),n-k,k^1)] > d[u]+1 )
				d[v] = d[u]+1, q.push(v);
		if ( 1 == ((m+n)&1) ) 
			if ( d[v = enc(n,m,k^1)] > d[u]+1 )
				d[v] = d[u]+1, q.push(v);
	}
	for(;!q.empty();q.pop());
	return d[target];
}

unsigned int conv( char *s ) {
	int i,j,k,l = strlen(s),c[2] = {0};
	for ( i = 0; i < l; ++i )
		if ( s[i] == '+' ) s[i] = '1';
		else s[i] = '0';
	for ( i = 0; i < l; ++c[s[i]-'0'], i = j ) 
		for ( j = i+1; j < l && s[i] == s[j]; ++j );
	return enc(c[0],c[1],s[0]-'0');
}

int main() {
	int i,j,k,ts,cs = 0;
	char s[0x400];
	for ( scanf("%d",&ts); ts--; scanf("%s",s), k=strlen(s), printf("Case #%d: %u\n",++cs,bfs(conv(s),k)) );
	return 0;
}

