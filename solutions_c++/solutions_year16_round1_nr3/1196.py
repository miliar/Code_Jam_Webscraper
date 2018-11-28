/*
 * TOPIC:
 * status:
 */
#include <cassert>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <vector>
#include <algorithm>
#include <set>
#include <map>
#define L(k) ((k) & ((~(k))+1ULL))
#define N 0x10
using namespace std;

int n,f[N],cs,ts,e[N],m,seen[N],yes;
unsigned int mask[N];
char bts[1<<21],who[1<<21];

int visit( int src, int x, int len, unsigned int u ) {
	if ( x == src && len >= 3 ) return 1;
	if ( seen[x] == yes ) return 0;
	seen[x] = yes;
	if ( (u>>f[x])&1 )
		return visit(src,f[x],len+1,u);
	return 0;
};

int all_in_cycle( unsigned int u ) {
	int i,j,k,q[N],*head,*tail;
	for ( m = 0, i = 0; i < n; ++i )
		if ( (u>>i)&1 )
			e[m++] = i;
	for ( k = 0, head = tail = q, seen[*tail++=e[0]]=++yes; head < tail; ) {
		i = *head++, ++k;
		if ( seen[j = f[i]] != yes ) seen[*tail++=j] = yes;
	}
	return k==m;
}

int F( unsigned int u ) {
	int i,j,k;
	for ( i = 0; i < m; ++i ) 
		if ( ++yes && visit(i,i,0,u) ) 
			return 0;
	return 1;
};

int main() {
	unsigned int u,v,nu;
	int i,j,k,w;
	for ( u = 0; u < (1<<21); bts[u] = bts[u>>1]+(u&1), ++u );
	for ( i = 0; i < 21; ++i ) who[1<<i] = i;
	for ( scanf("%d",&ts); ts--; ) {
		scanf("%d",&n);
		for ( i = 0; i < n; ++i ) mask[i] = 0;
		for ( i = 0; i < n; ++i ) {
			scanf("%d",&f[i]), --f[i];
			mask[f[i]] |= (1<<i);
		}
		for ( w = 0, u = 0; u < (1<<n); ++u ) {
			if ( w >= bts[u] ) continue ;
			for ( v = u; v; v &= ~L(v) ) {
				i = who[L(v)], nu = (mask[i]&u);
				if ( !((u>>f[i])&1) || bts[nu]>=3 || (bts[nu]==2&&!((nu>>f[i])&1)) ) goto next;
			}
			if ( all_in_cycle(u) || F(u) ) w = max(w,(int)bts[u]);
			next:;
		}
		printf("Case #%d: %d\n",++cs,w);
	}
	return 0;
}

