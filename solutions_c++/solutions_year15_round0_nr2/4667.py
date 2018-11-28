/* abhra73 */
#include <bits/stdc++.h>
#define sp(z) 				setprecision(z)
#define sv(z) 				sort(z.begin(),z.end())
#define F 					first
#define S 					second
#define pb 					push_back
#define mp 					make_pair
#define ll 					long long
#define ld 					long double 
#define si(z) 				scanf("%d",&z)
#define sl(z) 				scanf("%Ld",&z)
#define sd(z) 				scanf("%Lf",&z)
#define sc(z) 				scanf("%c",&z)
#define fre(y,q,s) 			for(int y=q;y>=s;y--)
#define fr(y,q,s) 			for(int y=q;y<s;y++)
#define f(y,z) 				for(int y=0;y<z;y++)
#define fe(y,z) 			for(int y=1;y<=z;y++)
#define matrix(arr,n,m)		vector<vector<ll> > arr(n,vector<ll>(m,0))
using namespace std;
ll lmin(ll a,ll b){ return (a<b)?a:b; } ll lmax(ll a,ll b){ return (a>b)?a:b; }
ld dmin(ld a,ld b){ return (a<b)?a:b; } ld dmax(ld a,ld b){ return (a>b)?a:b; }
ll gcd(ll a,ll b){ return (b==0)?a:gcd(b,a%b); } ll lcm(ll a, ll b) { return (a*b)/gcd(a,b); }
ll modpow(ll a, ll n, ll mod){ ll res=1; while(n){ if(n&1)res=(res*a)%mod; a=(a*a)%mod; n>>=1; } return res; }
ll lpow(ll a, ll n){ ll res=1; while(n){ if(n&1)res*=a; a*=a; n>>=1; } return res; }
ld dpow(ld a, ll n){ ld res=1; while(n){ if(n&1)res*=a; a*=a; n>>=1; } return res; }

/* ********************** Main Code starts from here ********************** */


int solve(vector<int> v){
	int ret=9,hlp;
	fe(j,9){
		hlp=j;
		f(i,v.size()){
			if(v[i] > j){
				hlp += v[i]/j;
				if(v[i]%j==0) hlp--;
			}
		}
		ret=min(hlp,ret);
	}
	return ret;
}

int main(){
	vector<int> v;
	int d,p;
	int t,ans,cas=0;
	si(t);
	while(t--){
		printf("Case #%d: ",++cas);
		v.clear();
		si(d);
		f(i,d){
			si(p);
			v.pb(p);
		}
		ans=solve(v);
		printf("%d\n",ans);
	}
	return 0;
}