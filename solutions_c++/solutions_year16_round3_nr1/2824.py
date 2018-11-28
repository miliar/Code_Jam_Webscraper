#include <bits/stdc++.h>

#define INF 0x3F3F3F3F
#define rep(i, a, b) for (int i = int(a); i < int(b); i++)
#define pb push_back
#define pi 3.1415926535897932384626433832795028841971
#define debug(x) cout << #x << " = " << x << endl;
#define debug2(x,y) cout << #x << " = " << x << " --- " << #y << " " << y << "\n";
#define debugM( x, l, c ) { rep( i, 0, l ){ rep( j, 0, c ) printf("%d ", x[i][j]); printf("\n");}}
#define all(S) (S).begin(), (S).end()
#define MAXV 1010000
#define MAXN 110
#define F first
#define S second
#define EPS 1e-9
#define mk make_pair

using namespace std;

typedef pair <int, int> ii;
typedef long long int ll;

ll readInt();

char aux[] = {"ABCDEFGHIJKLMNOPQRSTUVWXYZ"};
int sum, p[30], n;
string resp;

inline bool cmp( int a, int b ){
	return p[a] > p[b];
}

void solve(){
	int v[30];
	rep( i, 0, n ) v[i] = i;
	while( 1 ){
		sort( v, v+n, cmp );
		int u = v[0], w = v[1];
		if( !p[u] ) break;
		if( p[u] > p[w] ){
			if( p[u] > 1 ){
				printf(" %c%c", aux[u], aux[u] );
				p[u] -= 2;
				sum -= 2;
			}
			else{
				printf(" %c", aux[u] );
				p[u]--;
				sum--;
			}
		}
		if( p[u] == p[w] ){
			if( p[u] == 1 && sum&1 ){
				printf(" %c", aux[u] );
				p[u]--;
				sum--;
			}
			else{
				printf(" %c%c", aux[u], aux[w] );
				p[u]--; p[w]--;
				sum -= 2;
			}
			
		}
	}	
}

int main(){
	
	freopen( "A-large.in", "r", stdin );
	freopen( "A.txt", "w+", stdout );

	int t;
	scanf("%d", &t );
	rep( T, 1, t+1 ){
		resp = "";
		scanf("%d", &n );
		sum = 0;
		rep( i, 0, n ){
			scanf("%d", &p[i] );
			sum += p[i];
		}
		printf("Case #%d:", T );
		solve();
		printf("\n");
	}
}

