#include <iostream>
#include <stdio.h>
int main(int argc, char *argv[])
{
	int t, i, p, j;
	char s[1000002], prev;

	scanf("%d", &t);
	for(i = 1; i <= t; ++i)
	{
		scanf("%s", s);
		
		p = 0;
		j = 0;
		prev = 0;
		while(s[j])
		{
			if(prev != s[j])
			{
				++p;
			}
			prev = s[j];
			++j;
		}
		
		if(s[j-1] == '+')
		{
			--p;
		}

		printf("Case #%d: %d\n", i, p);		
	}
}
