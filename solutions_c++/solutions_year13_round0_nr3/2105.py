#include <iostream>
#include <string>
#include <sstream>


// Precalculated palindromes 1..10^14
unsigned long long kPalindrome[] = 
{
	1,
	2,
	3,
	11,
	22,
	101,
	111,
	121,
	202,
	212,
	1001,
	1111,
	2002,
	10001,
	10101,
	10201,
	11011,
	11111,
	11211,
	20002,
	20102,
	100001,
	101101,
	110011,
	111111,
	200002,
	1000001,
	1001001,
	1002001,
	1010101,
	1011101,
	1012101,
	1100011,
	1101011,
	1102011,
	1110111,
	1111111,
	2000002,
	2001002
};

unsigned long long nrPalindromes = sizeof(kPalindrome) / sizeof(unsigned long long);

// Finds the integer square root of a positive number of any type  
template <typename type>  
type intSqrt (type remainder)  
{  
  if (remainder < 0) // if type is unsigned this will be ignored = no runtime  
    return 0; // negative number ERROR  
  
  type place = (type)1 << (sizeof (type) * 8 - 2); // calculated by precompiler = same runtime as: place = 0x40000000  
  while (place > remainder)  
    place /= 4; // optimized by complier as place >>= 2  
  
  type root = 0;  
  while (place)  
  {  
    if (remainder >= root+place)  
    {  
      remainder -= root+place;  
      root += place * 2;  
    }  
    root /= 2;  
    place /= 4;  
  }  
  return root;  
}  

template <typename T>
std::string NumberToString ( T Number )
{
	std::stringstream ss;
	ss << Number;
	return ss.str();
}

bool isPalindrome(unsigned long long number)
{
	std::string s = NumberToString(number);

	return s == std::string(s.rbegin(), s.rend());
}

unsigned long calculatePalindromesInside(unsigned long long start, unsigned long long end)
{
	// Find the starting point
	unsigned long nr = 0;
	for(unsigned long long i = 0; i < nrPalindromes; i++)
	{
		if (kPalindrome[i] >= start && kPalindrome[i] <= end)
		{
			nr++;
		}
	}

	return nr;
}


int main(int argc, char *argv[])
{
	int nrTestCases;

	std::cin >> nrTestCases;

	for(int tc = 0; tc < nrTestCases; tc++)
	{
		unsigned long long alku, loppu;
		unsigned long long result = 0;

		std::cin >> alku >> loppu;

		unsigned long long sqalku = intSqrt(alku);
		if (alku != (sqalku*sqalku))
		{
			sqalku++;
		}
		unsigned long long sqloppu = intSqrt(loppu);


		result = calculatePalindromesInside(sqalku, sqloppu);

/*
		for(unsigned long long i = sqalku; i <= sqloppu; i++)
		{
			if (isPalindrome(i)
				&& isPalindrome(i*i))
			{
				std::cout << i << "\n";
				// result++;
			}
		}
		*/

		std::cout << "Case #" << (tc+1) << ": " << result << "\n";
	}

	return 0;
}