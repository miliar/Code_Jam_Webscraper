#include<bits/stdc++.h>

#define MOD 1000000007

using namespace std;

typedef long long ll;
typedef pair<ll,ll> pr;

map<pr,ll> mp;


int main(){

	ios_base::sync_with_stdio(false);
	int t;
	cin>>t;
	for(int i=0;i<t;i++){
		string s;
		cin>>s;
		string ans=s.substr(0,1);
		for(int j=1;j<s.size();j++){
			string tmp1,tmp2;
			tmp1=ans+s.substr(j,1);
			tmp2=s.substr(j,1)+ans;
			ans=tmp1>tmp2?tmp1:tmp2;
		}
		printf("Case #%d: %s\n",i+1,ans.c_str());
	}
}
