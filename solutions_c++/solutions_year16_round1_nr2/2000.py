#include <iostream>
#include <string>
#include <list>
#include <vector>
#include <math.h>
#include <sstream>
#include <unordered_map>
#include <algorithm>
using namespace std;
void ReadRankCases( list<list<int>>& oCases, int& oCount, int& oN )
{
	string read;
	cin >> oCount;
	for( int c = 0; c < oCount; ++c )
	{
		cin >> oN;
		int numLines = oN*2-1;
		list<int> tempList;
		for( int i = 0; i < numLines; ++i )
		{
			for( int j = 0; j < oN; ++j )
			{
				cin >> read ;
				tempList.push_back(stoi(read));
			}

		}
		oCases.push_back(tempList);
	}
	
}


void OutputRank(int iIndex, string iResult )//iResult[]
{
cout << "Case #" << iIndex << ": " << iResult<< endl;	

}

string FindMissingNote( list<int> iNumbers, int iN )
{
	unordered_map<int, int> countNumbers;
	for (list<int>::iterator it = iNumbers.begin(); it != iNumbers.end(); ++it)
	{
		++countNumbers[ *it];
	}

	vector<int> temp;
	for( auto it = countNumbers.begin(); it != countNumbers.end(); ++it )
	{
		if( (*it).second % 2 != 0 )
		{
			temp.push_back( (*it).first );
		}
	}

	sort(temp.begin(), temp.end());

	string result = "";
	for( int i =0; i < temp.size(); ++i)
	{
		result += to_string( (_LONGLONG)temp[i] );
		result += " ";
	}

	return result;
	
}

int main()
{

	//Read cases
	list<list<int>> cases;
	int count = 0;
	int n;
	ReadRankCases( cases,count,n  );

	int index = 1;
	for (list<list<int>>::iterator it = cases.begin(); it != cases.end(); ++it)
	{
		string result = FindMissingNote(*it, n);
		OutputRank(index, result);
		++index;
	}
	return 0;
}