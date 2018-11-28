
#include <iostream>
#include <cstdio>

int main()
{
	int t;
	scanf("%d", &t);
	int z = t;
	while (t--)
	{
		int s;
		scanf("%d", &s);
		char x[2000];
		scanf("%s", x);
		
		int sum = 0;
		int friends = 0;
		if (s == 0)
		{
			printf("Case #%d: 0\n", z - t);
			continue;
		}
		for (int i = 0; i <= s; i++)
		{
			if (i == 0)
			{
				if (x[i] == '0') friends = 1;
				sum += x[i] - '0';
				continue;
			}
			if (sum + friends < i)
			{
				friends += i - sum - friends;
			}
      sum += x[i] - '0';
		}
		printf("Case #%d: %d\n", z - t, friends);
	}
	
	
	return 0;
}
