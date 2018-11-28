#include <bits/stdc++.h>
using namespace std;
#define de(x) cout << #x << " = " << x << endl
#define rep(i,a,b) for(int i=a;i<b;++i)
#define per(i,a,b) for(int i=b-1;i>=a;--i)
#define all(x) (x).begin(),(x).end()
#define sz(x) (int)(x).size()
#define mp make_pair
#define pb push_back
#define fi first
#define se second
typedef long long ll;
typedef double db;
typedef pair<int, int> pii;
typedef vector<int> vi;
const double pi = acos(-1.0), eps = 1e-8;
const int inf = ~0U >> 2 , P = 1e9 + 7;
int Pow(int x,ll t){int r=1;for(;t;t>>=1,x=(ll)x*x%P)if(t&1)r=(ll)r*x%P;return r;}
void setIO(){
	freopen("a.in","r",stdin);
	freopen("out.txt","w",stdout);
}
const int N = 202;
int n , K;db p[N];
db f[N][N];
db gt(const vector<db> &P){
	f[0][0] = 1;
	for(int i=1;i<=K;++i){
		for(int j=1;j<i;++j)
			f[i][j] = f[i-1][j-1] * P[i] + f[i-1][j] * (1 - P[i]);
		f[i][0] = f[i-1][0] * (1 - P[i]);
		f[i][i] = f[i-1][i-1] * P[i];
	}
	return f[K][K/2];
}
void main2(){
	scanf("%d%d",&n,&K);
	rep(i,0,n) scanf("%lf",p + i);
	sort(p , p + n);
	db ans = 0;
	for(int i=0;i<=K;++i){
		vector<db> P;P.pb(1);rep(j,0,n) if(j < i || n - j + i <= K) P.pb(p[j]);
		ans = max(ans , gt(P));
	}
	printf("%.10f\n",ans);
}

int T;
int main(){
	setIO();
	scanf("%d",&T);
	rep(re,1,T+1){
		printf("Case #%d: ",re);
		main2();
	}
	return 0;
}
