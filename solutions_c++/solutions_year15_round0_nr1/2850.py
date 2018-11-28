#include <cstdio>

int N;
int S[10000], Total[10000];
char Tmp[10000];

int Work()
{
	scanf("%d%s", &N, Tmp);
	for (int i = 0; i <= N; i ++)
	{
		S[i] = Tmp[i] - '0';
		Total[i] = S[i];
		if (i > 0)
			Total[i] += Total[i - 1];
	}
	int Ans = 0;
	for (int i = N; i >= 1; i --)
		if (Total[i - 1] + Ans < i)
			Ans += i - Total[i - 1] - Ans;
	return Ans;
}

int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	int Cases;
	scanf("%d", &Cases);
	for (int Case = 1; Case <= Cases; Case ++)
	{
		printf("Case #%d: %d\n", Case, Work());
	}
	return 0;
}
