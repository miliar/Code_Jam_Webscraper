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
#define MAXN 1001

int A[MAXN];
bool used[MAXN];
int S[MAXN];
int N;

int doit(int t, int res)
{
	int pre = 0;
	int pos = -1;
	for (int i = 0; i < N; ++i)
	{
		if (A[i] == t)
		{
			pos = i;
			break;
		}
		if (!used[i])
		{
			++pre;
		}
	}
	used[pos] = true;
	return min(pre, res - pre - 1);
}

void _main()
{
	scanf("%d", &N);
	for (int i = 0; i < N; ++i)
	{
		scanf("%d", &A[i]);
		used[i] = false;
	}

	memcpy(S, A, sizeof(A));
	sort(S, S + N);

	int res = 0;
	for (int i = 0; i < N; ++i)
	{
		res += doit(S[i], N - i);
	}
	printf("%d\n", res);
}

int main()
{
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);

	int T;
	scanf("%d", &T);
	for (int cases = 1; cases <= T; cases++)
	{
		printf("Case #%d: ", cases);
		_main();
	}
}