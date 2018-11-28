#include <stdio.h>
#include <string.h>

int hash[18];

int
main(void)
{
	int r, a, T;
	scanf("%d", &T);
	for(int l = 0; l < T; l++)
	{
		memset(hash, 0, sizeof(hash));
		for(int k = 0; k < 2; k++)
		{
			scanf("%d", &r);
			for(int i = 0; i < 4; i++)
				if(i == r-1)
					for(int j = 0; j < 4; j++)
					{
						scanf(" %d", &a);
						hash[a]++;
					}
				else
					scanf(" %*[^\n]");
		}
		int ans = 0, x;
		for(int i = 1; i <= 16; i++)
			if(hash[i] == 2)
			{
				ans++;
				x = i;
			}
		printf("Case #%d: ", l+1);
		if(ans == 0)
			printf("Volunteer cheated!\n");
		else if(ans == 1)
			printf("%d\n", x);
		else
			printf("Bad magician!\n");
	}
	return 0;
}
