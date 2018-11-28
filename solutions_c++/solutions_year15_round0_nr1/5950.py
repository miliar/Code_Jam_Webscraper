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

//#include "bigint-2010.04.30\BigInteger.hh"

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

		istr >> maxVal;
		istr >> spect;	
	}

	// to check test case reading was ok
	std::string toString() const 
	{
		stringstream out;
		out << "spect="<<spect<<endl;
		
		return out.str();
	}

		

	// to solve the test case and output the value to ostr
	std::string solveTestCase()
	{		
		stringstream out;
		long curStanding = 0;
		int nbInvites = 0;
		FOR(i, 0, spect.size())
		{
			char c = spect[i];
			// convert as int
			int nb = c-'0';
			//cout << "Convert of "<<c<<" ="<<nb<<endl;
			if (curStanding >= i)
			{
				// no need for invites
				curStanding += nb;
			}
			else if (nb > 0)
			{
				nbInvites += (i-curStanding);
				curStanding = i+nb;
			}
		}

		out <<nbInvites;
		return out.str();
	}

private:
	int maxVal;
	string spect;
	
};


int main(int argc, char* argv[])
{
	std::string inputFile("C:\\Users\\David\\Downloads\\A-large.in");
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