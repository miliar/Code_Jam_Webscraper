#include <bits/stdc++.h>
using namespace std;
#define de(x) cout << #x << " = " << x << endl
#define rep(i,a,b) for(int i=a;i<(b);++i)
#define per(i,a,b) for(int i=(b)-1;i>=(a);--i)
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
const int N = 101;
int T , n , L;
string s[N] , G;
void wk(){
	cin >> n >> L;
	rep(i,0,n) cin >> s[i];
	cin >> G;
	rep(i,0,n) if(s[i] == G){
		puts("IMPOSSIBLE");
		return;
	}
	if(L == 1){
		printf("0 0?\n");
	} else{
		rep(i,0,L-1) putchar('1');
		putchar(' ');
		rep(i,0,L) printf("0?");
		puts("");
	}
}

int main(){
	setIO();
	cin >> T;
	rep(i,1,T+1){
		cerr << i << endl;
		printf("Case #%d: ",i);
		wk();
	}
	return 0;
}
