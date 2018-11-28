#include<iostream>
#include<algorithm>
#include<string.h>
#include<vector>
#include<iomanip>
#include<set>
using namespace std;

#define MAXN 105

int server[MAXN];

vector<string> str;
long long ans, cnt;
int n, m;

void dfs(int cur)
{
	if(cur == n)
	{
/*		server[0] = 0;
		server[1] = 1;
		server[2] = 1;
		server[3] = 0;*/
		vector<string> di[10];
		for(int i = 0; i < n; ++i)
		{
			di[server[i]].push_back(str[i]);
		}
		
		for(int i = 0; i < m; ++i)
			if(di[i].size() == 0)
				return;
			
		int curans = 0;	
		for(int i = 0; i < m; ++i)
		{
			set<string> s;
			for(int j = 0; j < di[i].size(); ++j)
			{
				string tmp = "";
				for(int k = 0; k < di[i][j].size(); ++k)
				{	
					tmp += di[i][j][k];
					s.insert(tmp);
				}
			}
			curans += (s.size() + 1);
		}
		
		if(curans == ans)
			cnt++;
		else if(curans > ans)
		{
			ans = curans;
			cnt = 1;
		}
		return;
	}
	
	for(int i = 0; i < m; ++i)
	{
		server[cur] = i;
		dfs(cur+1);
	}
	return;
}

int main()
{
		freopen("d:\\4.in", "r", stdin);
	freopen("d:\\4-ans.txt", "w", stdout);
	
	int T;
	cin>>T;
	for(int kase = 1; kase <= T; ++kase)
	{
		ans = 0;
		cin>>n>>m;
		str.clear();
		for(int i = 0; i < n; ++i)
		{
			string a;
			cin>>a;
			str.push_back(a);
		}
		
		dfs(0);
		
		cout<<"Case #"<<kase<<": "<<ans<<" "<<cnt<<endl;
	}
	return 0;
}
