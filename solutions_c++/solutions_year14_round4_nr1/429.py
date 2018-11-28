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


int N, X, files[10001];
bool used[10001];

void _main()
{
	scanf("%d%d", &N, &X);
	for (int i = 0; i < N; i++)
		scanf("%d", &files[i]);

	sort(files, files + N);

	memset(used, 0, sizeof(used));
	int res = 0;
	for (int i = N - 1; i >= 0; --i) 
	{
		if (used[i])
		{
			continue;
		}
		for (int j = i - 1; j >= 0; --j)
		{
			if (!used[j] && files[i] + files[j] <= X)
			{
				used[j] = true;
				break;
			}
		}
		res++;
	}

	printf("%d\n", res);
}

int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);

	int T;
	scanf("%d", &T);
	for (int cases = 1; cases <= T; cases++)
	{
		printf("Case #%d: ", cases);
		_main();
	}
}