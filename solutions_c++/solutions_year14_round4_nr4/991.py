#include<iostream>
#include<cstdio>
#include<string>
#include<set>
#include<algorithm>
#include<vector>
#include<map>
#include<cmath>
#include<queue>
using namespace std;

int n, m;
string s[100];
int loc[100];
int ans[100000];

vector<string> S[100];
set<string> pref;

void add(string s)
{
	int len = s.size();
	for (int i = 0; i < len; i++)
		pref.insert(s.substr(0, i + 1));
}

int calc()
{
	for (int i = 0; i < n; i++)
		S[i].clear();
	for (int i = 0; i < m; i++)
		S[loc[i]].push_back(s[i]);

	for (int i = 0; i < n; i++)
		if (S[i].size() == 0)
			return 0;

	int res = 0;
	for (int i = 0; i < n; i++)
	{
		pref.clear();
		for (int j = 0; j < S[i].size(); j++)
			add(S[i][j]);
		res += pref.size() + 1;
	}
	return res;
}

void brute(int i)
{
	if (i == m)
	{
		ans[calc()]++;
		return;
	}

	
	for (int serv = 0; serv < n; serv++)
	{
		loc[i] = serv;
		brute(i + 1);
	}
}

void Solution()
{
	cin >> m >> n;
	for (int i = 0; i < m; i++)
		cin >> s[i];
	for (int i = 0; i < 100000; i++)
		ans[i] = 0;

	brute(0);

	for (int i = 100000 - 1; i >= 0; i--)
		if (ans[i] > 0)
		{
			cout << i << " " << ans[i];
			break;
		}
}

int main()
{
#ifdef LOCAL
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);
#endif

	int T;
	cin >> T;
	for (int t = 1; t <= T; t++)
	{
		printf("Case #%d: ", t);
		Solution();
		printf("\n");
	}
}