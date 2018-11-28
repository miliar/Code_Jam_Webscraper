#include <fstream>
#include <string>
#include <vector>
#include <set>
#include <sstream>
#include <algorithm>
#include <math.h>
//#include <cstdint>
#include <iomanip>
#include <bitset>
typedef unsigned long long uint;
using namespace std;


uint nonTrivialFactor(uint number)
{	
	uint i;

	for (i = 2; i < number; i++)
	{
		if (number % i == 0)
		{
			return i;
		}
	}

	return 0;
}

bool isPrime(uint n)
{
	uint p, q, r;
	if (!(n & 1) || n < 2) return n == 2;

	for (p = 3, q = n / p, r = n%p; p <= q; p += 2, q = n / p, r = n%p)
	if (!r) return false;
	return true;
}

bool getCoin(string& coinString, uint nonTrivials[9])
{
	coinString[0] = '1';
	uint converted = _strtoui64(coinString.c_str(), NULL, 2);
	uint oneMore = converted + 1;
	bitset<16> oneMoreBS(oneMore);
	stringstream oneMoreSS;
	oneMoreSS << oneMoreBS;
	coinString = oneMoreSS.str();
	coinString[0] = '1';
	coinString[coinString.size() - 1] = '1';

	for (int base = 2; base <= 10; base++)
	{
		
		converted = _strtoui64(coinString.c_str(), NULL, base);
		if (isPrime(converted))
		{
			if (getCoin(coinString, nonTrivials))
				return true;
			else
				return false;
		}
		else
			nonTrivials[base - 2] = nonTrivialFactor(converted);
	}

	return true;
}

int main(int argc, char* argv[])
{
  fstream input("test.in");
  fstream out("out.txt", ios_base::out);
  int T = 0;
  input >> T ;
  string line;
  getline(input, line); //burn the empty line
  for (int i = 1; i <= T; i++)
  {
	  uint length, totalJamcoins;
	  input >> length;
	  input >> totalJamcoins;
	  getline(input, line);
	  uint jamcoin;
	  uint nonTrivials[9];

	  string coinString(length,'0');

	  out << "Case #" << i << ":" << endl;

	  for (int j = 0; j < totalJamcoins; j++)
	  {

		  getCoin(coinString, nonTrivials);
		  out << coinString << " ";
		  for (int base = 2; base <= 10; base++)
		  {
			  out << nonTrivials[base - 2];
			  if (base < 10)
				  out << " ";
			  else
				  out << endl;
		  }
	  }
  }
	return 0;
}

