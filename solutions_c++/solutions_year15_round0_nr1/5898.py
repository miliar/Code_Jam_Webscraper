#include<bits/stdc++.h>
using namespace std;
int main()
{
	int t;
	scanf("%d", &t);
	for (int i = 1; i <= t; i++)
	{
		int smax,invite = 0,total = 0;
		scanf("%d", &smax);
		getchar_unlocked();
		for (int j = 0; j <= smax; j++)
		{
			char n = getchar_unlocked()-'0';
			if (total < j && n)
			{
				invite += j - total;
				total = j;
			}
			total += n;
		}
		printf("Case #%d: %d\n", i,invite);
	}
	return 0;
}