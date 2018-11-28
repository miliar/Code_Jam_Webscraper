#include <stdio.h>
#include <stdarg.h>
#include <cstring>
#include <algorithm>
#include <set>
#include <vector>
#define clr(a) memset(a, 0, sizeof(a))

typedef long long ll;
typedef std::pair<int, int> pii;
#define DEBUG 1

void dbg(const char * fmt, ...)
{
#if DEBUG
	va_list args;
	va_start(args, fmt);
	vfprintf(stdout, fmt, args);
	va_end(args);
#endif
}

std::vector<std::string> sets[4];
std::string strings[8];
int n, m;

int calc_ans(int idx)
{
	auto temp = sets[idx];
	if (temp.size() == 0)
		return 0;
	std::sort(temp.begin(), temp.end());
	int ans = (int) temp[0].length() + 1;
	for(int i = 1; i < (int) temp.size(); i++)
	{
		ans += (int) temp[i].length();
		for(int j = 0; temp[i-1][j] != 0 && temp[i][j] != 0 && temp[i-1][j] == temp[i][j]; j++)
			ans--;
	}
	return ans;
}

int calc_ans()
{
	int ans = 0;
	for(int i = 0; i < n; i++)
		ans += calc_ans(i);
	//printf("%d\n", ans);
	//for(int i = 0; i < n; i++)
	//{
	//for(int j = 0; j < (int) sets[i].size(); j++)
	//printf("%s ", sets[i][j].c_str());
	//printf("\n");
	//}
	return ans;
}

pii rec(int cur)
{
	if (cur == m)
	{
		return pii(calc_ans(), 1);
	}
	pii ans(-1, 0);
	for(int i = 0; i < n; i++)
	{
		sets[i].push_back(strings[cur]);
		pii temp = rec(cur+1);
		if (sets[i].back() != strings[cur])
			throw 42;
		sets[i].pop_back();
		if (temp.first > ans.first)
			ans = temp;
		else if (temp.first == ans.first)
			ans.second += temp.second;
	}
	return ans;
}

void solve(int test_case)
{
	printf("Case #%d: ", test_case);
	scanf("%d%d", &m, &n);
	for(int i = 0; i < m; i++)
	{
		char temp[100];
		scanf("%s", temp);
		strings[i] = temp;
	}
	auto ans = rec(0);
	printf("%d %d\n", ans.first, ans.second);
}

int main()
{
	int n;
	scanf("%d", &n);
	for(int i = 1; i <= n; i++)
		solve(i);

	return 0;
}
