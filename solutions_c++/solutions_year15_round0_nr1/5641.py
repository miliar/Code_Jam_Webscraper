#include<iostream>
#include<algorithm>
using namespace std;
int main() {
	int c=1,T;
	cin>>T;
	while(c<=T) {
		int n,ans=0;
		string s;
		cin>>n>>s;
		for(int i=1;i<s.size();i++) {
			int tc=0;
			for(int j=i-1;j>=0;j--)tc+=(s[j]-'0');
			ans=max(ans,i-tc);
		}
		cout<<"Case #"<<c<<": "<<ans<<endl;
		c++;
	}
	return 0;
}
