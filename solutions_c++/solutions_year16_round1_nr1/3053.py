#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <map>
#include <unordered_map>
#include <set>
#include <unordered_set>
#include <queue>
#include <stack>
#include <algorithm>
using namespace std;
int compare(string a,string b,int len)
{
	for(int i = 0; i < len; ++i)
	{
		if(a[i] == b[i])
			continue;
		else if(a[i] < b[i])
			return -1;
		else
			return 1;
	}
	return 0;
}
void dfs(string &ans,string &s,int id, string cur,int len)
{
	if(id == len)
	{
		if(compare(cur,ans,len) == 1)
			ans = cur;
		return;
	}
	if(id > 0 && s[id] >= cur[0])
		dfs(ans,s,id+1,s[id] + cur,len);
	else
		dfs(ans,s,id+1,cur + s[id],len);
}
int main()
{
	freopen("in.txt","r",stdin);
	freopen("a_out.txt","w",stdout);
	int T;
	int cas = 0;
	scanf("%d",&T);
	string s;
	while(T--)
	{
		cin >> s;
		string ans = s;
		dfs(ans,s,0,"",s.length());
		printf("Case #%d: ",++cas);
		cout << ans << endl;
	}
	return 0;
}
