#include <bits/stdc++.h>

using namespace std;

#define MAX 1001
#define INF 1000000
#define EPS 1e-7
#define PI acos(-1.0)

#define PRINT(x) cout<<#x<<" = "<<x<<endl

#define READ() freopen("input.txt", "r", stdin)
#define WRITE() freopen("output.txt", "w", stdout)

#define CLR(x) memset( x, 0, sizeof(x) )
#define SET(x) memset( x, -1, sizeof(x) )

#define CHKBIT(x, i) ( ( ( x & ( 1 << i ) ) == 0 ) ? 0 : 1 )
#define SETBIT(x, i) ( x | ( 1 << i ) )
#define CLRBIT(x, i) ( x & (!( 1 << i )) )

#define pb push_back

#define ff first
#define ss second
#define mp make_pair
typedef pair<int, int> pii;

int main(){
	freopen("b_input.txt", "r", stdin);
	freopen("b_output.txt", "w", stdout);
	int T;
	scanf("%d", &T);
	for(int t=1; t<=T; t++){
		int a, b, k, res = 0;
		scanf("%d %d %d", &a, &b, &k);
		for(int i=0; i<a; i++){
			for(int j=0; j<b; j++){
				int x = i & j;
				if( x < k ) res++;
			}
		}
		printf("Case #%d: %d\n", t, res);
	}
	return 0;
}

