#include<bits/stdc++.h>
#define ll long long

using namespace std;

ll power(ll base,ll exp){
	ll ret=1;
	while(exp>0){
		if(exp & 1)ret=ret*base;
		base*=base;
		exp>>=1;
	}
	return ret;
}

int main(){
	ll t,k,c,s,i,j,ans,temp;
	cin>>t;
	for(j=1;j<=t;j++){
		ans=1;
		cin>>k>>c>>s;
		temp=power(k,c-1);
		cout<<"Case #"<<j<<": "<<ans<<" ";
		for(i=1;i<s;i++){
			cout<<ans+temp<<' ';
			ans+=temp;
		}
		cout<<"\n";
	}
	return 0;
}
