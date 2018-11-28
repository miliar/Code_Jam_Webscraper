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

ll K,C,S;

ll fi(ll x,ll marhale,ll ai){
	if(marhale==C) return x;
	x=(x-1)*K+ai;
	return fi(x,marhale+1,ai);
}

void solve(){
	F(i,1,K){
		cout<<fi(i,1,i)<<" ";
	}
	cout<<endl;
}


int main(){
freopen("input.txt","r",stdin);
freopen("output.txt","w",stdout);
//cout << setprecision(22) << fixed;
ios::sync_with_stdio(false);

ll tst; cin>>tst;
F(i,1,tst){
	cin>>K>>C>>S;
	cout<<"Case #"<<i<<": ";
	solve();
}







return 0;   
}
