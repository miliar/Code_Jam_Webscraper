#include <iostream>
#include <string>
using namespace std;

void op(string &s, int idx, int k) {
	for(int i=0;i<k;i++)
		if(s[i+idx]=='-')
			s[i+idx]='+';
		else s[i+idx]='-';	
}

bool ok(string s) {
	return s.find('-')==string::npos;
}

void solve(int tc) {
	string s;
	int k;
	cin>>s>>k;
	int ret=0;
	for(int i=0;i+k<=s.size();i++) if(s[i]=='-') {
		op(s,i,k);
		ret++;
	}
	cout<<"Case #"<<tc<<": ";
	if(!ok(s)) cout<<"IMPOSSIBLE"<<endl;
	else cout<<ret<<endl;
}

int main() {
	int t;
	cin>>t;
	for(int i=1;i<=t;i++) solve(i);
}
