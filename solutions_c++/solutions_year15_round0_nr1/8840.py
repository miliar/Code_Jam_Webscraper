#pragma warning(disable:4996)

#include <cstdio>
#include <cstdlib>
#include <cstring>

int Shyness[1005];

int main()
{
	std::freopen(".\\Output.txt", "w", stdout);
	std::freopen(".\\Input.txt", "r", stdin);
	int T;
	std::scanf("%d", &T);
	int S;
	int res = 0;
	int total = 0;
	for (int i = 0; i < T; ++i)
	{
		std::scanf("%d", &S);
		getchar();
		for (int j = 0; j <= S; ++j)
		{
			Shyness[j] = getchar()-'0';
		}
		for (int j = 0; j <= S; ++j)
		{
			if (Shyness[j] && total < j)
			{
				res += (j - total);
				total += (j - total);
			}
			total += Shyness[j];
		}
		std::printf("Case #%d: %d\n", i+1, res);
		total = res = 0;
	}
	return 0;
}