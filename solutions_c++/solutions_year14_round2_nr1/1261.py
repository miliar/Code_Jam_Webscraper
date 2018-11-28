#include <iostream>
#include <stdio.h>
#include <vector>
#include <string.h>
#include <algorithm>
using namespace std;
inline int ab(int n)
{
	return n>0?n:-n;
}
int main()
{
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	int t,k,n,i,j,a,ans;
	string s[100];
	vector<char> v;
	vector<pair<char,int> > c[100];
	vector<int> d[100];
	cin>>t;
	for (k=1;k<=t;k++)
	{
		cin>>n;
		memset(c,0,sizeof(c));
		for (i=0;i<n;i++) cin>>s[i];
		v.clear();
		for (i=0;i<s[0].size();i++)
			if (v.empty()||s[0][i]!=v[v.size()-1]) v.push_back(s[0][i]);
		for (i=0;i<n;i++)
		{
			c[i].clear();
			c[i].push_back(make_pair(s[i][0],1));
			for (j=1;j<s[i].size();j++)
				if (s[i][j]==s[i][j-1]) c[i][c[i].size()-1].second++;
				else c[i].push_back(make_pair(s[i][j],1));
			if (c[i].size()!=v.size()) break;
		}
		cout<<"Case #"<<k<<": ";
		if (i<n) cout<<"Fegla Won"<<endl;
		else{
		ans=0;
		for (a=0;a<v.size();a++)
		{
			d[a].clear();
			for (i=0;i<n;i++)
			{
				if (c[i][a].first!=v[a]) break;
				d[a].push_back(c[i][a].second);
			}
			if (i<n) break;
			sort(d[a].begin(),d[a].end());
			for (i=0;i<n;i++) ans+=ab(d[a][i]-d[a][n/2]);
		}
		if (a<v.size()) cout<<"Fegla Won"<<endl;
		else cout<<ans<<endl;}
	}
	return 0;
}
