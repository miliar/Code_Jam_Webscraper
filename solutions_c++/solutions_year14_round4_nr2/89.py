// TwT514 {{{
#include <bits/stdc++.h>
#define SZ(x) ((int)(x).size())
#define FOR(i,c) for (auto i=(c).begin(); i!=(c).end(); i++)
#define REP(i,n) for (int i=0; i<(n); i++)
#define REP1(i,a,b) for (int i=(int)(a); i<=(int)(b); i++)
#define ALL(x) (x).begin(),(x).end()
#define MS0(x,n) memset(x,0,(n)*sizeof(*x))
#define MS1(x,n) memset(x,-1,(n)*sizeof(*x))
#define MP make_pair
#define PB push_back
#define RI(a) scanf("%d",&(a))
#define RII(a,b) scanf("%d%d",&(a),&(b))
#define RIII(a,b,c) scanf("%d%d%d",&(a),&(b),&(c))
using namespace std;
typedef long long LL;
typedef pair<int,int> PII;
typedef vector<int> VI;
// }}}
#define N 1010

int n, a[N];
void input(){
	RI(n);
	REP(i,n) RI(a[i]);
}


void go(int res[]){
	res[0] = 0;
	REP(i,n){
		res[i+1] = res[i];
		REP(j,i) if(a[j]>a[i]) res[i+1]++;
	}
}
int l[N], r[N];

void solve(){
	go(l);
	reverse(a,a+n);
	go(r);
	reverse(r,r+n+1);
	//REP(i,n+1) printf("%d ", l[i]);puts("");
	//REP(i,n+1) printf("%d ", r[i]);puts("");
	int ans = N*N;
	REP(i,n+1) ans = min(ans,l[i] + r[i]);
	static int zi = 0;
	printf("Case #%d: %d\n", ++zi, ans);
}

void solve2(){
	int ans = 0;
	for(int i=0, j=n-1; i<=j; ){
		int mn=i;
		for(int k=i; k<=j; k++) if(a[k]<a[mn]) mn=k;
		if(mn-i < j-mn){
			ans += mn-i;
			for(int k=mn-1; k>=i; k--) a[k+1] = a[k];
			i++;
		}
		else{
			ans += j-mn;
			for(int k=mn+1; k<=j; k++) a[k-1] = a[k];
			j--;
		}
	}
	static int zi = 0;
	printf("Case #%d: %d\n", ++zi, ans);
}

int main() {
	int zn;
	RI(zn);
	while(zn--){
		input();
		solve2();
	}
    return 0;
}

