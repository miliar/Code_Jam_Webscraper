#include <stdio.h>
#include <iostream>
#include <string.h>

int main()
{
	int cases;
	std::cin >> cases;
	char buf[120];
	for(int c=0; c<cases; ++c)
	{
		std::cin >> buf;
		int l=(int)strlen(buf);
		char Good='+';
		int flips_needed=0;
		for(int i=l-1; i>=0; --i)
		{
			if(buf[i]!=Good)
			{
				++flips_needed;
				Good=Good=='+'?'-':'+';
			}
		}

		printf("Case #%d: %d\n", c+1, flips_needed);
	}
	return 0;
}