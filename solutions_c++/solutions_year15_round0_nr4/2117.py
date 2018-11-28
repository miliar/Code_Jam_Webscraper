#include <cstdio>

using namespace std;

int main()
{
	int nbTests;
	scanf("%d", &nbTests);
	for(int iTest = 1; iTest <= nbTests; ++iTest)
	{
		int x, r, c;
		scanf("%d%d%d", &x, &r, &c);
		if(x > 6)
			printf("Case #%d: RICHARD\n", iTest);
		else if(x == 1)
			printf("Case #%d: GABRIEL\n", iTest);
		else if(x > r && x > c)
			printf("Case #%d: RICHARD\n", iTest);
		else if(x == 2)
		{
			if(r % 2 && c % 2)
				printf("Case #%d: RICHARD\n", iTest);
			else
				printf("Case #%d: GABRIEL\n", iTest);
		}
		else if(x == 3)
		{
			if((r*c) % 3 || r < 2 || c < 2)
				printf("Case #%d: RICHARD\n", iTest);
			else
				printf("Case #%d: GABRIEL\n", iTest);
		}
		else if(x == 4)
		{
			if(r + c < 7)
				printf("Case #%d: RICHARD\n", iTest);
			else
				printf("Case #%d: GABRIEL\n", iTest);
		}
	}
	return 0;
}
