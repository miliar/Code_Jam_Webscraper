#include <iostream>
#include <cstdio>
using namespace std;
typedef long long lint;
bool f[10];
void solve(int test)
{
	int N;
	scanf("%d", &N);
	//N++;
	if (N == 0)
	{
		printf("Case #%d: INSOMNIA\n", test);
		return;
	}
	lint answer = N;
	for (int i = 0; i < 10; i++) f[i] = false;
	int cnt = 0;
	for (lint i = 1; ; i++)
	{
		lint n = i*N;
		for (; n; n /= 10)
		{
			if (!f[n % 10]) cnt++;
			f[n % 10] = true;
		}
		if (cnt == 10)
		{
			answer = i*N;
			break;
		}
	}
	printf("Case #%d: %I64d\n", test, answer);
}
int main()
{
	int T;
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	scanf("%d", &T);
	//T = 1000*1000;
	for (int i = 1; i <= T; i++)
	{
		solve(i);
	}
	return 0;
}