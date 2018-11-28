#include <cstdio>

int main(void)
{
	int cases;
	scanf("%i", &cases);
	for (int t = 0; t < cases; ++t)
	{
		bool possible[16];
		for (int i = 0; i < 16; ++i)
			possible[i] = true;
		for (int a = 0; a < 2; ++a)
		{
			int row;
			scanf("%i", &row);
			--row;
			for (int i = 0; i < 16; ++i)
			{
				int idx;
				scanf("%i", &idx);
				--idx;
				if (i / 4 != row)
					possible[idx] = false;
			}
		}
		int foundIdx = -1;
		for (int i = 0; i < 16; ++i)
		{
			if (possible[i])
			{
				if (foundIdx == -1)
					foundIdx = i;
				else
					foundIdx = -2;
			}
		}
		printf("Case #%i: ", t+1);
		if (foundIdx == -1)
			printf("Volunteer cheated!\n");
		else if (foundIdx == -2)
			printf("Bad magician!\n");
		else
			printf("%i\n", foundIdx+1);
	}
	return 0;
}