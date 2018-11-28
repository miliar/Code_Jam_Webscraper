#include <stdio.h>

// constexpr int N=16;
// constexpr int J=50;

constexpr int N=32;
constexpr int J=500;

int main()
{
	int d[N]= {0};
	d[0]=1;
	d[N-1]=1;

	char coin[N+1]= { 0 };

	int number_of_coins_found=0;
	printf("Case #1:\n");
	for(;;)
	{

		for(int i=N-2; i>1; --i)
		{
			if(d[i]==0)
			{
				d[i]=1;
				break;
			}
			d[i]=0;
		}

		int b2_helper=0;
		int b6_helper=0;
		int ones=0;
		for(int i=0; i<N; i+=2)
		{
			b2_helper+=d[i]*2+d[i+1];
			b6_helper+=d[i]*6+d[i];
			ones+=d[i]+d[i+1];
		}
		// base 2, check mod 3:   -- 2,1   2,1   2,1
		if(b2_helper%3!=0)
			continue;
		// base 3, check mod 2:   -- 1, 1, 1, 1, 1, 1
		if(ones%2!=0)            
			continue;
		// base 4, check mod 3:
		if(ones%3!=0)
			continue;
		// base 5, check mod 2:    -- already checked at base 3

		// base 6, check mod 7:
		if(b6_helper%7!=0)
			continue;
		// base 7, check mod 2:   -- already checked at base 3

		// base 8, check mod 3:   -- already checked at base 2

		// base 9, check mod 2:   -- already checked at base 3

		// base 10, check mod 3:  -- already checked at base 4

		for(int i=0; i<N; ++i)
		{
			coin[i]='0'+d[i];
		}
		printf("%s 3 2 3 2 7 2 3 2 3\n",coin);
		if(++number_of_coins_found==J)
			break;
	}
	return 0;
}