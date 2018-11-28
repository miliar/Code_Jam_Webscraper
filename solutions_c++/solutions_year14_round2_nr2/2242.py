#include <memory>
#include <string>
#include <list>
#include <vector>
#include <set>
#include <map>
#include <fstream>
#include <sstream>
#include <iostream>
#include <algorithm>
#include <math.h>  
#include <cmath>  

#include "bigint-2010.04.30\BigInteger.hh"

using namespace std;

#define FOR(i,a,b) for(long i=(a), _b=(b); i < _b;++i)
#define all(a) (a).begin(), (a).end()

const double pi = 2 * acos(0.0);
// greatest common divisor
template<class T> T gcd(T a, T b) { return b == 0 ? a : gcd(b, a % b); }
// square
template<class T> T sqr(T a) { return (a) * (a); }

typedef std::vector<int> vi;
typedef std::vector<long> vl;
typedef pair<int, int> pii;
typedef std::vector< pii > vii;
typedef std::list< std::string > lss;
typedef std::list<int> lsi;
typedef std::list<long> lsl;
//typedef vector<BigInteger> vbi;
//typedef list<BigInteger> lbi;


class TestCaseSolver 
{
public:
	TestCaseSolver() {
	}

	// to read/init the test case
	void readTestCase(std::istream &istr)
	{
		istr >> a;
		istr >> b;
		istr >> k;
		
	}

	// to check test case reading was ok
	std::string toString() const 
	{
		string str = "TODO";
		return str;
	}

	int getHighestBit(unsigned long val)
	{
		if (!val || val == 1)
    	return 0;

		int ret = 0;

		while (val >>= 1)
    		++ret;

		return ret;
	}


	// to solve the test case and output the value to ostr
	std::string solveTestCase()
	{
		//BigInteger nbWinners = 0;
		unsigned long long nbWinners = 0;


		//nb winners = nb combinaisons a&b < k

		/*int nbBitsK = getHighestBit(k);
		int nbBitsA = getHighestBit(a);
		int nbBitsB = getHighestBit(b);

		unsigned long long nbCombin = (a*b);
		unsigned long abis = (a>>(nbBitsK-1));
		if (abis == 0)
			abis = 1;
		unsigned long bbis = (b>>(nbBitsK-1));
		if (bbis == 0)
			bbis = 1;
		unsigned long long nbBad = bbis*abis;
		// now count good values if k had some 1 nbBitsK
		if (k > (1<<(nbBitsK)))
		{
			// remove some bad
		}

		unsigned long complK = ~k;
		complK &= (1<<(nbBitsK+1))-1;
		*/
		for (unsigned long i = 0 ; i < a ; ++i)
		{
			for (unsigned long j = 0 ; j < b ; ++j)
			{
				if ((i&j) < k)
				{
					++nbWinners;
				}
			}

		}

		
		stringstream out;
			out << nbWinners;
		return out.str();
	}

private:
	unsigned long a;
	unsigned long b;
	unsigned long k;
};


int main(int argc, char* argv[])
{
	std::string inputFile("C:\\Users\\David\\Downloads\\B-small-attempt0 (1).in");
	std::string outputFile("C:\\\Users\\David\\out.txt");

	ofstream out;
	ifstream in;

	in.open(inputFile);
	out.open(outputFile);

	unsigned long nbTestCases;
	in >> nbTestCases;

	char buffer[256];

	for (unsigned long curTest = 1 ; curTest <= nbTestCases ; ++curTest)
	{
		TestCaseSolver testCaseSolver;

		// 1-read test case
		testCaseSolver.readTestCase(in);

		//ostr << testCaseSolver.toString() << endl;

		// 2-process test case
		std::string answer = testCaseSolver.solveTestCase();

		// 3-output test case result		
		sprintf_s(buffer, "Case #%d: ", curTest);
		string res=buffer + answer;
		out << res << endl;
	}

	return 0;
}