#include <cstdio>
#include <cstring>
#include <algorithm>
#include <vector>
#include <algorithm>

const int MAX_M = 1000, MAX_L = 101;
const long long MOD = 1000000007;
char strs[MAX_M][MAX_L];
int M, N;

void solve()
{
	int ans_max = -1, ans_cnt = 0;

	for (int s = 0; s < (1 << M * 2); ++s)
	{
		bool ok = true;
		int where[MAX_M];
		for (int j = 0; j < M; ++j)
		{
			where[j] = ((s >> j * 2) & 3);
			if (where[j] >= N)
			{
				ok = false;
				break;
			}
		}
		if (!ok) continue;

//		for (int i = 0; i < M; ++i)
//		{
//			printf("%d ", where[i]);
//		}
//		puts("");

		int sum = 0;
		for (int which = 0; which < N; ++which)
		{
			std::vector<std::string> prefix;
			for (int i = 0; i < M; ++i)
			{
				if (where[i] != which) continue;
				for (int j = 0; strs[i][j]; ++j)
				{
					int ch = strs[i][j + 1];
					strs[i][j + 1] = 0;
					prefix.push_back(std::string(strs[i]));
					strs[i][j + 1] = ch;
				}
			}
			std::sort(prefix.begin(), prefix.end());
			int num = (int)(std::unique(prefix.begin(), prefix.end()) - prefix.begin());
			if (num > 0) ++num;
			sum += num;

//			printf("which=%d\n", which);
//			for (int j = 0; j < num; ++j) puts(prefix[j].c_str());
		}
		if (ans_max < sum)
		{
			ans_max = sum;
			ans_cnt = 1;
		}
		else if (ans_max == sum)
		{
			ans_cnt = (ans_cnt + 1) % MOD;
		}
	}
	printf("%d %d\n", ans_max, ans_cnt);
}

int main()
{
	int T;
	scanf("%d", &T);
	for (int cs = 1; cs <= T; ++cs)
	{
		scanf("%d%d", &M, &N);
		for (int i = 0; i < M; ++i) scanf("%s", strs[i]);
		printf("Case #%d: ", cs);
		solve();
	}
	return 0;
}
