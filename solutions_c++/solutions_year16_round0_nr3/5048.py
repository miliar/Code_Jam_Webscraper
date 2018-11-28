#include <bits/stdc++.h>

#define pb push_back
#define mp make_pair
#define f first
#define s second
#define all(x) x.begin(),x.end()
#define rall(x) x.rbegin(),x.rend()
#define pi acos(-1.0)
#define EPS 1e-9
#define mem(n,x) memset(n,x,sizeof(n))
typedef long long ll;

using namespace std;

vector<string> v;

void rec(int ind,string s){
	if(ind==16){v.pb(s);return;}

	rec(ind+1,s+"1");
	if(ind>0 && ind<15)rec(ind+1,s+"0");
}

ll toBase(string &s,int b){
	ll p=1, ret=0;
	for(int i=15;i>=0;--i){
		if(s[i]=='1')ret+=p;
		p*=b;
	}
	return ret;
}

ll check(ll x){
	if(x==2)return 0;
	if(x<2)return x;
	if(x%2==0)return 2;

	for(ll i=3;i*i<=x;i+=2){
		if(x%i==0)return i;
	}
	return 0;
}

int main()
{
	freopen("C-small-attempt0.in","r",stdin);
	freopen("C-small-attempt0.out","w",stdout);
	rec(0,"");
	vector<pair<string, vector<ll>  > > ans;
	for(string s:v){
		bool ok=1;
		vector<ll> tt;
		for(int i=2;i<=10;++i){
			ll tmp=check(toBase(s,i));
			if(!tmp){ok=0;break;}
			tt.pb(tmp);
		}
		if(ok)ans.pb(mp(s,tt));
		if(ans.size()==50)break;
	}

	cout<<"Case #1:\n";
	for(auto x:ans){
		cout<<x.f;
		for(ll i:x.s)cout<<" "<<i;
		cout<<"\n";
	}

	return 0;
}
