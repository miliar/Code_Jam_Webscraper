#include <iostream>
#include <string>
using namespace std;

int T;
string s;

int main() {
	cin>>T;
	for (int ii=1; ii<=T; ii++) {
		cin>>s;
		int i=0,ans=0;
		while (s[i]=='-'&&i<s.length()) {
			i++;
			ans=1;
		}
		i++;
		while (i<s.length()) {
			if (s[i-1]=='+'&&s[i]=='-')
				ans+=2;
			i++;
		}
		cout<<"Case #"<<ii<<": "<<ans<<endl;
	}
}
