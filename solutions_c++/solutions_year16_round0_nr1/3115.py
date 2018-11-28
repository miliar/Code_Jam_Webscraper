/*
 */
#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#define Q (1<<21)
using namespace std;
#include <queue>
typedef long long i64;
#define oo 0xfffffffful
#define enc(t,r) ((t)|(((r)%n)<<1))

i64 n;
char move[Q];
unsigned int d[Q],p[Q];
queue<unsigned int> q;

string dump( unsigned int u ) {
	if ( u == +oo )
		return "";
	return dump(p[u])+(char)(move[u]+'0');
}

string bfs( int dig, int &steps ) {
	int i,j,k;
	unsigned int u,v,rem;
	memset(d,0xff,sizeof d);
	for(;!q.empty();q.pop());
	for ( i = 1; i < 10; ++i )
		if ( i == dig ) {
			if ( d[u = enc(1,i)] == +oo )
				d[u] = 1, q.push(u), p[u] = +oo, move[u] = i;
		}
		else {
			if ( d[u = enc(0,i)] == +oo )
				d[u] = 1, q.push(u), p[u] = +oo, move[u] = i;
		}
	for(;!q.empty();) {
		u = q.front(), q.pop();
		if ( (u&1) && !(u>>1) ) {
			steps = d[u];
			return dump(u);
		}
		for ( i = 0; i < 10; ++i ) {
			rem = ((u>>1)*10+i)%n;
			if ( d[v = enc((u&1)|(i==dig?1:0),rem)] > d[u]+1 )
				d[v] = d[u]+1, q.push(v), move[v] = i, p[v] = u;
		}
	}
	return "";
}

int g( string &a, string &b ) {
	int m = strlen(a.c_str()), n = strlen(b.c_str());
	if ( m != n ) {
		if ( m < n ) return -1;
		return 1;
	}
	for ( int i = 0; i < m; ++i )
		if ( a[i] != b[i] )
			return a[i]<b[i]?-1:1;
	return 0;
}

string s[10],res[10];
int e[10];

string divi( string a ) {
	i64 c[0x400],rem,tmp;
	int i,j,k,m = strlen(a.c_str());
	for ( i = 0; i < m; ++i ) c[i] = a[i]-'0';
	for ( i = 0, j = m-1; i < j; ++i, --j ) 
		k = c[i], c[i] = c[j], c[j] = k;
	for ( rem = 0, i = m-1; i >= 0; --i ) {
		tmp = (rem*10+c[i])%10;
		c[i] = (rem*10+c[i])/10;
		rem = tmp;
	}
	char d[0x400];
	for ( k = m-1; k >= 0 && c[k] == 0; --k );
	if ( k < 0 )
		return "0";
	for ( j = k-1, i = 0; i < k; ++i, --j )
		d[i] = c[j]+'0';
	d[k] = '\0';
	return string(d);
}

int main() {
	int ts,cs = 0,i,j,k;
	string w;
	for ( scanf("%d",&ts); ts-- && 1 == scanf("%lld",&n); ) {
		printf("Case #%d: ",++cs);
		if ( n == 0 ) {
nx:
			puts("INSOMNIA");
			continue ;
		}
		bool ok = true ;
		for ( i = 0; i < 10 && ok; ++i )
			if ( (s[i] = bfs(i,e[i])) == "" ) ok = false ;
		if ( !ok ) goto nx;
		for ( w = s[0], i = 1; i < 10; ++i )
			if ( g(s[i],w) > 0 )
				w = s[i];
		printf("%s\n",w.c_str());
	}
	return 0;
}

