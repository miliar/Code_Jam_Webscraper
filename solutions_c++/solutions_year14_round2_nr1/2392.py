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


struct multipleLetter
{
	char letter;
	int nb;
	int startPosInString;
};

class TestCaseSolver 
{
public:
	TestCaseSolver() {
	}

	// to read/init the test case
	void readTestCase(std::istream &istr)
	{
		maxl = 0;
		istr >> n;
		
		FOR(i,0,n)
		{
			string s;
			istr >> s;
			str.push_back(s);

			if (s.length()>maxl) {
				longestStr = s;
				maxl = s.length();
			}
		}

	}

	// to check test case reading was ok
	std::string toString() const 
	{
		string str = "TODO";
		return str;
	}

	
	bool strip(string str)
	{
		string minStr = "";
		list<multipleLetter> lmulti;
		int ifinalPos = 0;
		FOR(i, 0, str.length())
		{
			minStr.push_back(str[i]);
			multipleLetter m;
			m.letter = str[i];
			m.nb=1;
			m.startPosInString=ifinalPos;
			++ifinalPos;

			while ((i+1)<str.length() && str[i] == str[i+1])
			{
				++m.nb;
				++i;
			}
			
			if (m.nb>1)
				lmulti.push_back(m);
		}
		mults.push_back(lmulti);
		if (basicString.empty())
			basicString = minStr;
		if (minStr != basicString)
			return false;
		return true;
	}
	

	// to solve the test case and output the value to ostr
	std::string solveTestCase()
	{
		int iNbMod = 0;
		bool bSuccess = false;
		list<string>::iterator it, itEnd = str.end();
		
		int iCurChar = 0;
		

		for (it = str.begin() ; it != itEnd ; ++it)
		{
			bSuccess = strip(*it);
			if (bSuccess == false)
				break;
		}

		if (bSuccess)
		{
			list< list <multipleLetter> > mults2 = mults;

			// now parse and find a way to minimize transformations
			list< list <multipleLetter> >::iterator itm, itmend= mults.end();
			for (int icur=0; icur < basicString.length();++icur)
			{
				int totalOcc = 0;
				int meanOcc = 1;
				for (itm = mults.begin();itm != itmend;++itm)
				{
					if (!(*itm).empty() && (*itm).front().startPosInString==icur)
					{
						totalOcc += (*itm).front().nb;
						(*itm).pop_front();
					}
					else
						++totalOcc;
				
				}
				meanOcc = (int)ceil (((double)totalOcc)/n);
				if ((double(meanOcc)) - ((double)totalOcc)/n > 0.5)
					--meanOcc;

				//int iNbOp = 0;
				int inbTooMuch = 0;
				list< list <multipleLetter> >::iterator itm2, itmend2= mults2.end();
				for (itm2 = mults2.begin();itm2 != itmend2;++itm2)
				{
					if (!(*itm2).empty() && (*itm2).front().startPosInString==icur)
					{
						iNbMod += abs((*itm2).front().nb-meanOcc);
						(*itm2).pop_front();
					}
					else{
						iNbMod += abs(1-meanOcc);
					}

				}
			}
		}

		stringstream out;
		if (bSuccess)
			out << iNbMod;
		else 
			out << "Fegla Won";
		return out.str();
	}

private:
	int n;
	int maxl;
	string longestStr;
	list<string> str;

	list< list <multipleLetter> >mults;
	string basicString;
};


int main(int argc, char* argv[])
{
	std::string inputFile("C:\\Users\\David\\Downloads\\A-small-attempt0 (2).in");
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