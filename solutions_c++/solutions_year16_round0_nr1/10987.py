#include <bits/stdc++.h>
#define ll long long
#define ld long double
#define pb push_back
#define mp make_pair
#define PI 2*asin(1)
#define all(v) v.begin(),v.end()
#define forall(it,v) for(it=v.begin();it!=v.end();it++)
#define min3(a,b,c) min(a,min(b,c))
#define max3(a,b,c) max(a,max(b,c))
#define clr(v,n) memset(v,n,sizeof v)
#define clrv(v,n) REP(i,sz(v)) v[i]=n;
#define REP(i,n) for(int i=0; i<n; i++)
#define rep(i,a,b) for(int i=a; i<b; i++)
#define sz(v) v.size()
#define pii pair<int,int> 
#define pii pair<int,int> 
#define F first
#define S second
#define INF INT_MAX
#define INFL 100000000000000007
#define EPS 1e-7
inline ll gcd (ll a, ll b) { return (b?gcd(b, a%b):a); }
inline ll lcm (ll a, ll b) { return (a/gcd(a, b))*b; }
inline int cmp(double x, double y = 0, double tol = EPS){return (x <= y + tol) ? (x + tol < y) ? -1 : 0 : 1;}
using namespace std;
const int MAXN=5005;

set <int> q;

void put(ll n){
	while(n){
		q.insert(n%10);
		n/=10;
	}
}
int main(){
	int n, t;
	cin >> t;
	
	int caso=0;
	while(t--){
		caso++;
		cin >> n;
		q.clear();
		
		ll cnt=0;
		while(q.size()<10 && cnt<1e7){
			cnt++;
			put(cnt*n);
		}
		
		if(q.size()==10){
			printf("Case #%d: %Ld\n", caso, n*cnt);
		}
		else{
			printf("Case #%d: INSOMNIA\n", caso);
		}
	}
}
























