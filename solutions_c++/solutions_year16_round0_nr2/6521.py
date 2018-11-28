#include <iostream>
using namespace std;

int find(string s) {
	if(s.length() == 1) {
		if(s[0] == '-') return 1;
		else return 0;
	}
	else {
		int ct = 0;
		for(int i=1;i<s.length();i++) {
			if(s[i] != s[i-1]) ct++;
		}
		if(s[s.length()-1] == '-') ct++;
		return ct;
	}
}

int main() {
	int T;
	cin>>T;
	int cs = 1;
	while(T--) {
		string s;
		cin>>s;
		cout<<"Case #"<<cs++<<": "<<find(s)<<endl;
	}
	return 0;
}