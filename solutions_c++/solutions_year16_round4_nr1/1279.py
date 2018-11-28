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

ll n,S,R,P;

inline pair<ll,ll> srt(pair<ll,ll> x){
if(x.X>x.Y) swap(x.X,x.Y); 
return x;
}
pair<ll,ll> win(ll x){
	ll y;
	pair<ll,ll> t;
	if(x==0){
		y=1;
	}
	else if(x==1){
		y=2;		
	}
	else if(x==2){
		y=0;		
	}
	return srt({x,y});
}

vector<ll> big(vector<ll> x){
	if(x.size()==(1<<n)) return x;
	pair<ll,ll> y;
	vector<ll> ans;
	F(i,0,x.size()-1){
		y=win(x[i]);
		ans.pb(y.X);
		ans.pb(y.Y);
	}
	return big(ans);
}
string ch(vector<ll> x){
	string s="";
	F(i,0,x.size()-1){
		if(x[i]==0){
			s+='P';
		}
		else if(x[i]==1){
			s+='R';
		}
		else{
			s+='S';
		}
	}
	return s;
}
bool ok(vector<ll> x){
	ll c1=0,c2=0,c3=0;
	F(i,0,x.size()-1){
		if(x[i]==0) c1++;
		else if(x[i]==1) c2++;
		else c3++;
	}
	if(c1==P && c2==R && c3==S) return true;
	return false;
}
string sot(string v){
	if(v.size()==2){
		if(v[0]>v[1]) swap(v[0],v[1]);
		return v;
	}
	string v1=sot(v.substr(0,v.size()/2)),v2=sot(v.substr(v.size()/2,v.size()/2));
	if(v1>v2) swap(v1,v2);
	return v1+v2;
}
void solve(){
	vector<ll> v1=big({0}),v2=big({1}),v3=big({2});
	string s1=sot(ch(v1)),s2=sot(ch(v2)),s3=sot(ch(v3));
//	cout<<s1<<endl<<s2<<endl<<s3<<endl<<endl;
	vector<string> ans;
	if(ok(v2)) ans.pb(s2);
	if(ok(v1)) ans.pb(s1);
    if(ok(v3)) ans.pb(s3);
    
    if(ans.empty()) cout<<"IMPOSSIBLE"<<endl;
    else {
    	sort(ans.begin(),ans.end() );
    	cout<<ans[0]<<endl;
	}
}
void in(){
	cin>>n>>R>>P>>S;
}
void clr(){
	
}

int main(){
freopen("input.txt","r",stdin);
freopen("output.txt","w",stdout);
//cout << setprecision(22) << fixed;
ios::sync_with_stdio(false);



ll tst; cin>>tst;
F(ioi,1,tst){
	cout<<"Case #"<<ioi<<": ";
	clr();
	in();
	solve();
}



return 0;   
}
