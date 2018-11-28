#include <stdio.h>
#include <math.h>
#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cstring>
#include <string>
#include <memory>
#include <algorithm>
#include <map>
#include <vector>

using namespace std;

int main()
{
	freopen("input.in","r",stdin);
	freopen("output.out","w",stdout);
	int TestCase;
	int Smax;
	char audi[1005];
	scanf("%d",&TestCase);
	for(int i = 1;i <= TestCase;i++)
	{
		scanf("%d",&Smax);
		scanf("%s",&audi);
		int audiCount = 0;
		int guestCount = 0;
		for(int j = 0;j <= Smax;j++)
		{	
			if( audi[j] != '0' && audiCount<j)
			{
				guestCount += j - audiCount;
				audiCount += (j - audiCount);
			}

			audiCount += audi[j] - 48;	

		}

		printf("Case #%d: %d\n",i ,guestCount);
		
	}
	return 0;
}