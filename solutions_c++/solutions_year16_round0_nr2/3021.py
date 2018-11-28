#include<bits/stdc++.h>
#define ll long long

using namespace std;

stack < char > stac;

int main(){
	
	string s,st;
	ll t,i,j,ans;
	cin>>t;
	for(j=1;j<=t;j++){
		cin>>s;
		ans=0;
		while(true){
			stac.push(s[0]);
			for(i=1;i<s.length();i++){
				if(s[i]!=stac.top()){
					break;
				}
			}
			if(i==s.length() && stac.top()=='+')break;
			else if(i==s.length()){
				ans++;break;
			}
			st="";
			while(!stac.empty()){
				char z= stac.top();
				stac.pop();
				if(z=='-')st+='+';
				else st+='-';
			}
			while(i<s.length()){
				st+=s[i];
				i++;
			}
			s=st;
			ans++;
		}
		while(!stac.empty()){
			stac.pop();
		}
		cout<<"Case #"<<j<<": "<<ans<<"\n";
		//cout<<ans<<"\n";
	}
	return 0;
}
