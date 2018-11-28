#include <cstdio>
#include <cinttypes>
#include <cstdint>
#define N 16
#define J 50

intmax_t coinJam;
intmax_t base[10];
intmax_t evenDivisor[10];

#define NEXT_COIN coinJam += 2;

void generateFirsCoinJamCandidate(void)
{
	coinJam = 1;
	coinJam = coinJam << N-1;
	coinJam += 1;
	
}


intmax_t convertToBase(intmax_t local, intmax_t base)
{
	intmax_t rc = 0;
	intmax_t current = 1;
	intmax_t one = 1;
	while(local)
	{
		if (local & one)
		{
		    rc += current;
		}
		local = local >> 1;
		current *= base;
	}
	return rc;	
}
intmax_t imaxSqr(intmax_t inputBase){
	intmax_t sqr = 1;
	while (sqr*sqr < inputBase)
	{
		sqr = sqr << 1;
	}
	return sqr;
}


intmax_t findDivisor(intmax_t inputBase)
{
	intmax_t input = base[inputBase];
	intmax_t limit = imaxSqr(input);
	intmax_t current = 2;
	for (current = 2; current < limit; current++)
	{
		if (input%current == 0)
		{
			evenDivisor[inputBase] = current;
			return 1;
		}
	}
	return 0;
}

void printCoinJam(void)
{
	intmax_t output = coinJam;
	char  coinJamString[N+1];
	for (int c = 1; c <= N; c++)
	{
		coinJamString[N - c] = (output & 1) + '0';
		output /= 2;
	}
	coinJamString[N] = '\0';
	//printf("%s %" PRIdMAX " %" PRIdMAX " %" PRIdMAX " %" PRIdMAX " %" PRIdMAX " %" PRIdMAX " %" PRIdMAX " %" PRIdMAX " %" PRIdMAX "\n", coinJamString,
//	                                       base[2],
//	                                       base[3],
//	                                       base[4],
//	                                       base[5],
//	                                       base[6],
//	                                       base[7],
//	                                       base[8],
//	                                       base[9],
//	                                       base[10]);
	printf("%s %" PRIdMAX " %" PRIdMAX " %" PRIdMAX " %" PRIdMAX " %" PRIdMAX " %" PRIdMAX " %" PRIdMAX " %" PRIdMAX " %" PRIdMAX "\n", coinJamString,
	                                       evenDivisor[2],
	                                       evenDivisor[3],
	                                       evenDivisor[4],
	                                       evenDivisor[5],
	                                       evenDivisor[6],
	                                       evenDivisor[7],
	                                       evenDivisor[8],
	                                       evenDivisor[9],
	                                       evenDivisor[10]);
}

long isCoinJam(void)
{
	for (int c = 2; c <= 10; c++)
	{		
		base[c] = convertToBase(coinJam,c);
		evenDivisor[c] = 0;
	}
	for (int c = 2; c <= 10; c++)
	{
		if (!findDivisor(c))
		    return 0;
	}
	return 1;
	
}


void findCoinJam(void)
{
	while(!isCoinJam())
	{
		NEXT_COIN;
	}
	printCoinJam();
	NEXT_COIN;
}

int main()
{
	generateFirsCoinJamCandidate();
	for (long c = 0; c < J; c++)
	{
		findCoinJam();
	}

}
