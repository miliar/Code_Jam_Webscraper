// Google Code Jam 2015
// Round 1
// A
//
// Adrian Dale
// 02/05/2015

#include <iostream>
#include <string>
#include <iomanip>
#include <sstream>
#include <vector>
#include <algorithm>
#include <set>

using namespace std;

int T; // No of test cases

#define MAX_N 1000000

vector<int> StepsToHere(MAX_N+1, 0);

// Basic version
void SolveTestCase(int N)
{
	//cout << "Solving for  " << N << endl;
	cout << StepsToHere[N];
}

int ReverseN(int n)
{
	ostringstream nstream;
	nstream << n;
	string nrev = nstream.str();
	reverse(nrev.begin(), nrev.end());

	size_t start_pos = nrev.find_first_not_of('0');

	istringstream parser(nrev.substr(start_pos));
	int result;
	parser >> result;
	return result;
}

void Setup()
{
	StepsToHere[1] = 1;
	for (int i = 2; i <= MAX_N; i++)
	{
		

		if (StepsToHere[i] == 0)
		{
			StepsToHere[i] = StepsToHere[i-1]+1;
		}
		else
		{
			StepsToHere[i] = min(StepsToHere[i], StepsToHere[i - 1] + 1);
		}
		
		int rev = ReverseN(i);
		if (rev <= MAX_N)
		{
			if (StepsToHere[rev] == 0)
			{
				StepsToHere[rev] = min(i+1, StepsToHere[i] + 1);
			}
				if (StepsToHere[rev-1] != 0)
				{
					StepsToHere[rev] = min(StepsToHere[rev], StepsToHere[rev - 1] + 1);
				}
			
		}
	}
	//for (int i = 1; i < 100; ++i)
	//{
	//	cout << "i=" << i << " => " << StepsToHere[i] << endl;
	//}
}

void ReadTestCases()
{
	string line;

	getline(cin, line);
	istringstream parser(line);
	parser >> T;

	int TestNo = 1;
	while (TestNo <= T)
	{
		getline(cin, line);
		parser.str(line);
		parser.clear();
		int N;
		parser >> N;
		
		cout << "Case #" << TestNo << ": ";
		SolveTestCase(N);
		cout << endl;

		++TestNo;
	}
}

void Test01()
{
	for (int i = 1; i < 140; ++i)
	{
		cout << "i=" << i << " irev=" << ReverseN(i) << endl;
	}
}

int main()
{
	//Test01();
	Setup();
	ReadTestCases();
	//SolveTestCase(1, 1, "jij");
	return 0;
}
