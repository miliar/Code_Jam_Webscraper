#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstring>
#define int64 long long
#define Sort sort
#define next NEXT

using namespace std;

const int dir_x[4] = {-1, 0, 1, 0};
const int dir_y[4] = {0, 1, 0, -1};

int a[110][110];
int cnt[110][110];
int next[110][110];
int N, M;

int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);

	int T;
	scanf("%d", &T);
	for (int ii=0;ii<T;++ii)
	{
		scanf("%d%d",&N, &M);
		for (int i=0;i<N;++i)
		{
			char st[110];
			scanf("%s", st);
			for (int j=0;j<M;++j)
			{
				if (st[j] == '.') a[i][j] = 4;
				if (st[j] == '^') a[i][j] = 0;
				if (st[j] == '>') a[i][j] = 1;
				if (st[j] == 'v') a[i][j] = 2;
				if (st[j] == '<') a[i][j] = 3;
			}
		}
		for (int i=0;i<N;++i)
			for (int j=0;j<M;++j)
				next[i][j] = cnt[i][j] = 0;
		int ans = 0;
		for (int i=0;i<N && ans != -1;++i)
			for (int j=0;j<M && ans != -1;++j)
			{
				if (a[i][j] == 4) continue;
				int can = 0;
				for (int dir = 0;dir < 4;++dir)
				{
					int nx = i + dir_x[dir], ny = j + dir_y[dir];
					next[i][j] = -1;
					for (;nx>=0 && nx<N && ny>=0 && ny<M;)
					{
						if (a[nx][ny] < 4)
						{
							can |= 1 << dir;
							break;
						}
						nx += dir_x[dir], ny += dir_y[dir];
					}
				}
				if (can == 0) ans = -1;
				else
				{
					if (can & (1 << a[i][j])) ans += 0;
					else ans += 1;
				}
			}

		printf("Case #%d: ", ii + 1);
		if (ans == -1) printf("IMPOSSIBLE\n");
		else printf("%d\n", ans);
	}

	return 0;
}