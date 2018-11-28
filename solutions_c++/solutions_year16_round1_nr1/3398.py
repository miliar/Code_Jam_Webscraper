#include <bits/stdc++.h>
using namespace std;
int main() {
	freopen ("A-large.in","r",stdin);
	freopen ("A-large.out","w",stdout);
	int t;
	cin>>t;
	string s;
	for(int tc = 1; tc <= t; tc++) {
		cin>>s;
		list<char> sol;
		list<char>::iterator it = sol.begin();
		sol.insert(it,s[0]);

		for(int i = 1; i < s.size();i++){
			it = sol.begin();
			if(s[i] < *it){
				it = sol.end();
			}
			sol.insert(it,s[i]);
		}
		cout<<"Case #"<<tc<<": ";
		for(it = sol.begin(); it != sol.end();it++)cout<<*it;
		cout<<endl;
	} 
	return 0;
}