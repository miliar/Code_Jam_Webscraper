#include <cstdio>
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <cstdlib>
#include <cmath>
#include <cassert>

#define LL long long

using namespace std;

const int max_pr = (1 << 21);
const int maxn = 43;

//vector <int> answer;
int cnt[maxn];
bool dp[max_pr];
int n, k;
vector <int> list[maxn];
//int fr[max_pr];
int need[maxn];
int start_keys[maxn];
int mark[maxn];
short int best_seq[max_pr][22];

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int tests, q;
	scanf("%d", &tests);
	for (int test = 1; test <= tests; test++)
	{
		printf("Case #%d: ", test);
		scanf("%d%d", &k, &n);
		for (q = 0; q < k; q++)
			scanf("%d", &start_keys[q]);
		for (q = 0; q < n; q++)
		{
			int tmp;
			scanf("%d%d", &need[q], &tmp);
			list[q].clear();
			for (int j = 0; j < tmp; j++)
			{
				int x;
				scanf("%d", &x);
				list[q].push_back(x);
			}
		}
		memset(dp, false, sizeof(dp));
		int max_prof = (1 << n) - 1;
		dp[0] = true;
		for (int prof = 0; prof <= max_prof; prof++) if (dp[prof])
		{
			memset(cnt, 0, sizeof(cnt));
			for (int i = 0; i < k; i++)
				cnt[start_keys[i]]++;
			int now = prof;
			int len = 0;
			for (int j = 0; j < n; j++)
			{
				mark[j] = now % 2;
				if (now % 2 == 1)
				{
					for (int h = 0; h < list[j].size(); h++)
						cnt[list[j][h]]++;
					cnt[need[j]]--;
					len++;
				}
				now /= 2;
			}
			for (int choice = 0; choice < n; choice++)
				if (cnt[need[choice]] > 0 && mark[choice] == 0)
				{
					int new_prof = prof + (1 << choice);
					if (!dp[new_prof])
					{
						//fr[new_prof] = choice;
						for (int pos = 0; pos < len; pos++)
							best_seq[new_prof][pos] = best_seq[prof][pos];
						best_seq[new_prof][len] = choice;
					}
					else
					{
						bool f = true;
						for (int pos = 0; pos < len; pos++)
							if (best_seq[new_prof][pos] < best_seq[prof][pos])
							{
								f = false;
								break;
							}
							else if  (best_seq[new_prof][pos] > best_seq[prof][pos])
								break;
						if (f)
						{
							//fr[new_prof] = choice;
							for (int pos = 0; pos < len; pos++)
								best_seq[new_prof][pos] = best_seq[prof][pos];
							best_seq[new_prof][len] = choice;
						}
					}
					dp[new_prof] = true;
				}
		}
		if (!dp[max_prof])
		{
			printf("IMPOSSIBLE\n");
			continue;
		}
		for (int j = 0; j < n; j++)
			printf("%d ", best_seq[max_prof][j] + 1);
		printf("\n");
		/*int cur_prof = max_prof;
		answer.clear();
		for (int j = 1; j <= n; j++)
		{
			answer.push_back(fr[cur_prof].second);
			cur_prof = fr[cur_prof].first;
		}
		for (int j = answer.size() - 1; j >= 0; j--)
			printf("%d ", answer[j] + 1);
		printf("\n");*/
	}
}