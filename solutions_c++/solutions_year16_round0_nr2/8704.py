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

int Solve(string S)
{
	int ans = 0;
	for (int i = 0; i < S.size() - 1; i++)
	{
		if (S[i] != S[i + 1]) ans++;
	}
	return ans;
}

void Output(int caseNum, int ans)
{
	printf("Case #%lld: ", caseNum);
	printf("%lld\n", ans);
}

signed main()
{
	cin >> T;
	for (int i = 1; i <= T; i++)
	{
		string S;
		cin >> S;
		S.push_back('+');
		Output(i, Solve(S));
	}
	return 0;
}