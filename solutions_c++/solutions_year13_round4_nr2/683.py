#include<cstdio>

int T, N, l;
long long M, P, d, two[60];

int main()
{ 
  	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	scanf("%d", &T);
	two[0] = 1;
	for (int i = 1; i <= 51; i++)
		two[i] = two[i - 1] * 2;
	for (int g = 0; g < T; g++)
	{
		printf("Case #%d: ", g + 1);
		scanf("%d%I64d", &N, &P);
		if (P == 0)
		{
			printf("%d %d\n", 0, 0);
			continue;
		}
		M = two[N];
		if (P == M)
		{
			printf("%I64d %I64d\n", M - 1, M - 1);
			continue;
		}
		d = M - P;
		//printf("%I64d %I64d %I64d\n", d, M, P);
		for (int i = 51; i >= 0; i--)
		{
			if (d >= two[i])
			{
				l = i;
				break;
			}
		}
		printf("%I64d ", two[N - l] - 2);
		for (int i = 51; i >= 0; i--)
		{
			if (P >= two[i])
			{
				l = i;
				break;
			}
		}
		printf("%I64d\n", M - M / two[l]); 
	}
	return 0;
}
