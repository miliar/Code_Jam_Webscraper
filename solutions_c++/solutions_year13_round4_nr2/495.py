#include <bits/stdc++.h>
using namespace std;

#define fr(a,b,c) for(int a = b ; a < c ; ++a )
#define db(x) cerr << #x " == " << x << endl
#define _ << ", " <<

typedef long long ll;

ll comb[60][60], som[60][60];
int n;
ll p,q;

int main() {
	fr(i,0,60) {
		comb[i][0] = comb[i][i] = 1;
		fr(j,1,i) comb[i][j] = comb[i-1][j-1] + comb[i-1][j];
		som[i][0] = 0;
		fr(j,0,i+1) som[i][j+1] = som[i][j] + comb[i][j];
		som[i][i+2] = som[i][i+1]+1;
	}
	

	int T, caso = 1;
	scanf("%d", &T);
	while( T-- ) {
		printf("Case #%d: ", caso++);
		scanf("%d%lld", &n, &p);
		if( p == (1LL<<n) ) {
			printf("%lld %lld\n", p-1, p-1);
			continue;
		}
		q = 1LL<<n;
		int k = 0;
		ll x = 0;
		while( p > (x|(1LL<<n-k-1)) ) x = x | (1LL<<n-k-1), k++;
		ll r1 = (1LL<<k+1)-2;
		x = 0;
		k = 0;
		while( p > (x|(1LL<<k)) ) x = x | (1LL<<k), k++;
		ll r2 = 0;
		int y = 0;
		while( k-- ) r2 = r2 | (1LL<<n-y-1), y++;
		
		printf("%lld %lld\n", r1, r2);
	}
	return 0;
}
