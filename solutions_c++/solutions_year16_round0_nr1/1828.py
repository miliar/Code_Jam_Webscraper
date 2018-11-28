#include <stdio.h>

int d;

int
main(void)
{
	int T, n;
	scanf("%d", &T);
	for(int t = 1; t <= T; t++)
	{
		printf("Case #%d: ", t);
		d = 0;
		scanf("%d", &n);
		for(int i = n; i != 0 && i <= 2000000000; i += n)
		{
			int tmp = i;
			while(tmp != 0)
			{
				d |= (1 << (tmp%10));
				tmp /= 10;
			}
			if(d == 1023)
			{
				printf("%d\n", i);
				break;
			}
		}
		if(d != 1023)
			printf("INSOMNIA\n");
	}
}
