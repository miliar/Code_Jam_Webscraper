// Google Code Jam 2015
// Qualifying Round
// A - Standing Ovation
//
// Adrian Dale
// 11/04/2015

#include <iostream>
#include <string>
#include <iomanip>
#include <sstream>
#include <vector>
#include <algorithm>

using namespace std;

int T; // No of test cases

void SolveTestCase(int Smax, string Audience)
{
	//cout << "Solving for  " << Smax << ", " << Audience << endl;

	int standing = 0;
	
	int friendsAdded = 0;

	int shyLevel = 0;
	for (auto shyCountChar : Audience)
	{
		int shyCount = shyCountChar - '0';
		
		
		if (shyCount == 0)
		{
			++shyLevel;
			continue;
		}

		if (standing >= shyLevel)
		{
			standing += shyCount;
		}
		else
		{
			int toAdd = shyLevel - standing;
			friendsAdded+= toAdd;
			standing+=toAdd;
			standing += shyCount;
			
		}
		++shyLevel;
	}
	
	
	cout <<  friendsAdded;
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
		int Smax;
		parser >> Smax;
		string Audience;
		parser >> Audience;
		cout << "Case #" << TestNo << ": ";
		SolveTestCase(Smax, Audience);
		cout << endl;

		++TestNo;
	}
}

int main()
{
	ReadTestCases();
	//SolveTestCase(5, "110011");
	return 0;
}
