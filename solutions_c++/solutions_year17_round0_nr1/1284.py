#include <stdio.h>

int main()
{
	int loops;
	scanf("%i", &loops);
	
	for (int i=0;i<loops;i++)
	{
		char buf[2000];
		int flipsize;
		scanf("%s %i", buf, &flipsize);
		
		int flips=0;
		for (int j=0;buf[j];j++)
		{
			if (buf[j]=='-')
			{
				flips++;
				for (int k=0;k<flipsize;k++)
				{
					if (buf[j+k]=='\0') goto fail;
					else buf[j+k] ^= ('-' ^ '+');
				}
			}
		}
		if (false)
		{
		fail:
			printf("Case #%i: IMPOSSIBLE\n", i+1);
		}
		else
		{
			printf("Case #%i: %i\n", i+1, flips);
		}
	}
}
