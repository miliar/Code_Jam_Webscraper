#include <cstdio>
#include <algorithm>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <queue>
#define N 11
#define Q (1<<N)
#define oo (0xfffffffful)
#define BIT(k) (1ULL<<(k))
#define MASK(k) (BIT(k)-1ULL)
using namespace std;

unsigned int d[Q],q[Q],*head,*tail;
int K,n;

int main() {
	int i,j,k,ts,cs = 0;
	unsigned int u,v;
	char s[0x400];
	for ( scanf("%d",&ts); ts-->0; ) {
		for ( scanf("%s %d",s,&K), u = 0, n = 0; s[n]; ++n )
			if ( s[n] == '+' ) u |= BIT(n);
		for ( memset(d,0xff,sizeof d), d[u] = 0, head=tail=q, *tail++ = u; head < tail; )
			for ( u = *head++, i = 0; (j = i+K-1) < n; ++i ) 
				if ( d[v = (u^(MASK(K)<<i))] > d[u]+1 )
					d[*tail++ = v] = d[u]+1;
		printf("Case #%d: ",++cs);
		if ( d[MASK(n)] < +oo )
			printf("%u\n",d[MASK(n)]);
		else puts("IMPOSSIBLE");
	}
	return 0;
}

