#define _USE_MATH_DEFINES
#include <bits/stdc++.h>
using namespace std;

#define int long long

int T;

bool IsFinished(bool flg[10])
{
	for (int i = 0; i < 10; i++)
	{
		if (!flg[i]) return false;
	}
	return true;
}

int Solve(int N)
{
	if (N == 0) return 0;
	bool flg[10] = {};
	int w = 1;
	while (N % 10 == 0) N /= 10, w *= 10, flg[0] = true;
	for (int n = N;; n += N)
	{
		for (int w = 1; w <= n; w *= 10)
		{
			flg[n/w % 10] = true;
		}
		if (IsFinished(flg)) return n*w;
	}
}

void Output(int caseNum, int ans)
{
	printf("Case #%lld: ", caseNum);
	if (ans <= 0) puts("INSOMNIA");
	else printf("%lld\n", ans);
}

signed main()
{
	cin >> T;
	for (int i = 1; i <= T; i++)
	{
		int N;
		cin >> N;
		Output(i, Solve(N));
	}
	return 0;
}