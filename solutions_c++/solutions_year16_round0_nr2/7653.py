//By SCJ
#include<bits/stdc++.h>
using namespace std;
int main()
{
//ios::sync_with_stdio(0);
//cin.tie(0);
	int T;cin>>T;
	for(int ca=1;ca<=T;++ca)
	{
		string s;cin>>s;
		vector<char> v;
		v.push_back(s[0]);
		for(int i=1;i<s.size();++i)
		{
			if(s[i]!=s[i-1]) v.push_back(s[i]);
		}
		int ans;
		if(v[v.size()-1]=='+') ans=v.size()-1;
		else ans=v.size();
		printf("Case #%d: %d\n",ca,ans);
	}
}
