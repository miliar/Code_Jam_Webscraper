#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <ctime>
#include <iostream>
#include <algorithm>
#include <set>
#include <map>
#include <vector>
#include <string>
#include <queue>
#include <stack>
#include <cassert>
#include <ctime>
using namespace std;
typedef long long LL;
#define For(i,a,b) for (int i = (a); i <= (b); i++)
#define Cor(i,a,b) for (int i = (a); i >= (b); i--)
#define rep(i,a) for (int i = 0; i < a; i++)
#define Fill(a,b) memset(a,b,sizeof(a))
vector<int> pos;
int a[3];
string ans;

void bfs(int s, int n)
{
	queue<pair<int, int> > Q;
	Q.push(make_pair(s, 0));
	while (!Q.empty())
	{
		pair<int, int> u = Q.front(); Q.pop();
		if (u.second == n)
			pos.push_back(u.first);
		else
		{
			int w = u.first, d = u.second;
			if (w == 0)
			{
				Q.push(make_pair(0, d + 1));
				Q.push(make_pair(1, d + 1));
			}
			if (w == 1)
			{
				if (d == n - 1)
				{
					Q.push(make_pair(1, d + 1));
					Q.push(make_pair(2, d + 1));
				}
				else
				{
					Q.push(make_pair(2, d + 1));
					Q.push(make_pair(1, d + 1));
				}
			}
			if (w == 2)
			{
				Q.push(make_pair(0, d + 1));
				Q.push(make_pair(2, d + 1));
			}
		}
	}
}
vector<string> v;
string adjust(string s, int n)
{
	int m = 1 << n;
	for (int i = 0; i < n; i++)
	{
		v.clear();
		int t = 1 << i;
		for (int j = 0; j < m; j += t)
		{
			string tmp = "";
			for (int k = 0; k < t; k++)
				tmp += s[j + k];
			v.push_back(tmp);
		}
		for (int j = 0; j < v.size(); j += 2)
			if (v[j] > v[j + 1])
				swap(v[j], v[j + 1]);
		s = "";
		for (int j = 0; j < v.size(); j++)
			s += v[j];
	}
	return s;
}
void solve(int task)
{
	printf("Case #%d: ", task);
	int n, p, r, s;
	scanf("%d%d%d%d", &n, &r, &p, &s);
	ans = "";
	for (int i = 0; i < 3; i++)
	{
		pos.clear();
		a[0] = a[1] = a[2] = 0;
		bfs(i, n);
		for (int j = 0; j < pos.size(); j++)
			a[pos[j]]++;
		if (a[0] != p || a[1] != r || a[2] != s)
			continue;
		string s = "";
		for (int j = 0; j < pos.size(); j++)
		{
			if (pos[j] == 0)
				s += "P";
			if (pos[j] == 1)
				s += "R";
			if (pos[j] == 2)
				s += "S";
		}
		s = adjust(s, n);
		if (ans == "" || ans > s)
			ans = s;
	}
	if (ans == "")
		printf("IMPOSSIBLE\n");
	else
		cout << ans << endl;
}
int main()
{
	freopen("a.in", "r", stdin);
	freopen("a1.out", "w", stdout);
	int T;
	scanf("%d", &T);
	for (int i = 1; i <= T; i++)
		solve(i);
}
