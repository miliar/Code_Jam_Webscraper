#include <cstdio>
#include <cstdlib>
#include <ctime>
#include <cstring>
#include <cmath>
#include <algorithm>
#include <set>
#include <map>
#include <vector>

#define mp make_pair
#define pb push_back

using namespace std;

typedef long long ll;

const int inf = 0x3f3f3f3f;

char ch[4] = {'R', 'S', 'P'};
int cnt[101];

vector<char> dfs(int deep, int cur, int sz)
{
	vector<char> tmp;
	tmp.clear();
	if (sz == 1)
	{
		tmp.pb(ch[cur]);
		cnt[cur] ++;
		return tmp;
	}
	vector<char> x, y;
	x = dfs(deep + 1, cur, sz >> 1);
	y = dfs(deep + 1, (cur + 1) % 3, sz >> 1);
	int type = 0;
	for (int i = 0; i < sz / 2; i ++)
	{
		char xx = x[i], yy = y[i];
		if (xx < yy) { type = 1; break; }
		if (xx > yy) { type = 2; break; }
	}
	if (type == 1)
	{
		for (int i = 0; i < sz / 2; i ++)
			tmp.pb(x[i]);
		for (int i = 0; i < sz / 2; i ++)
			tmp.pb(y[i]);
	}
	else
	{
		for (int i = 0; i < sz / 2; i ++)
			tmp.pb(y[i]);
		for (int i = 0; i < sz / 2; i ++)
			tmp.pb(x[i]);
	}
	return tmp;
}

int main( )
{
	int T, n, r, p, s, tp = 0;
	scanf("%d", &T);
	while (T --)
	{
		scanf("%d %d %d %d", &n, &r, &p, &s);
		int N = (1 << n);
		vector<char> x, y, tmp;
		x.clear(), y.clear();
		int sum = 0;
		for (int i = 0; i < 3; i ++)
		{
			for (int j = 0; j < 3; j ++) cnt[j] = 0;
			tmp = dfs(1, i, N);
			if (r == cnt[0] && s == cnt[1] && p == cnt[2])
			{
				if (sum == 0) x = tmp;
				else y = tmp;
				++ sum;
			}
		}
		++ tp;
		printf("Case #%d: ", tp);
		if (sum == 0) printf("IMPOSSIBLE\n");
		else if (sum == 1)
		{
			for (int i = 0; i < N; i ++)
				printf("%c", x[i]);
			printf("\n");
		}
		else
		{
			int type = 0;
			for (int i = 0; i < N; i ++)
			{
				if (x[i] < y[i]) { type = 1; break; }
				if (x[i] > y[i]) { type = 2; break; }
			}
			if (type == 1)
			{
				for (int i = 0; i < N; i ++)
					printf("%c", x[i]);
			}
			else
			{
				for (int i = 0; i < N; i ++)
					printf("%c", y[i]);
			}
			printf("\n");
		}
	}
	return 0;
}
