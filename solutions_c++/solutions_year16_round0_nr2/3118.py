#include <cstdio>
#include <cstdlib>
#include <vector>

int main()
{
	int Test;
	scanf("%d", &Test);
	long long int * flips = new long long int[Test];
	getchar();
	for(int t=0; t < Test; ++t)
	{
		char str[101];
		scanf("%s", str);
		char prev;
		long long int flip = 0;
		int n;
		for(int i=0; i<101; ++i)
		{
			if(str[i]=='\0')
			{
				n = i;
				break;
			}
		}
		prev = str[n-1];
		for(int i=n-2; i >= 0; --i)
		{
			if(str[i]==prev && prev=='+')
			{
				continue;
			}
			else if(str[i]==prev)
			{
				continue;
			}
			else if(str[i]=='+')
			{
				flip += 2;
				prev = '+';
			}
			else 
			{
				prev = '-';
			}
		}
		if(prev=='-')
		{
			flip += 1;
		}
		flips[t] = flip;
	}
	for(int t=0; t<Test; ++t)
	{
		printf("Case #%d: %lli\n", t+1, flips[t]);
	}
	delete[] flips;
	return 0;
}