#include <bits/stdc++.h>
using namespace std;

typedef long long ll;
const double pi = acos(-1.0);
const double eps = 1e-8;
//const ll INF=(_I64_MAX)/2;
//#pragma comment(linker, "/STACK:102400000,102400000")
const int inf = 0x3f3f3f3f;
#define maxx(a) memset(a, 0x3f, sizeof(a))
#define minn(a) memset(a, 0xC0, sizeof(a))
#define zero(a) memset(a, 0, sizeof(a))
#define FILL(a,b) memset(a, b, sizeof(a))
#define REP(i,a,b) for(i=a;i<b;i++)
#define rep(i,n) REP(i,0,n)
#define srep(i,n) for(i = 1;i <= n;i ++)
#define MP make_pair
#define fi first
#define se second
typedef pair<int, int> PII;
typedef pair<ll, ll> PX;

const int N = 100 + 11;


char a[N][N];
int c1[N],c2[N];
void work() {
	int r,c;
	FILL(c1,0);
	FILL(c2,0);
	cin>>r>>c;
	int i,j;
	rep(i,r) rep(j,c) {

		cin>>a[i][j];
		if(a[i][j] != '.') {
			c1[i] ++;
			c2[j] ++;
		}
	}

	int ans = 0;
	int k;


	rep(i,r) rep(j,c) {
		if(c1[i] == 1 && c2[j] == 1 && a[i][j] != '.') {
			//cout<<"?"<<i<<' '<<j<<endl;
			puts("IMPOSSIBLE");return;
		}
	}


	rep (i,r) rep(j,c) {
		if (a[i][j] != '.') {
			bool tag = 0;
			if(a[i][j] == '^') {
				for(k = i-1;k >= 0;k --) {
					if(a[k][j] != '.') tag = 1;
				}

			}
			else if(a[i][j] == '>') {
				for(k = j+1;k < c;k ++) {
					if(a[i][k] != '.') tag = 1;
				}
			}
			else if(a[i][j] == '<') {
				for(k = j-1;k >= 0;k --) {
					if(a[i][k] != '.') tag = 1;
				}
			}
			else {
				for(k = i+1;k < r;k ++) {
					if(a[k][j] != '.') tag = 1;
				}
			}
			if(!tag) {
				ans ++;
			}
		}

	}

	cout<<ans<<endl;
}


int main() {
#ifdef LOCAL
	freopen("in.txt", "r", stdin);
	freopen ("out.txt","w",stdout );
#endif
//    init();
//
//    getprime(N-1);
    int cas = 1;
    int t;
    cin>>t;
    while(t--) {
    	printf("Case #%d: ",cas++);
    	work();
    }


	return 0;
}

