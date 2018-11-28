#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<math.h>
#include<time.h>
#include<string>
#include<set>
#include<map>
#include<vector>
#include<algorithm>
#include<iostream>
#include<queue>
using namespace std;

char w[4005][15];
char s[2005 * 15];
char ow[15];
int sz;

vector<vector<int> > a;
int b[4005][2];
int cur = 1;

int tp[25];
int res = 1000000000;
int n;
void func(int p)
{
	if (p == n - 2)
	{
		for (int i = 0; i < n; i++)
		{
			for (int j = 0; j < a[i].size(); j++)
			{
				b[a[i][j]][tp[i]] = cur;
			}
		}

		int t = 0;
		for (int i = 0; i < sz; i++)
		{
			if (b[i][0] == cur && b[i][1] == cur)
				t++;
		}
		res = min(res, t);

		cur++;
		return;
	}
	tp[p+2] = 0;
	func(p + 1);
	tp[p+2] = 1;
	func(p + 1);
}

int main()
{
	freopen("C.in", "r", stdin);
	freopen("C.out", "w", stdout);

	int TT;
	scanf("%d", &TT);
	for (int T = 0; T < TT; T++)
	{
		printf("Case #%d: ", T + 1);
		scanf("%d", &n);
		gets(s);
		a.clear();
		a.resize(n);
		sz = 0;
		for (int t = 0; t < n; t++)
		{
			gets(s);
			int len = strlen(s), p = 0;
			while (p < len)
			{
				while (s[p] == ' ')
					p++;
				if (s[p] == 0)
					break;
				sscanf(s + p, "%s", ow);
				p += strlen(ow);
				int id = -1;
				for (int i = 0; i < sz; i++)
				{
					if (strcmp(ow, w[i]) == 0)
					{
						id = i;
						break;
					}
				}
				if (id == -1)
				{
					id = sz++;
					strcpy(w[id], ow);
				}
				a[t].push_back(id);
			}
		}
		res = 1000000000;
		tp[0] = 0;
		tp[1] = 1;
		func(0);
		printf("%d\n", res);
	}

	return 0;
}