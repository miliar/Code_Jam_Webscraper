#include <bits/stdc++.h>
using namespace std;

#define fr(a,b,c) for( int a = b ; a < c ; ++a )
#define si(x) scanf("%d", &x)

struct T {
	int x[26];
	bool f;
	T(): f(false) { memset(x,-1,sizeof x); }
} t[1125080];
int ult = 1;

#define N 1125080

char str[1<<15];
int pd[1125080][60][5];
int go(int x, int y, int z) {
	if( !str[y] ) return t[x].f ? 0 : 100000;
	if( ~pd[x][y][z] ) return pd[x][y][z];
	
	int ret = 100000;
	if( t[x].f ) ret = go(0,y,z);
	
	if( z == 0 ) {
		fr(i,0,26) {
			if( ~t[x].x[i] ) {
				ret = min(ret, go(t[x].x[i], y+1, 4)+1);
			}
		}
	}
	if( ~t[x].x[ str[y]-'a' ] ) {
		ret = min(ret, go(t[x].x[ str[y]-'a' ], y+1, z?z-1:0));
	}
	return pd[x][y][z] = ret;
}

typedef pair<int,int> pii;
#define F first
#define S second

#define M (2*5*N)
int mark[5*N], mk;
int meo[2][5*N];
int fila[M];
int ini, fim;
int vai() {
	memset(mark,0,sizeof mark);
	mk = 1;
	ini = 0;
	fim = 2;
	fila[0] = 0;
	fila[1] = -1;
	int A = 0;
	int B = 1;
	int y = 0;
	char c = str[0]-'a';
	
	meo[A][0] = 0;
	while( true ) {
		int at = fila[ini++];
		if( ini == M ) ini = 0;
		if( at == -1 ) {
			//if( ini == fim ) break;
			mk++;
			y++;
			swap(A,B);
			if( !str[y] ) break;
			
			fila[fim++] = -1;
			if( fim == M ) fim = 0;
			
			c = str[y]-'a';
			continue;
		}
		int x = at%N;
		int z = at/N;
		int v = meo[A][at];
		
		denovo:;
		if( z == 0 ) {
			fr(i,0,26) {
				if( ~t[x].x[i] ) {
					int p = 4*N+t[x].x[i];
					if( mark[p] != mk || meo[B][p] > v+1 ) {
						meo[B][p] = v+1;
						if( mark[p] != mk ) {
							mark[p] = mk;
							fila[fim++] = p;
							if( fim == M ) fim = 0;
						}
					}
				}
			}
		}
		if( ~t[x].x[c] ) {
			int p = t[x].x[c] + (z?z-1:0)*N;
			if( mark[p] != mk || meo[B][p] > v ) {
				meo[B][p] = v;
				if( mark[p] != mk ) {
					mark[p] = mk;
					fila[fim++] = p;
					if( fim == M ) fim = 0;
				}
			}
		}
		if( t[x].f ) {
			x = 0;
			goto denovo;
		}
	}
	
	int ret = 10000;
	while( ini != fim ) {
		int at = fila[ini++];
		if( ini == M ) ini = 0;
		
		int x = at%N;
		int v = meo[A][at];
		if( t[x].f ) ret = min(ret, v);
	}
	return ret;
}

int main() {
	FILE * f = fopen("words.txt", "r"); // words.txt = garbled_email_dictionary.txt
	while( fscanf(f,"%s", str) == 1 ) {
		int x = 0;
		for( int i = 0 ; str[i] ; ++i ) {
			if( !~t[x].x[str[i]-'a'] ) {
				t[x].x[str[i]-'a'] = ult++;
			}
			x = t[x].x[str[i]-'a'];
		}
		t[x].f = true;
	}
	fclose(f);
	cerr << ult << endl;
	int tc, caso = 1;
	si(tc);
	while( tc--  ){
		printf("Case #%d: ", caso++);
		scanf("%s", str);
		//memset(pd,-1,sizeof pd);
		printf("%d\n", vai());
		
		cerr << tc << endl;
	}
	return 0;
}

