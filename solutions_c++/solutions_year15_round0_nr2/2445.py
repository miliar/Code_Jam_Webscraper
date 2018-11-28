#include <cstdio>
#include <iostream>
#include <algorithm>
#include <set>
#include <map>
#include <vector>
#include <cstdlib>
#include <ctime>
#include <stack>
#include <cmath>
#include <queue>
using namespace std;

int N, a[1010];

int evaluate(int max_size)
{
	int ret = 0;
	for (int i = 0; i < N; ++i)
	{
		if (a[i] > max_size)
		{
			ret += (a[i] / max_size) - 1;
			if (a[i] % max_size != 0) ret++;
		}
	}
	return ret;
}

void input()
{
	cin >> N;
	int out = -1u/2;
	for (int i = 0; i < N; ++i)
	{
		cin >> a[i];
	}
	for (int i = 1; i <= 1000; ++i)
	{
		out = min(out, evaluate(i) + i);
	}
	cout << out << endl;
}

int main()
{
	freopen("input.in", "r", stdin);
	freopen("output.out", "w", stdout);
	
	int T;
	scanf("%d", &T);

	for (int test = 1; test <= T; ++test)
	{
		printf("Case #%d: ", test);
		input();
	}

	return 0;
}