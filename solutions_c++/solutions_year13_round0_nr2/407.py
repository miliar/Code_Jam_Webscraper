#include <bits/stdc++.h>
using namespace std;

#define fr(a,b,c) for( int a = b ; a < c ; ++a )
#define db(x) cerr << #x " == " << x << endl
#define _ << ", " <<

typedef long long ll;

int v[200][200];
int L[200], C[200];
int m,n;

int main() {
	int t, caso = 1;
	scanf("%d", &t);
	while( t-- ) {
		scanf("%d%d", &m, &n);
		fr(i,0,m) fr(j,0,n) scanf("%d", v[i]+j);
		printf("Case #%d: ", caso++);
		
		fr(i,0,m) {
			int ma = 0;
			fr(j,0,n) ma = max(ma,v[i][j]);
			L[i] = ma;
		}
		fr(j,0,n) {
			int ma = 0;
			fr(i,0,m) ma = max(ma,v[i][j]);
			C[j] = ma;
		}
		fr(i,0,m) fr(j,0,n) {
			if( v[i][j] < L[i] && v[i][j] < C[j] ) {
				puts("NO");
				goto fim;
			}
		}
		puts("YES");
		fim:;
	}
	return 0;
}
