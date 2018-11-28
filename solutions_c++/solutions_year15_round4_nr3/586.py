#include <cstdio>
#include <set>
#include <iostream>
#include <string>
#include <vector>
#include <map>
#include <algorithm>
using namespace std;

const int Maxn=205;

string str;
map<string, int> s0, s1;
vector<string> list[Maxn];
int n, ans;

void dfs(int i, int cnt)
{
	if (cnt>=ans) return;
	if (i==n)
	{
		ans=cnt;
		return;
	}
	int cnt0=cnt;
	for (int j=0; j<(int)list[i].size(); ++j)
	{
		++s0[list[i][j]];
		if (s0[list[i][j]]==1 && s1[list[i][j]]>0) ++cnt;
	}
	dfs(i+1, cnt);
	cnt=cnt0;
	for (int j=0; j<(int)list[i].size(); ++j) --s0[list[i][j]];
	for (int j=0; j<(int)list[i].size(); ++j)
	{
		++s1[list[i][j]];
		if (s1[list[i][j]]==1 && s0[list[i][j]]>0) ++cnt;
	}
	dfs(i+1, cnt);
	for (int j=0; j<(int)list[i].size(); ++j) --s1[list[i][j]];
}

int main()
{
	int T;
	cin>>T;
	for (int tt=1; tt<=T; ++tt)
	{
		cin>>n;
		getline(cin, str);
		for (int i=0; i<n; ++i)
		{
			getline(cin, str);
			int len=str.size();
			int last=0;
			list[i].clear();
			for (int j=0; j<=len; ++j)
				if (j==len || str[j]==' ')
				{
					list[i].push_back(str.substr(last, j-last));
					last=j+1;
				}
		}
		ans=100000000;
		s0.clear();
		s1.clear();
		int cnt=0;
		for (int i=0; i<(int)list[0].size(); ++i) ++s0[list[0][i]];
		for (int i=0; i<(int)list[1].size(); ++i)
		{
			++s1[list[1][i]];
			if (s1[list[1][i]]==1 && s0[list[1][i]]>0) ++cnt;
		}
		dfs(2, cnt);
		printf("Case #%d: %d\n", tt, ans);
	}
	return 0;
}

