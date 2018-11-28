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
		 istr >> N;
	}

	int countSheep(unsigned long long l)
	{
		stringstream ss;
		ss << l;
		string s = ss.str();
		for (char c : s)
		{
			digits.insert(c);
		}
		return digits.size();
	}

	// to solve the test case and output the value to ostr
	std::string solveTestCase()
	{
		stringstream ss;

		if (N > 0)
		{
			int lastCount = 0;
			int count = 0;
			unsigned long long val = N;
			int cycle = 0;
			do
			{
				lastCount = count;
				count = countSheep(val);
				//cout << val << endl;
				val += N;
				++cycle;
			} while (cycle < 100 && count < 10);

			if (count == 10)
				ss << val-N;
			else
				ss << "INSOMNIA";
		}
		else
		{
			ss << "INSOMNIA";
		}

		return ss.str();
	}

	set<char> digits;
	unsigned long long N;
};



int main(int argc, char* argv[])
{
	std::ios_base::sync_with_stdio(false);

	std::string inputFile("C:\\Users\\David\\Downloads\\A-large.in");
	std::string outputFile("C:\\GoogleJam\\A-large.out");

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