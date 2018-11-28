#include<bits/stdc++.h>
using namespace std;
int main(){
	int n,t;
	cin>>t;
	for(int tcase=1;tcase<=t;tcase++){
		string s;
		cin>>s;
		n=s.length();
		int ans=0;
		for(int i=0;i<n-1;i++){
			if(s[i]=='+' && s[i+1]=='-')
				ans+=2;
		}
		if(s[0]=='-')ans++;
		cout<<"Case #"<<tcase<<": "<<ans<<endl;
	}
	return 0;
}