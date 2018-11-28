#include <iostream>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <set>
#include <map>
#include <vector>
#include <string>
#include <cstring>

using namespace std;

struct Trie{
	Trie* ar[26];

	Trie(){
		memset(ar, NULL, sizeof(ar));
	}

	~Trie()
	{
		for (int i = 0; i < 26; i++)
		{
			if (ar[i] != NULL)
				delete ar[i];
		}
	}

	int insert(char *s, int pos, int len)
	{
		if (pos == len)
		{
			return 0;
		}
		int c = s[pos] - 'A';
		if (ar[c] != NULL)
		{
			return ar[c]->insert(s, pos + 1, len);
		}
		else
		{
			ar[c] = new Trie();
			return 1 + ar[c]->insert(s, pos + 1, len);
		}
	}
};

int m, n;
char ar[20][20];
int len[20];
int kol[10];
int now[20];
Trie* roots[10];

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int q;
	scanf("%d", &q);
	for (int t = 0; t < q; t++)
	{
		int best = 0;
		int ans = 1e9;
		scanf("%d%d\n", &m, &n);
		for (int i = 0; i < m; i++)
		{
			scanf("%s", &ar[i]);
			len[i] = strlen(ar[i]);
		}
		int cnt = 1;
		for (int i = 0; i < m; i++)
		{
			cnt *= n;
		}
		for (int i = 0; i < cnt; i++)
		{
			for (int j = 0; j < n; j++)
			{
				kol[j] = 0;
			}
			int p = i;
			for (int j = 0; j < m; j++)
			{
				now[j] = p % n;
				p /= n;
				kol[now[j]]++;
			}
			bool good = true;
			for (int j = 0; j < n && good; j++)
			{
				if (roots[j] != NULL)
				{
					delete roots[j];
				}
				roots[j] = new Trie();
				if (kol[j] == 0)
					good = false;
			}
			if (!good)
			{
				continue;
			}
			int cur = n;
			for (int j = 0; j < m; j++)
			{
				cur += roots[now[j]]->insert(ar[j], 0, len[j]);
			}
			if (cur > best)
			{
				best = cur;
				ans = 0;
			}
			ans += (cur == best);
		}
		printf("Case #%d: %d %d\n", t + 1, best, ans);
	}
	return 0;
}