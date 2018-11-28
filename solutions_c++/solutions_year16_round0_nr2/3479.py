#include<bits/stdc++.h>
#define endl "\n"
using namespace std;
typedef long long ll;
int a[10];
int main(){	
	ios_base::sync_with_stdio(0);
	int T;
	cin>>T;
	for(int xx=1;xx<=T;xx++){
		string s;
		cin>>s;
		ll changes=0;
		for(int i=1;i<s.size();i++){
			if(s[i]!=s[i-1])changes++;
		}
		if(s[s.size()-1]=='-')changes++;
		cout<<"Case #"<<xx<<": "<<changes<<engdl;
	}
	return 0;
}