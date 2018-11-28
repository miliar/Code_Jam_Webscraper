#include <string>
#include <algorithm>
#include <vector>
#include <sstream>
#include <map>
#include <cctype>
#include <math.h>
#include <numeric>
#include <set>
#include <stack>
#include <fstream>
#include <bitset>
#include <iostream>

using namespace std;

bool IsPrimeNum(unsigned long long anum)
{
	bool isprime = true;
	long double numrt = sqrt(anum);

	for (unsigned long long t = 2; t <= numrt+1; ++t)
	{
		if ((anum%t) == 0)
		{
			isprime = false;
			break;
		}
	}
	return isprime;
}

unsigned long long GetValueInBase(string bitnum, unsigned long long base)
{
	size_t len = bitnum.length();
	unsigned long long val = 0;

	for (size_t k = 0; k < bitnum.length(); ++k)
	{
		if (bitnum[k] == '1')
			val += pow(base, len-k-1);
	}

	return val;
}

unsigned long long GetDivisor(unsigned long long aval)
{
	for (unsigned long long div = 2; div < aval; ++div)
	{
		if ((aval%div) == 0)
			return div;
	}
	return 1;
}

int main()
{
	int nooftests;
	int n;
	int j;
	vector<string> jamcoins;

	cin >> nooftests;
	
	for (int testnum = 0; testnum < nooftests; ++testnum)
	{
		cin >> n >> j;
		unsigned long long runningdigitcnt = n - 2;
		unsigned long long maxno = pow(2, runningdigitcnt);

		for (unsigned long long seq = 0; seq < maxno; ++seq)
		{
			bitset<32> bitnum(seq);
			string strbitnum = bitnum.to_string<char, std::string::traits_type, std::string::allocator_type>();
			strbitnum = strbitnum.substr(strbitnum.length() - runningdigitcnt);			
			strbitnum = "1" + strbitnum + "1"; //its of length 'n'
			
			int notprimecnt = 0;
			for (int numbase = 2; numbase <= 10; ++numbase)
			{
				unsigned long long actualval = GetValueInBase(strbitnum, numbase);
				bool isprime = IsPrimeNum(actualval);
				if (!isprime)
					notprimecnt++;
				else
					break;
			}

			if (notprimecnt == 9)
				jamcoins.push_back(strbitnum);
			
			if (jamcoins.size() == j)
				break;
		}

		cout << "Case #" << (testnum+1) << ":" << "\n";
		//get the divisors
		for (size_t coinno = 0; coinno < jamcoins.size(); ++coinno)
		{
			string strthecoin = jamcoins[coinno];			
			cout << strthecoin<<" ";

			for (int nbase = 2; nbase <= 10; ++nbase)
			{
				unsigned long long actval = GetValueInBase(strthecoin, nbase);
				unsigned long long adiv = GetDivisor(actval);
				
				if ((adiv != 1) && (adiv!=actval))
					cout << adiv << " ";
			}

			cout << "\n";
		}
	}
	
	return 0;
}