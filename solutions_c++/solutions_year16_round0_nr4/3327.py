#include <iostream>
#include <stdio.h>
unsigned long long ipower(unsigned long long base, unsigned long long exp)
{
    unsigned long long result = 1;
    while (exp)
    {
        if (exp & 1)
            result *= base;
        exp >>= 1;
        base *= base;
    }

    return result;
}

void printans(unsigned long long *a, unsigned long long s, unsigned long long i)
{
	printf("Case #%d:", i);
	for(unsigned long long j = 0; j < s; ++j)
	{
		printf(" %llu", a[j]);
	}
	printf("\n");
} 
int main(int argc, char *argv[])
{
	unsigned long long t, k, c, s, mreq, i, j, krc; 
	unsigned long long ans[102];

	scanf("%llu", &t);
	for(i = 1; i <= t; ++i)
	{
		scanf("%llu %llu %llu", &k, &c, &s);

		if(c == 1)		
		{
			if(s < k)
			{
				printf("Case #%d: IMPOSSIBLE\n", i);
			}
			else
			{
				for(j = 0; j < k; ++j)
				{
					ans[j] = j + 1;
				}
				printans(ans, k, i);
			}
			continue;
		}

		if(k & 1)
		{
			mreq = (k / 2) + 1;
		}
		else
		{
			mreq = k / 2;
		}

		if(s < mreq)
		{
			printf("Case #%d: IMPOSSIBLE\n", i);					
			continue;
		}

		c = c - 1;
		krc = ipower(k, c);
		for(j = 0; j < mreq; ++j)
		{
			ans[j] = (j * krc) + (k - (j + 1));
			ans[j] += 1;				
		}
		
		printans(ans, mreq, i);
	}
}
