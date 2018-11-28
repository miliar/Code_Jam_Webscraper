#include <iostream>
#include <stdio.h>

int main(int argc, char *argv[])
{
	int t, i, j, d, p, n, c;

	scanf("%d", &t);
	for(i = 1; i <= t; ++i)
	{
		scanf("%d", &n);
		if(n == 0)
		{
			printf("Case #%d: INSOMNIA\n", i);
			continue;
		}
		
		char seen[16] = {0};
		c = 1;
		while(1)
		{
			p = n*c;
			while(p)
			{	
				d = p % 10;
				seen[d] = 1;
				p = p / 10;			
			}
			for(j = 0; j < 10; ++j)	
			{
				if(seen[j] == 0)
				{
					break;
				}
			}
			if(j == 10)
			{
				printf("Case #%d: %d\n", i, n*c);
				break;
			}
			++c;
		}
	}
	return 0;
}
