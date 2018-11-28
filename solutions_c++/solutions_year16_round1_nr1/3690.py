#include<bits/stdc++.h>
using namespace std;

int main() {
	ios::sync_with_stdio(false);
	int t;
	cin>>t;
	string s;
	for ( int k=1;k<=t;k++ ) {
		cin>>s;
		list<char> ans;
		int l=s.length();
		ans.push_back(s[0]);
		for ( int i=1;i<l;i++ ) {
            if ( ans.front()<=s[i] ) {
				ans.push_front(s[i]);
            }
            else {
				ans.push_back(s[i]);
            }
		}
		cout<<"Case #"<<k<<": ";
		std::list<char>::iterator it;
		for ( it=ans.begin();it!=ans.end();it++ ) {
			cout<<*it;
		}
		cout<<"\n";
	}
	return 0;
}
