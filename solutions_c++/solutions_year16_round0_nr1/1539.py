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

ll di[10];

void nu(ll x){
	while(x){
		di[x%10]=1;
	    x/=10;
	}
}

inline bool ch(){
	F(i,0,9) if(di[i]==0) return false;
	return true;
}
void solve(ll n,ll po){
	fill(di,di+10,0);
	ll ct=0,k=1000000;
	while(!ch() && k){
		ct++;
		nu(ct*n);
		k--;
	}
	if(k==0) cout<<"Case #"<<po<<": "<<"INSOMNIA"<<endl;
	else cout<<"Case #"<<po<<": "<<ct*n<<endl;
}




int main(){
freopen("input.txt","r",stdin);
freopen("output.txt","w",stdout);
//cout << setprecision(22) << fixed;
ios::sync_with_stdio(false);


ll tst,n; cin>>tst;
F(i,1,tst){
	cin>>n;
	solve(n,i);
}







return 0;   
}
