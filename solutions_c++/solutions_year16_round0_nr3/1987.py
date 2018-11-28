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
#include <bitset>

#include "bigint-2010.04.30/BigInteger.hh"

using namespace std;

#define all(a) (a).begin(), (a).end()
#define FOR(i, a, b) for (long i(a), _b(b); i < _b; ++i)
const double pi = 2 * acos(0.0);
// greatest common divisor
template<class T> T gcd(T a, T b) { return b == 0 ? a : gcd(b, a % b); }
// square
template<class T> T sqr(T a) { return (a)* (a); }


/*struct cmp
{
bool operator()(const T& a, const T &b)
{
return a < b;
}
};
*/


class TestCaseSolver
{
public:
	TestCaseSolver() {}

	~TestCaseSolver() {
	}

	// to read/init the test case
	void readTestCase(std::istream &istr)
	{
		 istr >> N >> J;
	}

	BigInteger parserVal(const string &vs, int base)
	{
		BigInteger v = 0;
		for (char c : vs)
		{
			v *= base;
			if (c == '1')
			{
				v += 1;
			}
		}

		return v;
	}

/*	bool isValidJamCoin(unsigned long v)
	{
		// quick check, even when failing v could be a non-prime, but who cares... 
		if ((v - 1) % 6 == 0)
		{
			return false;
		}
		if ((v + 1) % 6 == 0)
		{
			return false;
		}
		return true; // v cannot be a prime number
	}
	*/
	bool checkValidAllBases(const string &val, list<unsigned long> &divisors)
	{
		// TODO : convert myself using a modulo 1000000007 (<-check number of zeros)
		for (int b = 2; b <= 10; ++b)
		{
			BigInteger v = parserVal(val, b);
			//unsigned long v = std::strtol(val.c_str(), nullptr, b);
			auto d = findDivisor(v);
			//cout << val << " base " << b << " =" << v << endl;
			if (d == 1) return false;
			divisors.push_back(d);
		}
		return true;
	}
	
	unsigned long findDivisor(BigInteger v)
	{
		if (v % 2 == 0) return 2;
		if (v % 3 == 0) return 3;
		BigInteger k = 1;
		BigInteger d = 1;
		auto r = v / 7;
		if (r > 1000000) r = 1000000;
		while (k <= r)
		{
			d = k * 6 - 1;
			if (v%d == 0)
				return d.toUnsignedLong();
			d += 2;
			if (v % d == 0)
				return d.toUnsignedLong();
			++k;
		}

		return 1;
	}
	/*unsigned long findDivisor(unsigned long v)
	{
		if (v % 2 == 0) return 2;
		if (v % 3 == 0) return 3;
		unsigned long k = 1;
		unsigned long d = 1;
		const auto r = (unsigned long(sqrt(v)));
		while (k<=r)
		{ 
			d = k * 6 - 1;
			if (v%d == 0)
				return d;
			d += 2;
			if (v % d == 0)
				return d;
			++k;
		}

		return 1;
	}*/
	// to solve the test case and output the value to ostr
	std::string solveTestCase()
	{
		stringstream ss;
		//ss << "\n";
		int count = 0;

		// try stupid method
		//string v = "1000000000000001";
		const unsigned long maxV = pow(2, N - 2);
		for (int i = 0; i < maxV && count < J; ++i)
		{
			// generate string val
			stringstream sv;
			sv << "1" << std::bitset<30>(i) << "1";
			string v = sv.str();
			list<unsigned long> divisors;
			cout << v << endl;
			if (checkValidAllBases(v, divisors))
			{
				ss << '\n';
				++count;
				ss << v;
				cout << "Found " << count << " / " << J << endl;
				for (auto d : divisors)
				{
					ss << " " << d;
				}
				
			}
		}
		
		return ss.str();
	}

	int N, J;
};



int main(int argc, char* argv[])
{
	std::ios_base::sync_with_stdio(false);

	std::string inputFile("C:\\Users\\David\\Downloads\\C-small.in");
	std::string outputFile("C:\\GoogleJam\\C.out");

	ofstream out;
	ifstream in;

	//in.open(argv[1]);
	//out.open(argv[2]);
	in.open(inputFile);
	out.open(outputFile);

	unsigned int nbTestCases;
	in >> nbTestCases;

	for (unsigned int curTest = 1; curTest <= nbTestCases; ++curTest)
	{
		TestCaseSolver testcaseSolver;

		testcaseSolver.readTestCase(in);
		std::string answer = testcaseSolver.solveTestCase();
		out << "Case #" << curTest << ": " << answer << '\n';
		cout << "Case #" << curTest << ": " << answer << endl;

	}
	out << flush;

	return 0;
}