#include <bits/stdc++.h>

using namespace std;

#define pb push_back
#define fr(i,a,b) for(auto i=a;i<=b;i++)
#define rfr(i,a,b) for(auto i=b;i>=a;i--)

typedef long long ll;

ll get_mintime(vector<ll>& P){
	ll maxcnt=P[0];
	fr(i,0,(int)P.size()-1){
		maxcnt=max(maxcnt,P[i]);
	}
	ll mintime=maxcnt;
	fr(x,1,maxcnt-1){
		ll curres=x;
		fr(i,0,(int)P.size()-1){
			if(P[i]>x){
				curres+= ceil( ( (P[i]-x)*1.0 ) / (x*1.0) );
			}
		}
		mintime=min(mintime,curres);
	}
	return mintime;
}

int main(){
	freopen("in","r",stdin);
	freopen("out","w",stdout);
	ll T,D;vector<ll> P;
	cin>>T;
	fr(xx,1,T){
		cin>>D;
		P.clear();
		fr(i,0,D-1){
			ll a;
			cin>>a;
			P.pb(a);
		}
		ll res=get_mintime(P);
		cout<<"Case #"<<xx<<": "<<res<<"\n";
	}
	return 0;
}