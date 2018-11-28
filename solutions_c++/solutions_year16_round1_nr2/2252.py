/*
 * B Small
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
#define N 0x10
#define BIT(k) (1ULL<<(k))
#define MASK(k) (BIT(k)-1ULL)
#define L(k) ((k) & ((~(k))+1ULL))
using namespace std;

int n,cs,ts;
char bts[1<<21];

struct seg {
	int c[N];
	int operator [] ( int i ) const {
		return c[i];
	}
	seg() { memset(c,0,sizeof c); };
};

bool operator < ( const seg &a, const seg &b ) {
	for ( int i = 0; i < n; ++i )
		if ( a[i] != b[i] ) 
			return a[i] < b[i];
	return false ;
}


bool operator == ( const seg &a, const seg &b ) {
	return !(a<b||b<a);
}

seg s[2*N];
vector<seg> rows,cols;
seg t[2*N],cc[N];
char who[1<<21];
int b[N][N];

int main() {
	int i,j,k,l;
	unsigned int u,v,unfilled,used;
	seg res;
	bool ok;
	for ( i = 0; i < 21; ++i )
		who[BIT(i)] = i;
	for ( u = 0; u < (1<<21); ++u )
		bts[u] = bts[u>>1]+(u&1);
	for ( scanf("%d",&ts); ts--; ) {
		printf("Case #%d:",++cs);
		scanf("%d",&n);
		for ( i = 0; i < 2*n-1; ++i ) 
			for ( j = 0; j < n; ++j )
				scanf("%d",&t[i].c[j]);
		for ( ok = false, u = 0; u < (1<<(2*n-1)); ++u ) {
			if ( bts[u] != n ) continue ;
			for ( rows.clear(), cols.clear(), i = 0; i < 2*n-1; ++i ) 
				if ( (u>>i)&1 ) 
					rows.push_back(t[i]);
				else cols.push_back(t[i]);
			sort(rows.begin(),rows.end());
			sort(cols.begin(),cols.end());
			assert ( rows.size() == n );
			assert ( cols.size() == n-1 );
			for ( i = 0; i < n; ++i )
				for ( j = 0; j < n; ++j )
					b[i][j] = rows[i][j];
			for ( j = 0; j < n; ++j )
				for ( i = 0; i < n; ++i )
					cc[j].c[i] = b[i][j];
			for ( used = 0, unfilled = 0, j = 0; j < n; ++j ) {
				for ( v = (~used)&MASK(n-1); v; v &= ~L(v) ) 
					if ( cc[j] == cols[k=who[L(v)]] ) {
						used |= BIT(k);
						goto next;
					}
				unfilled |= BIT(j);
				next:;
			}
			if ( used != MASK(n-1) ) continue ;
			assert( !(unfilled&(unfilled-1)) );
			j = who[unfilled];
			for ( ok = true, i = 0; i < n; ++i )
				res.c[i] = b[i][j];
			break ;
		}
		assert ( ok );
		for ( j = 0; j < n; ++j )
			printf(" %d",res[j]);
		putchar('\n');
	}
	return 0;
}

