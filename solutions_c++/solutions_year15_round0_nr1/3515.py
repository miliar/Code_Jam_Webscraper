#include<iostream>
#include <string>
using namespace std;
typedef long long lld;
int main () {
	int t,T;
	cin>>T;
	t=T;
	while (t--) {
		lld x;
		string s;
		cin>>x>>s;
		lld res = (s[0]=='0'), st = (s[0]=='0'?1:s[0]-'0');
		for (int i = 1; i < s.size(); i++) {
			if (i > st) {res += i - st;st=i;}
			st = st + (lld)s[i]-'0';
		}
		cout<<"Case #"<<T-t<<": "<<res<<"\n";
	}
	return 0;
}
