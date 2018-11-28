#include <iostream>
#include <cstdio>
#include <cstring>

using namespace std;

int main()
{
	int T, z = 1;
	scanf("%d",&T);
	while(T--)
	{
		char str[105],c;long long int count = 0;
		scanf("%s",str + 1);
		int len = strlen(str + 1);
		c = str[1]; 
		for(int i = 2; i <= len; i++)
		{
			if(c != str[i])
			{
				count++;
				if(c == '+')
					c = '-';
				else
					c = '+';
			}
		}

		if(c == '-')
			count++;
		printf("Case #%d: %lld\n",z,count);
		z++;
	}
	return 0;
}