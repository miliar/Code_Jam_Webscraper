#include<iostream>
#define ll long long
using namespace std;

int main(){
	ll t,s,k=1,c,c1;
	cin>>t;
	while(t--){
		ll i, j, len, d, p=0;
		cin>>s;
		string str;
		cin>>str;
		len = str.size();
		ll c[len];
		c[0] = str[0]-'0';
		for(i=1; str[i]; i++){
//			cout<<"i: "<<i<<"\n";

			if(c[i-1] >= i){
				c[i] = str[i]-'0'+c[i-1];
//				cout<<"c[i]: "<<c[i]<<"\n";
				continue;
			}
			else{
				d = i-c[i-1];
				p += d;
				c[i] = str[i]-'0'+c[i-1] + d;
//				cout<<"d: "<<d<<" p: "<<p<<" c[i]: "<<c[i]<<"\n";
			}				
		}
		cout<<"Case #"<<k<<": "<<p<<"\n";
		k++;
	}
}
