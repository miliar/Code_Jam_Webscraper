#include <stdio.h>
#include <string.h>

int main()
{
	int n, counter = 0;
	char c[20];
	
	scanf("%d", &n);
	
	for(int w = 0; w < n; w++)
	{
		scanf(" %s", c);
		counter = 0;
		for(int i = 1; i < strlen(c); i++)
		{
			if(c[i] != c[i-1])
			{
				counter++;
				for(int k = i-1; k >= 0; k--)
					if(c[k] == '-')
						c[k] = '+';
					else
						c[k] = '-';
			}
		}
	
		if(c[0] == '-')
			counter++;
	
		printf("Case #%d: %d\n", w+1, counter);
	}
	return 0;

}
