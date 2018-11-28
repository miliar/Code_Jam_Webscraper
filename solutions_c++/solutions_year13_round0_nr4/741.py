//============================================================================
// Name        : D.cpp
// Author      : kangaroo
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <cstring>
#include <cstdio>
#include <vector>
using namespace std;

const int maxn = 20;
const int keynum = 201;

int keycnt[keynum];
vector<int> contains[maxn];
int keyType[maxn];
bool h[1 << maxn], ok[1 << maxn];
int n;

void getKeys(int state, int (&a)[keynum])
{
	memcpy(a, keycnt, sizeof(keycnt));
	for (int i = 0; i < n; ++i)
		if (state & (1 << i))
		{
			a[keyType[i]]--;
			for (unsigned int j = 0; j < contains[i].size(); ++j)
				a[contains[i][j]]++;
		}
}

bool check(int state)
{
	if (state == (1 << n) - 1)
		return true;
	if (h[state])
		return ok[state];
	int a[keynum];
	getKeys(state, a);
	for (int i = 0; i < n; ++i)
		if ((state & (1 << i)) == 0 && a[keyType[i]] > 0)
			if (check(state | (1 << i))) {
				h[state] = true;
				ok[state] = true;
				return true;
			}
	h[state] = true;
	ok[state] = false;
	return false;
}

int result[maxn];

int main() {
	freopen("D-small-attempt0.in", "r", stdin);
	freopen("D-small-attempt0.out", "w", stdout);
	int T;
	scanf("%d", &T);
	for (int casenum = 1; casenum <= T; ++casenum)
	{
		int k;
		scanf("%d %d", &k, &n);
		memset(keycnt, 0, sizeof(keycnt));
		for (int i = 0; i < k; ++i)
		{
			int t;
			scanf("%d", &t);
			keycnt[t]++;
		}

		memset(contains, 0, sizeof(contains));
		for (int i = 0; i < n; ++i)
		{
			scanf("%d", &keyType[i]);
			int cnt;
			scanf("%d", &cnt);
			contains[i].clear();
			for (int j = 0; j < cnt; ++j)
			{
				int key;
				scanf("%d", &key);
				contains[i].push_back(key);
			}
		}

		memset(h, false, sizeof(h));
		memset(ok, false, sizeof(ok));

		printf("Case #%d:", casenum);
		int state = 0;
		bool hasSol = true;
		int curnum[keynum];
		memcpy(curnum, keycnt, sizeof(keycnt));

		for (int t = 0; t < n; ++t)
		{
			hasSol = false;
			for (int i = 0; i < n; ++i)
				if ((state & (1 << i)) == 0 && curnum[keyType[i]] > 0)
				{
					if (check(state | (1 << i)))
					{
						state |= 1 << i;
						result[t] = i;
						hasSol = true;
						curnum[keyType[i]]--;
						for (unsigned int j = 0; j < contains[i].size(); ++j)
							curnum[contains[i][j]]++;
						break;
					}
				}
			if (!hasSol) break;
		}
		if (!hasSol)
			printf(" IMPOSSIBLE\n");
		else
		{
			for (int i = 0; i < n; ++i)
				printf(" %d", result[i] + 1);
			printf("\n");
		}
	}

	return 0;
}
