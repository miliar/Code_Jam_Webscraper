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
		istr >> fraction;
		unsigned long div = fraction.find('/');
		_p = atol(fraction.substr(0, div).c_str());
		_q = atol(fraction.substr(div+1).c_str());
	
	}

	// to check test case reading was ok
	std::string toString() const 
	{
		stringstream out;
		out << "fraction="<<fraction<<" p="<<_p<<" q="<<_q<<endl;
		return out.str();
	}

	long getMin1Ancestor(unsigned long long p, unsigned long long q)
	{
		// check if impossible
		//cout << "p = "<<p<<" q="<<q<<endl; 
		if (q == 0 || q%2)
			return -10000;

		if ((p<<1)>=q )
			return 1;
		else 
			return 1+getMin1Ancestor(p,q>>1);
	}


	

	// to solve the test case and output the value to ostr
	std::string solveTestCase()
	{
		unsigned long long ancestors = 1;
		ancestors = ancestors << 40;
		
		stringstream out;
		if (ancestors%_q != 0)
		{
			out << "impossible";
		}
		else {
		 long l = getMin1Ancestor(_p, _q);
		

			
			if (l > 0)
				out << l;
			else 
				out << "impossible";
		}
		return out.str();
	}

private:
	unsigned long long _p;
	unsigned long long _q;
	string fraction;
	
};


int main(int argc, char* argv[])
{
	std::string inputFile("C:\\Users\\David\\Downloads\\A-small-attempt1 (1).in");
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

		//cout << testCaseSolver.toString() << endl;

		// 2-process test case
		std::string answer = testCaseSolver.solveTestCase();

		// 3-output test case result		
		sprintf_s(buffer, "Case #%d: ", curTest);
		string res=buffer + answer;
		out << res << endl;
	}

	return 0;
}