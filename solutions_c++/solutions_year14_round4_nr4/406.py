#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <string>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <ctime>

using namespace std;
#define INF 1000000000
#define EPS 1e-9


int M, N;
string S[1001];
int divide[1001];
bool used[101];
int res, ways;

int cal(int cur)
{
	set<string> ss;
	for (int i = 0; i < M; i++)
	{
		if (divide[i] == cur)
		{
			for (int j = 0; j < S[i].length(); j++)
			{
				ss.insert(S[i].substr(0, j + 1));
			}
		}
	}
	return ss.size() + 1;
}

void go(int cur, int cnt)
{
	if (cur == M)
	{
		if (cnt != N) return;

		int curRes = 0;
		for (int i = 0; i < N; i++)
			curRes += cal(i);

		if (curRes == res)
		{
			ways++;
		}
		else if (curRes > res)
		{
			ways = 1;
			res = curRes;
		}
		return;
	}
	for (int i = 0; i < N; i++)
	{
		divide[cur] = i;
		if (!used[divide[cur]])
		{
			used[divide[cur]] = true;
			go(cur + 1, cnt + 1);
			used[divide[cur]] = false;
		}
		else
		{
			go(cur + 1, cnt);
		}
	}
}
void _main()
{
	cin >> M;
	cin >> N;
	for (int i = 0; i < M; i++)
		cin >> S[i];

	res = 0;
	ways = 0;
	memset(used, 0, sizeof(used));
	go(0, 0);

	printf("%d %d\n", res, ways);
}

int main()
{
	freopen("D-small-attempt1.in", "r", stdin);
	freopen("D-small-attempt1.out", "w", stdout);

	int T;
	scanf("%d", &T);
	for (int cases = 1; cases <= T; cases++)
	{
		printf("Case #%d: ", cases);
		_main();
	}
}