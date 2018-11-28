#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;
int T, N,temp,len;
int dp[110][2];
char pm[110];

int solution(int pos, int PM)
{
	if (pos == len) return PM;
	int &ret = dp[pos][PM];
	if (ret != -1) return ret;
	ret = 0;
	if (PM==0)
	{
		if (pm[pos] == '+')
			ret = min(solution(pos + 1, 0), solution(pos + 1, 1) + 1);
		else
			ret = min(solution(pos + 1, 0) + 2, solution(pos + 1, 1) + 1);
	}
	else
	{
		if (pm[pos] == '-')
			ret = min(solution(pos + 1, 1), solution(pos + 1, 0) + 1);
		else
			ret = min(solution(pos + 1, 1) + 2, solution(pos + 1, 0) + 1);
	}
	return ret;
}



int main()
{
	//freopen("input.txt", "r", stdin);
	//freopen("output.txt", "w", stdout);
	scanf("%d", &T);
	for (int testcase = 1; testcase <= T; testcase++)
	{
		memset(dp, -1, sizeof(dp));
		scanf("%s", pm);
		len = strlen(pm);
		printf("Case #%d: ", testcase);
		int sol = min(solution(0, 0),solution(0,1));
		printf("%d\n", sol);
	}
}