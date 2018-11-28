#include <iostream>
#include <fstream>
#include <sstream>
#include <bitset>
#include <list>
#include <algorithm>
#include <math.h>
#include <stdio.h>
#include <inttypes.h>


// http://stackoverflow.com/questions/11656241/how-to-print-uint128-t-number-using-gcc

#define P10_UINT64 10000000000000000000ULL   /* 19 zeroes */
#define E10_UINT64 19

#define STRINGIZER(x)   # x
#define TO_STRING(x)    STRINGIZER(x)

static int print_u128_u(unsigned __int128 u128)
{
    int rc;
    if (u128 > UINT64_MAX)
    {
        unsigned __int128 leading  = u128 / P10_UINT64;
        uint64_t  trailing = u128 % P10_UINT64;
        rc = print_u128_u(leading);
        rc += printf("%." TO_STRING(E10_UINT64) PRIu64, trailing);
    }
    else
    {
        uint64_t u64 = u128;
        rc = printf("%" PRIu64, u64);
    }
    return rc;
}

static int snprint_u128_u(unsigned __int128 u128, char *buffer, int bufferSize)
{
    int rc;
    if (u128 > UINT64_MAX)
    {
        unsigned __int128 leading  = u128 / P10_UINT64;
        uint64_t  trailing = u128 % P10_UINT64;
        rc = snprint_u128_u(leading, buffer, bufferSize);
        rc += snprintf(buffer + rc, bufferSize - rc, "%." TO_STRING(E10_UINT64) PRIu64, trailing);
    }
    else
    {
        uint64_t u64 = u128;
        rc = snprintf(buffer, bufferSize, "%" PRIu64, u64);
    }
    return rc;
}



// Returns 0 if prime, first nontrivial divisor otherwise
unsigned __int128 findNonTrivialDivisor(unsigned __int128 x)
{
  if (x < 2) 
  	return false;
  for (unsigned __int128 i = 2; i <= sqrtl(x); i++) 
  {
    if ((x % i) == 0) {
    	return i;
    }
  }
  return 0;
}


template<int N>
unsigned __int128 bitsetToBase(const std::bitset<N> &coinJamBitset, int base)
{
	unsigned __int128 result = 0;
	for (int i = 0; i < N; i++)
		result += coinJamBitset[i] * powl(base, i);
	return result;  
}


template <int N>
void computeCoinJam(int J)
{
	std::bitset<N> coinJamBitset;
	std::list<unsigned long long> listValidCoinjam;


	int nbValidCoin = 0;


	while (nbValidCoin != J)
	{
		// Generate random coinJam
		coinJamBitset[0] = 1;
		for (int i = 1; i < N - 1; i++)
			coinJamBitset[i] = std::rand() % 2;
		coinJamBitset[N - 1] = 1;


		// Check if valid
		bool isValid = true;

		unsigned long long curCoinJamValue = coinJamBitset.to_ullong();
		auto alreadyFound = std::find(listValidCoinjam.begin(), listValidCoinjam.end(), curCoinJamValue);

		if (alreadyFound != listValidCoinjam.end()) {
			continue;
		}

		std::stringstream listNonTrivialDivisor;
		listNonTrivialDivisor.flush();

		for (int base = 2; base <= 10; base++)
		{
			unsigned __int128 currentBaseValue = bitsetToBase<N>(coinJamBitset, base);
			unsigned  long long nonTrivialDivisor = findNonTrivialDivisor(currentBaseValue); 

			if (nonTrivialDivisor == 0)
			{
				isValid = false;
				break;
			}
			else
			{
				listNonTrivialDivisor << nonTrivialDivisor << " ";
			}
		}

		if (isValid)
		{
			nbValidCoin++;
			std::cout << coinJamBitset.to_string() << " " << listNonTrivialDivisor.str() << std::endl;
			listValidCoinjam.push_back(coinJamBitset.to_ullong());

		}
	}

}

void debug()
{
	std::bitset<32> coin("11001101111001111001011000001111");


	for (int base = 2; base <= 10; base++)
	{
		unsigned __int128 currentBaseValue = bitsetToBase<32>(coin, base);
		std::cout << coin.to_string() << " => ";
		print_u128_u(currentBaseValue);
		 std::cout << std::endl;		
	}
	exit (1);
}

int main(int argc, char *args[])
{
//	debug();
	std::ifstream input(args[1]);

	int nbCase;
	input >> nbCase;

	for (int curCase = 1; curCase <= nbCase; curCase++)
	{
		int N, J;
		input >> N >> J;

		std::cout << "Case #" << curCase << ":" << std::endl;
		switch (N) 
		{
			case 4: computeCoinJam<4>(J); break;
			case 6: computeCoinJam<6>(J); 	break;
			case 16: computeCoinJam<16>(J); break;
			case 32: computeCoinJam<32>(J); break;
		}
		std::cout << std::endl;
	}
	return 0;
}
