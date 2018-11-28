#include <stdio.h>
#include <iostream>

using namespace std;

int main() {
	int test;
	cin>>test;
	for(int t=1; t<=test; t++) {
		int shy_max;
		string s;
		cin>>shy_max>>s;

		int ans=0,standing = 0;
		for(int i=0; i<s.size(); i++) {
			if(standing>=i) {
				standing += s[i]-'0';
			}
			else if(s[i]!='0') {
				ans += i-standing;
				standing = i + s[i]-'0';
			}
			//cout<<ans<<" ";
		}
		cout<<"Case #"<<t<<": "<<ans<<endl;
	}
	return 0;
}