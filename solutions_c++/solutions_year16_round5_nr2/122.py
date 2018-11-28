#include<stdio.h>
#include<vector>
#include<algorithm>
#include<string>
#include<iostream>
using namespace std;
int par[110];
vector<int>ko[110];
double com[110][110];
double dp[110];
int siz[110];
void dfs(int node)
{
	siz[node] = 1;
	for (int i = 0; i < ko[node].size(); i++)
	{
		dfs(ko[node][i]);
		siz[node] += siz[ko[node][i]];
	}
	double now = 1;
	int s = 0;
	for (int i = 0; i < ko[node].size(); i++)
	{
		now *= dp[ko[node][i]] * com[s + siz[ko[node][i]]][s];
		s += siz[ko[node][i]];
	}
	dp[node] = now;
}
long long rrr = 2463534242LL;
int getrand(int mod)
{
	rrr = (rrr ^ (rrr << 13))&((1LL << 32) - 1); rrr = rrr ^ (rrr >> 17);
	rrr = (rrr ^ (rrr << 5))&((1LL << 32) - 1);
	return rrr%mod;
}
int main()
{
	freopen("b-small-attempt0.in", "r", stdin);
	freopen("out.txt", "w",stdout);
	int data;
	scanf("%d", &data);
	for (int i = 0; i < 110; i++)
	{
		com[i][0] = 1;
		for (int j = 1; j <= i; j++)com[i][j] = com[i - 1][j - 1] + com[i - 1][j];
	}
	for (int p = 1; p <= data; p++)
	{
		for (int i = 0; i < 110; i++)
		{
			par[i] = 0;
			ko[i].clear();
			dp[i] = 0;
		}
		int num;
		scanf("%d", &num);
		for (int i = 0; i < num; i++)scanf("%d", &par[i + 1]);
		string str;
		cin >> str;
		num++;
		for (int i = 1; i < num; i++)ko[par[i]].push_back(i);
		dfs(0);
		double ans[5];
		fill(ans, ans + 5, 0);
		//for (int i = 0; i < num; i++)printf("%lf ", dp[i]); printf("\n");
		int query;
		scanf("%d", &query);
		vector<string>dat;
		for (int i = 0; i < query; i++)
		{
			string s;
			cin >> s;
			dat.push_back(s);
		}
		for (int q = 0; q < 3000; q++)
		{
			bool flag[110];
			fill(flag, flag + 110, false);
			flag[0] = true;
			string g;
			for (int i = 1; i < num; i++)
			{
				vector<int>vec;
				vector<double>d;
				for (int j = 0; j < num; j++)
				{
					if (flag[par[j]] && (!flag[j]))
					{
						vec.push_back(j);
						d.push_back(double(siz[j]) / double(num-i));
					}
				}
				double r = getrand(114514) / 114513.0;
				double sum = 0.0;
				int rr = -1;
				for (int j = 0; j < vec.size(); j++)
				{
					sum += d[j];
					if (sum > r - (1e-9))
					{
						rr = vec[j];
						break;
					}
				}
			//	printf("\n");
				g.push_back(str[rr-1]);
				flag[rr] = true;
			}
			//if (q <= 30)cout << g << endl;
			for (int j = 0; j < query; j++)
			{
				for (int k = 0; k < g.size(); k++)
				{
					bool f = true;
					for (int l = 0; l < dat[j].size(); l++)
					{
						if (k + l >= g.size())
						{
							f = false;
							break;
						}
						if (g[k + l] != dat[j][l])
						{
							f = false;
							break;
						}
					}
					if (f)
					{
						ans[j]++;
						break;
					}
				}
			}
		}
		printf("Case #%d:", p);
		for (int i = 0; i < query; i++)
		{
			printf(" %lf", double(ans[i]) / double(3000));
		}
		printf("\n");
	}
}