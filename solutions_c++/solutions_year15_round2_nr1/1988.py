/********************

	root8950

*********************/


#include<bits/stdc++.h>
using namespace std;
#define ll long long
#define PII pair<int,int>
#define ft first
#define sd second
#define MAXN MOD
#define mp make_pair
#define f_in(st) freopen(st,"r",stdin)
#define f_out(st) freopen(st,"w",stdout)
#define sc(x) scanf("%d",&x)
#define scll(x) scanf("%lld",&x)
#define pr(x) printf("%d\n",x)
#define prll(x) printf("%lld\n",x)
#define pb push_back
#define MOD 1000000007
#define PIE 3.141592653589
#define inf INT_MAX/2
#define ASST(X,L,R) assert(X >= L && X <= R)

ll rev(ll n ){
	ll revnum=0;
	while(n>0){
		revnum=revnum*10+n%10;
		n=n/10;
	}
	return revnum;
}

vector<ll> cache(1000001);

void solve(){
	for(int i=1;i<=1000000;i++){
		ll revnum=rev(i);
		if(i%10!=0 && revnum < i){
			cache[i]=min(cache[i-1]+1,cache[revnum]+1);
		}
		else cache[i]=cache[i-1]+1;
	}
}

int idx=1;

int main(){
	//ios_base::sync_with_stdio(false);
	//cin.tie(NULL);
	int t;
	cin >> t;
	solve();
	while(t--){
		ll n;
		cin >> n;
		cout << "Case #" << idx << ": ";
		idx++;
		cout << cache[n] << "\n";
	}
	return 0;
}

