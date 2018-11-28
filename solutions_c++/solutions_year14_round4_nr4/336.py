#include <stdio.h>
#include <string.h>
#include <algorithm>
#include <map>
#include <vector>
using namespace std;

int n, m;
char str[10][20];
int split[10];
int cnt[500];

struct node
{
	int vcnt;
	node* edge[26];
} memo[200];
int pos = -1;
node* root;

void addString(node* root, char* word)
{
	int i, len;
	node* cur = root;
	for (i = 0, len = strlen(word); i < len; i++) {
		int eidx = word[i] - 'A';
		if (cur->edge[eidx] == NULL) {
			cur->edge[eidx] = &memo[++pos];
		} cur = cur->edge[eidx];
	} cur->vcnt++;	//统计匹配的子串个数
}

int work()
{
	int i, j, ret = 0;
	for (i = 0; i < n; i++)
	{
		memset(memo, 0, sizeof memo);
		pos = -1;
		root = &memo[++pos];
		for (j = 0; j < m; j++)
			if (split[j] == i)
			{
				// printf("\t\t%s\n", str[j]);
				addString(root, str[j]);
			}
		if (pos >= 1)
			ret += (pos + 1);
		// printf("\t\ti = %d, pos = %d, ret = %d\n", i, pos, ret);
	}
	return ret;
}

int main()
{
	int t, cas;
	int i, j, tot, x, y;
	scanf("%d", &t);
	for (cas = 1; cas <= t; cas++)
	{
		memset(cnt, 0, sizeof cnt);
		scanf("%d%d", &m, &n);
		tot = 1;
		for (i = 0; i < m; i++) tot *= n;
		for (i = 0; i < m; i++) scanf("%s", str[i]);
		for (i = 0; i < tot; i++)
		{
			int msk = i;
			for (j = 0; j < m; j++)
			{
				split[j] = msk % n;
				msk /= n;
			}
			int num = work();
			// for (j = 0; j < m; j++) printf("%d ", split[j]); printf("\n");
			// printf("\ti = %d, num = %d\n", i, num);
			cnt[num]++;
		}
		for (i = m * 15; i >= 0; i--)
			if (cnt[i] > 0)
				{ x = i; y = cnt[i]; break; }
		printf("Case #%d: %d %d\n", cas, x, y);
	}
	return 0;
}
