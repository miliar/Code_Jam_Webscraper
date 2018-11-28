#include <bits/stdc++.h>
using namespace std;
#define int long long 
const int F=10;
int n=32,j=500;
map<string,vector<int> > m;
string to_str(int e,int len) {
	string res;
	while(len--) {
		int d=e%2;
		e/=2;
		res=(d?"1":"0")+res;
	}
	return res;
}
signed main() {
	ios_base::sync_with_stdio(false);
	cin.tie(nullptr);
	cout<<"Case #1:\n";
	for(int len=2;len<n;++len) {
		if(n%len==0) {
			for(int i=1;i<(1<<len);++i) {
				string s=to_str(i,len);
				if(s[0]==s.back() && s[0]=='1') {
					string t;
					for(int j=0;j<n/len;++j) {
						t+=s;
					}
					if(m.find(t)==m.end()) {
						m[t].resize(F+1);
						for(int k=2;k<=F;++k) {
							m[t][k]=stoll(s,nullptr,k);
						}
					}
				}
			}
		}
	}
	for(auto i:m) {
		if(!j) break;
		j--;
		cout<<i.first<<" ";
		for(auto j:i.second) {
			if(j) cout<<j<<" ";
		}
		cout<<"\n";
	}
	return 0;
}
