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
using namespace std;
int dfs(string s)
{
	int len = s.length();
	int ans = 0;
	for(int i = 0; i < len - 1; ++i)
		if(s[i] != s[i+1])
			ans++;
	if(s[len-1] == '-')
		ans++;
	return ans;
}
int main()
{
	freopen("in.txt","r",stdin);
	freopen("a_out.txt","w",stdout);
	int T;
	int cas = 0;
	scanf("%d",&T);
	while(T--)
	{
		string s;
		unordered_map<string,int> dict;
		cin >> s;
		printf("Case #%d: %d\n",++cas,dfs(s));
	}
	return 0;
}
