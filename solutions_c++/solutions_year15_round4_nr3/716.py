#include <iostream>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <set>
#include <map>
#include <vector>
#include <string>
#include <cstring>
#include <sstream>

using namespace std;

const int maxN = 210;

char s[12000];
int n;
string st;
map<string, int> words;
vector<bool> eng, fr;
vector<int> ar[maxN];

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int q;
	scanf("%d", &q);
	for (int t = 0; t < q; t++)
	{
		int cnt = 0;
		eng.clear();
		fr.clear();
		words.clear();
		scanf("%d\n", &n);
		gets(s);
		istringstream iss(s);
		ar[n - 2].clear();
		while (iss >> st)
		{
			if (words.find(st) == words.end())
			{
				words[st] = cnt++;
			}
			ar[n - 2].push_back(words[st]);
		}
		gets(s);
		iss = istringstream(s);
		ar[n - 1].clear();
		while (iss >> st)
		{
			if (words.find(st) == words.end())
			{
				words[st] = cnt++;
			}
			ar[n - 1].push_back(words[st]);
		}
		for (int i = 0; i < n - 2; i++)
		{
			ar[i].clear();
			gets(s);
			iss = istringstream(s);
			while (iss >> st)
			{
				if (words.find(st) == words.end())
				{
					words[st] = cnt++;
				}
				ar[i].push_back(words[st]);
			}
		}
		int ans = 1e9;
		for (int mask = 0; mask < (1 << (n - 2)); mask++)
		{
			fr.clear();
			eng.clear();
			fr.resize(cnt, false);
			eng.resize(cnt, false);
			int cur = 0;
			for (int i = 0; i < n - 2; i++)
			{
				for (int j = 0; j < ar[i].size(); j++)
				{
					if (mask & (1 << i))
					{
						fr[ar[i][j]] = true;
					}
					else
					{
						eng[ar[i][j]] = true;
					}
				}
			}
			for (int i = 0; i < ar[n - 2].size(); i++)
			{
				eng[ar[n - 2][i]] = true;
			}
			for (int i = 0; i < ar[n - 1].size(); i++)
			{
				fr[ar[n - 1][i]] = true;
			}
			for (int i = 0; i < cnt; i++)
			{
				cur += (fr[i] && eng[i]);
			}
			ans = min(ans, cur);
		}
		printf("Case #%d: %d\n", t + 1, ans);
	}
	return 0;
}