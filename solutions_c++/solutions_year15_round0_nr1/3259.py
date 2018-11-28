#include <cstdio>

using namespace std;

char sString[3000];
int maxS;

int main()
{
	int T;
	scanf("%d", &T);

	for(int ncase = 1; ncase <= T; ncase++)
	{
		scanf("%d", &maxS);
		scanf("%s", sString);

		int sum = 0;
		int ans = 0;
		for (int i = 0; i <= maxS; i++)
		{
			if (sum < i && ((int)(sString[i] - '0')) != 0)
			{
				ans += i - sum;
				sum = i;
			}
			sum += (int)(sString[i] - '0');
		}

		if (ncase != T)
			printf("Case #%d: %d\n", ncase, ans);
		else
			printf("Case #%d: %d", ncase, ans);
	}
}