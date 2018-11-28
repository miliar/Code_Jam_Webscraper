#include <cstdio>
#include <iostream>

int main(void)
{
	int T;
	std::cin >> T;
	for(int t=1; t <=T; t++)
	{
		char pancake[101];
		scanf("%s",pancake);
		int idx = 0; char last = pancake[0];
		int count = 0;
		while(pancake[idx] != '\0')
		{
			if(last != pancake[idx] )
			{
				last = pancake[idx];
				count++;
			}
			idx++;
		}
		if(pancake[idx-1] == '-')
			count++;
		printf("Case #%d: %d\n",t,count);

	}
}
