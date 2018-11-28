#include <stdio.h>
#include <stdbool.h>

int main()
{
	int T;
	scanf("%d", &T);

	for (int test = 1; test <= T; test++)
	{
		int X, R, C;
		scanf("%d%d%d", &X, &R, &C);

		bool gabwin = false;

		switch (X)
		{
			case 1:
				gabwin = true;
				break;
			case 2:
				gabwin = (R * C) % 2 == 0;
				break;
			case 3:
				gabwin = (R >= 2 && C >= 2);
				break;
			case 4:
				gabwin = (R > 2 && C > 3) || (R > 3 && C > 2);
				break;
			default:
				break;
		}

		if ((R * C) % X != 0)
			gabwin = false;

		printf("Case #%d: %s\n", test, gabwin ? "GABRIEL" : "RICHARD");
	}

	return 0;
}
