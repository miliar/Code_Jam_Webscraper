#include <bits/stdc++.h>
using namespace std;

#define fr(a,b,c) for( int a = b ; a < c ; ++a )
#define si(x) scanf("%d", &x)

int a,n, t[111];
int pd[101][1000001];
int go(int x, int y) {
	if( y > 1000000 ) return 0;
	if( x == n ) return 0;
	if( ~pd[x][y] ) return pd[x][y];
	
	if( t[x] < y ) return pd[x][y] = go(x+1,y+t[x]);
	else return pd[x][y] = min(n-x, 1+go(x,y+y-1));
}

int main() {
	int tc, caso = 1;
	si(tc);
	while( tc--  ){
		printf("Case #%d: ", caso++);
		si(a), si(n);
		fr(i,0,n) si(t[i]);
		sort(t,t+n);
		if( a == 1 ) {
			printf("%d\n", n);
		} else {
			memset(pd,-1,sizeof pd);
			printf("%d\n", go(0,a));
		}
		cerr << tc << endl;
	}
	return 0;
}

