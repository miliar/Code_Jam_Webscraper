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
double V,X;
int n;
double v[N],x[N];



void work() {
	cin>>n>>V>>X;
	int i,j;
	rep(i,n) {
		cin>>v[i]>>x[i];
	}
	if (x[0] == x[1]) {
		n = 1;
		v[0] += v[1];
	}


	if(n ==1) {
		if(fabs(x[0] - X) > 1e-6) {
			puts("IMPOSSIBLE");return;
		}
		printf("%.8lf\n",V/v[0]);return;
	}

	if(x[0] > x[1]) {
		swap(x[0],x[1]);
		swap(v[0],v[1]);
	}
	if(X < x[0] || X  > x[1]) {
		puts("IMPOSSIBLE");return;
	}

	double t1 =  X - x[1];
	double t2 = x[0] - X;
	if(t1 < 0) {
		t1 = -t1;
		t2 = -t2;
	}

	//cerr<<t1<<' '<<t2<<endl;

	if (fabs(t1) < 1e-8) {
		printf("%.8lf\n",V/v[1]);return;
	}
	if (fabs(t2) < 1e-8) {
		printf("%.8lf\n",V/v[0]);return;
	}
	double z1 = V/(t1+t2)*t1 / v[0];
	double z2 = V/(t1+t2)*t2 / v[1];
	printf("%.8lf\n",max(z1,z2));return;
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

