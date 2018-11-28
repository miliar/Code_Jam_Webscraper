#include <stdio.h>
#include <string.h>
using namespace std;

int main()
{
	long long int T, len, i, count = 0, steps = 0;
	char str[105], temp;

	scanf("%lld", &T);

	while(T--)
	{
		steps = 0;
		count++;
		scanf("%s", str);
		len = strlen(str);
		while(len > 0 && str[len - 1] == '+')
		{
			len--;
		}
		str[len] = 0;
		while(len > 0)
		{
			if(str[0] == '+')
			{
				steps++;
				i = 0;
				while(str[i] == '+')
				{
					str[i] = '-';
					i++;
				}
			}
			for(i = 0; i < len / 2; i++)
			{
				temp = str[i];
				str[i] = str[len - 1 - i];
				str[len - 1 - i] = temp;
			}
			for(i = 0; i < len; i++)
			{
				str[i] = '+' + '-' - str[i];
			}
			steps++;
			while(str[len - 1] == '+')
			{
				len--;
			}
			str[len] = 0;
		}
		printf("Case #%lld: %lld\n", count, steps);
	}
	return 0;
}