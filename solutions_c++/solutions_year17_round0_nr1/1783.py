#include <bits/stdc++.h>
using namespace std;
int main(){
	int t,k,tc=1,ans,i,j;
	string s;
	for(cin>>t;tc<=t;++tc){
		cin>>s>>k;
		for(i=ans=0;i<s.size()-k+1;++i)
			if(s[i]=='+') continue;
			else for(++ans,j=i;j<i+k;++j) s[j]= s[j]=='+'?'-':'+';
		for(;i<s.size();++i)
			if(s[i]=='-'){
				cout<<"Case #"<<tc<<": "<<"IMPOSSIBLE\n";
				break;
			}
		if(i==s.size()) cout<<"Case #"<<tc<<": "<<ans<<'\n';
	}
}