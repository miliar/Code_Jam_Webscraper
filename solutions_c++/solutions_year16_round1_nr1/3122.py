#include<bits/stdc++.h>
#define ll long long
using namespace std;
vector<string> v;
string s;
ll n;

int main() {
	freopen("inAs.txt", "r", stdin);
	freopen("outAs.txt", "w", stdout);
	ll t;
	cin>>t;
	for(int cases = 1; cases <=t; cases++) {
		cin>>s;
		n = s.size();
		string temp;
		temp.push_back(s[0]);
		cout<<"Case #"<<cases<<": ";
		for(int i=1;i<n;i++) {
			if(s[i] >= temp[0]) {
				temp = s[i] + temp;
			}
			else {
				temp += s[i];
			}
		}
		cout<<temp<<"\n";
	}
	return 0;
}