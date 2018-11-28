#include <bits/stdc++.h>
using namespace std;
int t;
string s;
bool solved(const string &s) {
	for(int i=0;i<s.length();++i) {
		if(s[i]=='-') {
			return false;
		}
	}
	return true;
}
int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(nullptr);
	cin>>t;
	for(int tt=1;tt<=t;++tt) {
		cout<<"Case #"<<tt<<": ";
		cin>>s;
		int cnt=0;
		while(!solved(s)) {
			cnt++;
			if(s[0]=='+') {
				for(int i=0;s[i]=='+';++i) {
					s[i]='-';
				}
			} else {
				for(int i=0;s[i]=='-';++i) {
					s[i]='+';
				}
			}
		}
		cout<<cnt<<"\n";
	}
	return 0;
}
