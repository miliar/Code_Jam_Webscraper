
#include <iostream>
#include <string>
#include <vector>
#include <stack>
#include <queue>
#include <set>
#include <map>
#include <utility>
#include <algorithm>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cstring>
#include <climits>
using namespace std;

const int mx = 1000+10;
int n, m;
string str[100];
int cnt[100],belong[100];
int mxans, mxcnt;

struct Node
{
	char ch;
	int next[26];
	Node(){ ch = '0'; memset(next, 0, sizeof(next));}
}node[10000];
int tot;

int g(int x)
{
	int ret = 1;
	for (int i = 0; i < 26; i++)
		if (node[x].next[i] != 0)
			ret += g(node[x].next[i]);
	return ret;
}

void f(int x)
{
	if (x == m)
	{
		for (int i = 1; i <= n;i++) if(cnt[i] == 0) return;

		int ret = 0;
		for (int i = 1; i <= n; i++)
		{
			tot = 1;
			for (int i = 0; i < 26; i++) node[0].next[i] = 0;
			for (int j = 0; j < m; j++) if(belong[j] == i)
			{
				int p = 0; 
				string s = str[j]; //cout<<s<<" ";;
				for (int k = 0; k < s.length(); k++)
				{
					int t = s[k] - 'A';
					if (node[p].next[t] == 0)
					{
						for (int kk = 0; kk < 26; kk++) node[tot].next[kk] = 0;
						node[p].next[t] = tot++;
						p = node[p].next[t];
					}
					else
						p = node[p].next[t];
				}
			}		
			ret += g(0); //cout<<g(0)<<endl;
		}
		
		if (ret > mxans) mxans = ret, mxcnt= 1;
		else if(ret == mxans) mxcnt++;
		return;

	}
	for (int i = 1; i <= n; i++)
	{
		belong[x] = i, cnt[i]++;
		f(x+1);
		cnt[i]--;
	}
}

int main ()
{
	freopen("data.in", "r", stdin);
	freopen("data.out", "w", stdout);
	int TC; scanf("%d", &TC);
	for (int tc = 1; tc <= TC; tc++)
	{
		scanf("%d%d", &m, &n);
		char tem[20];
		for (int i = 0; i < m; i++) scanf("%s", tem), str[i] = string(tem);
		memset(cnt, 0, sizeof(cnt));
		memset(belong, 0, sizeof(belong));
		mxans = -1, mxcnt = -1;
		f(0);
		printf("Case #%d: %d %d\n", tc, mxans, mxcnt);
	}

}