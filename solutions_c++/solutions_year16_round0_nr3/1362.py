// IN THE NAME OF ALLAH
#include<bits/stdc++.h>
#define pb push_back
#define X first
#define Y second
#define F(i,a,b) for(ll i=(a) ; i<=(b) ; i++)
#define PI 3.1415926535897932384626433832795
#define eps 0.000001
using namespace std;
typedef long long ll;
typedef float ld;
const ll M=1e5+100;

ll tst,N,J,pw[11][17],da32[11]; 
struct gp{ string s;  ll div[11];  gp(){  s="";  fill(div,div+11,-1); } };
vector<gp> ans;
vector<string> v;

ll poow(ll a,ll b,ll mod){
	if(b==0) return 1;
	if(b==1) return a%mod;
	ll t=poow(a,b/2,mod);
	if(b%2==0) return (t*t)%mod;
	return (((t*t)%mod)*a)%mod;
}

inline bool MD(ll x,ll y,ll base){
	ll k=x+poow(base,31,y);
	if(k%y==0) return true;
	return false;
}

inline ll prime(ll x,ll base){
	F(i,2,1e4){
		if(MD(x,i,base)) return i;
	}
	return 0;
}

ll mabna(string s,ll b){
	ll ct=0;
	for(ll i=s.length()-1 , j=0 ; i>=0 ; i--,j++){
		ct+=(s[i]-'0')*pw[b][j];
	}
	return ct;
}

void make(ll x){
	if(x==17) return ;
	ll sz=v.size()-1;
	for(ll i=sz ; i>=0 ; i--){
		v.pb(v[i]+'1');
		if(x!=16) v.pb(v[i]+'0');
	}
	v.erase(v.begin(),v.begin()+sz+1);
	make(x+1);
}

void ch(string s){
	ll p[11];
	F(i,2,10){
		p[i]=prime(mabna(s,i),i);
		if(p[i]==0) return ;
	} 
	gp A;
	A.s=s;
	F(i,2,10) A.div[i]=p[i];
	ans.pb(A);
}


int main(){
freopen("input.txt","r",stdin);
freopen("output.txt","w",stdout);
//cout << setprecision(22) << fixed;
ios::sync_with_stdio(false);

v.pb("1");
make(2);
F(i,1,10) pw[i][0]=1;
F(i,1,16) F(j,1,10) pw[j][i]=j*pw[j][i-1];
cin>>tst>>N>>J;
cout<<"Case #1:"<<endl;
for(ll i=0 ; i<v.size() && ans.size()<500  ; i++) ch(v[i]);
//cout<<ans.size();


F(i,0,ans.size()-1){
	cout<<"1000000000000000";
	cout<<ans[i].s<<" ";
	F(j,2,10) cout<<ans[i].div[j]<<" ";
	cout<<endl;
}




return 0;   
}
