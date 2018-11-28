#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <math.h>
#include <limits.h>

using namespace std;

int64_t t,n;

int64_t compute(int64_t n)
{
	int seen[] = {0, 0, 0, 0, 0, 0, 0, 0, 0, 0};

	if(n==0)
	{
		return -1;
	}

	for(int64_t m=1; m < 10000000; m++)
	{
		int64_t check = n*m;
		
		while(check > 0)
		{
			int64_t value = check % 10;
			check = check / 10;
			seen[value] = 1;
		}
		
		int filled = 0;
		for(int j=0; j < 10; j++)
		{
			if(seen[j]==1)
			{
				filled += 1;
			}
		}
		if(filled>=10)
		{
			return n*m;
		}
	}
	
}

int main()
{
	cin >> t;
	for(int tt=0; tt < t; tt++)
	{
		cin >> n;
		int64_t r = compute(n);
		if(r < 0)
		{
			cout << "Case #" << tt+1 << ": INSOMNIA" << endl;
		}
		else
		{
			cout << "Case #" << tt+1 << ": " << r << endl;			
		}

	}
	
	
	return 0;
}
