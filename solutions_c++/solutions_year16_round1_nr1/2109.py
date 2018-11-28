#include <iostream>
#include <sstream>
using namespace std;

string lastword(string& s) {
	string ret;
	ret = s[0];
	for(int i=1;i<s.length(); ++i) {
		if(ret[0] > s[i]) {
			ret = ret + s[i];
		} else {
			char c[] = {s[i], '\0'};
			ret = string(c) + ret;
		}
	}

	return ret;
}
int main() {
	int t;
	cin>>t;
	for(int i=1;i<=t;++i) {
		string str;
		cin>>str;
		cout<<"Case #"<<i<<": ";
		cout<<lastword(str)<<"\n";
	}
	return 0;
}
