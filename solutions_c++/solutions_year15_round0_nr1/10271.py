#include <bits/stdc++.h>
#define ll long long
using namespace std;

int main() {
	int t,s,m=1;
	string p;
	cin>>t;
	while(t--){
		cin>>s;
		cin>>p;
		ll st=0,ans=0;
		st+=(p[0]-'0');
		for(int i=1;i<p.length();i++){
			if(st<i){ans+=i-st;st+=i-st+(p[i]-'0');}
			else st+=(p[i]-'0');
			
}
		cout<<"Case #"<<m<<": "<<ans<<endl;
		m++;
		
}
	return 0;
}
