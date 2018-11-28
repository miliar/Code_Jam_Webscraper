#include <bits/stdc++.h>
using namespace std;
typedef long long int ll;

int main() {
	ll tc;cin>>tc;
	
	for(ll ii=1;ii<=tc;ii++)
	{
		cout<<"Case #"<<ii<<": ";
		string s,ss;cin>>ss;
		s+=ss[0];
		
		for(ll i=0;i<ss.length()-1;i++)
			if(ss[i]!=ss[i+1])
				s+=ss[i+1];
		
		
			if(s[s.length()-1]=='+')
				cout<<(s.length()-1)<<"\n";
			else
				cout<<s.length()<<"\n";
			
		
		
	}
	
	
	return 0;
}