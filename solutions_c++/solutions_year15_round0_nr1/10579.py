#include <cstdio>

int main(int argc, char const *argv[])
{
	int t;

	scanf("%d", &t);

	for (int kse = 1; kse <= t; ++kse)
	{
		int s, count = 0, friends = 0;
		char si;

		scanf("%d", &s);

		for (int i = 0; i <= s; ++i)
		{
			scanf(" %c", &si);
			
			if (count < i)
			{
				friends += i - count;
				count = i;
			}
			
			
			count += si - '0';
		}

		printf("Case #%d: %d\n", kse, friends);
	}

	return 0;
}