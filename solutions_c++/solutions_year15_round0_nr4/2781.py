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

struct cmp
{
	bool operator()(int i, int j)
	{
		return i >j;
	}
};

class TestCaseSolver 
{
public:
	TestCaseSolver() {
	}

	// to read/init the test case
	void readTestCase(std::istream &istr)
	{

		istr >> size;
		istr >> x;
		istr >> y;
		
		FOR(i,0,nbPlates)
		{
			int n;
			istr >> n;
			plates.push_back(n);
		}
	}

	// to check test case reading was ok
	std::string toString() const 
	{
		stringstream out;
		//out << "spect="<<spect<<endl;
		
		return out.str();
	}


	int getTimeToEat(list<int> &pan)
	{
		pan.sort(cmp());
		int maxVal = pan.front();
		if (maxVal <= 3)
			return maxVal;

		list<int> pan1 = pan;
		eatOne(pan1);

		int time1 = 1 + getTimeToEat(pan1);
		// alternative : split max plate in two and recall time to eat on new list

		int minTime = 100000;
		int lastVal = -1;
		list<int>::iterator it, itEnd;
		for (it = pan.begin(), itEnd = pan.end() ; it != itEnd ; ++it)
		{
			int val = *it;
			if (val == lastVal)
				continue; // skip it, already tried

			if (val < (lastVal - 2) || val <= 3)
				break;

			lastVal = val;
			int n1 = val/2;

			list<int> pan2;
			pan2.insert(pan2.end(), pan.begin(), it);
			list<int>::iterator it2 = it;
			++it2;
			pan2.insert(pan2.end(), it2, itEnd);		
			
			pan2.push_back((*it)/2);
			pan2.push_back((*it+1)/2);
			
			int time2 = 1 + getTimeToEat(pan2);
			if (time2<minTime)
				minTime = time2;
		}
//		if (maxVal%2 == 0)
	/*	{
			int n1 = maxVal/2;

			list<int> pan2 = pan;
			pan2.front() -= n1;
			pan2.push_back(n1);
			
			time2 = 1 + getTimeToEat(pan2);
		}
		*/

		return min (time1, minTime);

	}
		

	// to solve the test case and output the value to ostr
	std::string solveTestCase()
	{		
		stringstream out;

		//long time = 0;

		// check lowest possible time

//		time = (getTimeToEat(plates));

		bool bWinGabriel = false;

		if (size <=1)
			bWinGabriel = true;
		else
		{
			if (size == 2)
			{
				if ((x*y)%2 == 0)
					bWinGabriel = true;
			}
			else if (size == 3)
			{
				if ((x*y)%3 == 0)
				{
					if (x >= 2 && y>= 2)
						bWinGabriel = true;
				}
			}
			else // size 4
			{
				if ((x*y)%4 == 0)
				{
					if (x >= 2 && y>= 2)
					{
						if (x>=3 && y>=3)
							bWinGabriel = true;
						else
						{
							if (x*y >= 12)
								bWinGabriel = true;
						}
					}
				}
			}
		}


		if (bWinGabriel)
			out << "GABRIEL";
		else
			out << "RICHARD";
		return out.str();
	}

	void eatOne(list<int> &p)
	{
		list<int>::iterator it, itEnd;

		for (it = p.begin(), itEnd = p.end() ; it != itEnd ; ++it)
		{
			// if new val is 0 cut just before it (consider P is always sorted)
			if ((*it)<=1)
			{
				// cut
				p.erase(it, itEnd);
				break;
			}
			if (*it)
				(*it) -=1;
		}
	}

private:
	int nbPlates;
	list<int> plates;

	int size;
	int x;
	int y;

};


int main(int argc, char* argv[])
{
	std::string inputFile("C:\\Users\\David\\Downloads\\D-small-attempt0 (1).in");
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

		cout << res<<endl;
		out << res << endl;
	}

	return 0;
}