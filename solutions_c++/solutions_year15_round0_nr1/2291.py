#include <bits/stdc++.h>

using namespace std;

#define pb push_back
#define fr(i,a,b) for(auto i=a;i<=b;i++)
#define rfr(i,a,b) for(auto i=b;i>=a;i--)

typedef long long ll;

int main(){
	freopen("in","r",stdin);
	freopen("out","w",stdout);
	ll T,Smax;
	vector<ll> S;
	cin>>T;

	fr(xx,1,T){
		S.clear();
		cin>>Smax;
		ll cur,req=0,res=0;
		string ss;
		cin>>ss;
		fr(i,0,Smax){
			ll a=ss[i]-'0';
			S.pb(a);
		}
		cur=S[0];
		fr(i,1LL,Smax){
			req=i;
			if(req>cur){
				res+=(req-cur);
				cur+=((req-cur)+S[i]);
			}
			else{
				cur+=S[i];
			}
		}
		cout<<"Case #"<<xx<<": "<<res<<"\n";
	}

	return 0;
}