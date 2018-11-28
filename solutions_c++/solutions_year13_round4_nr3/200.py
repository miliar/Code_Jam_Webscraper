#include <cstdio>
#include <iostream>
#include <algorithm>
#include <numeric>
#include <string>
#include <map>
#include <vector>
#include <cmath>

using namespace std;

int num[20];
int a[20], b[20];
bool finished;
bool u[20];
int dp[20];
void rec(int pos, int end)
{
	if (finished) return ;
	if (pos == end)
	{
		for(int st = 0; st < end; st++)
		{
			int longest = 1;
			dp[st] = 1;
			for(int i = st + 1; i < end; i++)
			{
				dp[i] = 0;
				for(int j = st; j < i; j++)
					if (num[i] < num[j] && dp[j] > 0)
						longest = max(longest, dp[i] = max(dp[i], dp[j] + 1));
			}
			if (longest != b[st]) return ;
		}
		for(int i = 0; i < end; i++)
			printf(" %d", num[i] + 1);
		puts("");
		finished = true;
		return ;
	}
	for(int cur = 0; cur < end; cur++)
	{
		if (u[cur]) continue;
		
		int more = 0, free = 0;
		for(int i = cur + 1; i < end; i++)
			more += !u[i];
		for(int i = pos + 1; i < end; i++)
			if (a[i] > a[pos])
				free++;
		if (more > free) continue;

		int less = 0;
		free = 0;
		for(int i = 0; i < cur; i++)
			less += !u[i];
		for(int i = pos + 1; i < end; i++)
			if (b[i] < b[pos])
				++free;
		if (less > free) continue;


		/*more = 0;
		for(int i = 0; i < cur; i++)
			more += u[i];
		if (more > 0)
			for(int i = pos + 1; i < end; i++)
				if (b[i] >= b[cur])
					more = 0;
		if (more == 0) continue;*/

		int longest = 1;
		dp[pos] = 1;
		num[pos] = cur;
		for(int i = pos - 1; i >= 0; i--)
		{
			dp[i] = 0;
			for(int j = i + 1; j <= pos; j++)
				if (num[i] < num[j] && dp[j] > 0)
					longest = max(longest, dp[i] = max(dp[i], dp[j] + 1));
		}
		if (longest != a[pos]) continue;
		u[cur] = true;
		rec(pos + 1, end);
		u[cur] = false;
	}

}

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int T, t, n, i, j, k;
	long long p;

	cin >> T;
	for(t = 1; t <= T; t++)
	{
		cin >> n;
		for(i = 0; i < n; i++)
			cin >> a[i];
		for(i = 0; i < n; i++)
			cin >> b[i];
		printf("Case #%d:", t);
		finished = false;
		rec(0, n);
	}

	return 0;
}