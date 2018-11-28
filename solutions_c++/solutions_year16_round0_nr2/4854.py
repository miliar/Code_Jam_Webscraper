#include<bits/stdc++.h>
using namespace std;
typedef long long ll;
int main(){
	freopen("B-large.in","r",stdin);
	freopen("a.txt","w",stdout);
	ll t;
	string a;
	cin>>t;
	for(ll i=1;i<=t;i++){
		cin>>a;
		cout<<"Case #"<<i<<": ";
		char now='+';
		ll cnt=0;
		bool flag=false;
		for(ll i=a.length()-1;i>=0;i--){
			if(a[i]=='-'&&!flag){
				flag=true;
				cnt++;
				now='-';
			}
			if(flag){
				if(a[i]!=now){
					now=a[i];
					cnt++;
				}
			}
		}
		cout<<cnt<<endl;
	}
}
