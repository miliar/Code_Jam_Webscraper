#include <bits/stdc++.h>
using namespace std;
const int N = 107;
int n, t;
string s;
int main()
{
	#ifndef ONLINE_JUDGE
		freopen("I.in","r",stdin);
		freopen("O.out","w",stdout);
	#endif
	cin>>t;
	for(int casen = 1; casen <= t; casen++) {
		cout<<"Case #"<<casen<<": ";
		cin>>s;
		int c = 1;
		for(int i=1;s[i];i++) {
			if(s[i] != s[i-1]) c++;
		}
		if(s[0] == '+') {
			if(c&1) cout<<c-1<<'\n';
			else cout<<c<<'\n';
		} else {
			if(c&1) cout<<c<<'\n';
			else cout<<c-1<<'\n';
		}
	}
	return 0;
}