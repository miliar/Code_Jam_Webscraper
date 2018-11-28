#include<bits/stdc++.h>
using namespace std;

typedef long long ll;

ll pow(ll b,ll e){
	if (e==0)return 1;
	if(e%2==0){
		ll temp=pow(b,e/2);
		return temp*temp;
	}
	else{
		ll temp=pow(b,e/2);
		return temp*temp*b;
	}
}

int main(){
	int T;cin>>T;
	for(ll t=1;t<=T;t++){
		ll k,c,s;
		cin>>k>>c>>s;
		//cout<<k<<" "<<c<<" "<<s<<" "<<pow(k,c)<<endl;
		if(s < k/c +(k%c>0)){
			cout<<"Case #"<<t<<": IMPOSSSIBLE"<<endl;
			continue;
		}
		cout<<"case #"<<t<<": ";
		for(ll i=1;i<= k/c;i++){
			ll temp=1;
			for(ll j=0;j<c;j++)
				temp+=(c*(i-1)+j)*pow(k,(ll)(c-1-j));
			cout<<temp<<" ";
			//if(temp>pow(k,c))cout<<"*****"<<pow(k,c)<<" "<<temp<<"#########\n";
		}
		if(k%c>0){
			ll temp=1;
			for(ll j=0;j<k%c;j++)
				temp+=((k/c)*c+j)*pow(k,(ll)(c-1-j));
			cout<<temp;
		}
		cout<<endl;
	}
}