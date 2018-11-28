/*
 *
 * TOPIC:
 * status:
 */
#include <cassert>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <vector>
#define xchg(x,y) (((x)==(y))||((x)^=(y),(y)^=(x),(x)^=(y)))
#define bubble (xchg(pos[heap[i]],pos[heap[j]]),xchg(heap[i],heap[j]))
using namespace std;
#define N (1<<21)

int pos[N],heap[N],cn,d[N],p[N],n,total;

void push( int x ) {
	int i,j,k;
	if ( pos[x] < 0 )
		pos[heap[cn]=x]=cn, ++cn;
	for ( j = pos[x]; j && d[heap[i=(j-1)>>1]] < d[heap[j]]; bubble, j = i );
}

int pop() {
	int i,j,x = *heap;
	if ( cn += (pos[x]=-1) )
		pos[*heap=heap[cn]] = 0;
	for ( j = 0; (i=j,j<<=1,++j) < cn; bubble ) {
		if ( j<cn-1 && d[heap[j+1]] > d[heap[j]] ) ++j;
		if ( d[heap[i]] >= d[heap[j]] ) break ;
	}
	return x;
}

bool valid() {
	int w = -N,i,j,k,s;
	for ( i = 0; i < n; ++i )
		if ( d[i] > w ) w = d[k=i];
	for ( s = 0, i = 0; i < n; ++i )
		if ( i != k ) s += d[i];
	return s >= w;
}

int main() {
	int i,j,k,ts,cs = 0;
#ifndef ONLINE_JUDGE
	freopen("large.in","r",stdin);
#endif
	for ( scanf("%d",&ts); ts--; ) {
		scanf("%d",&n), memset(pos,-1,sizeof pos), cn = 0;
		for ( total = 0, i = 0; i < n; ++i ) 
			scanf("%d",d+i), push(i), total += d[i];
		printf("Case #%d:",++cs);
		while ( cn ) {
			assert( cn >= 2 );
			assert( valid() );
			i = pop(), j = pop();
			assert( d[i] >= d[j] );
			if ( d[i] == d[j] ) {
				if ( cn == 0 ) {
					printf(" %c%c",i+'A',j+'A');
					total -= 2;
			   		if ( --d[i] ) push(i);
					if ( --d[j] ) push(j);
					continue ;
				}
				else {
					push(j), printf(" %c",i+'A');
					--total;
					if ( --d[i] ) push(i);
					continue ;
				}
			}
			if ( d[i] == d[j]+1 ) {
				push(j), --total;
				printf(" %c",i+'A');
				if ( --d[i] ) push(i);
				continue ;
			}
			assert( d[i] >= d[j]+2 );
			push(j);
			printf(" %c%c",i+'A',i+'A');
			total -= 2;
			if ( d[i] -= 2 ) push(i);
		}
		putchar('\n');
	}
	return 0;
}

