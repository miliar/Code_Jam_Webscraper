#include<bits/stdc++.h>

using namespace std;


int main() {
	int tCase;
	cin>>tCase;
	for (int t=1; t<=tCase; ++t) {
		string s;
		cin>>s;
		string ans = "";
		ans += s[0];
		for (int i = 1,len=s.size(); i < len; ++i)
		{
			if(s[i] >= ans[0]){
				ans = s[i]+ans;
			}
			else {
				ans = ans+s[i];
			}
		}
	      	cout<<"Case #"<<t<<": "<<ans<<endl;	      
	}
	return 0;
}