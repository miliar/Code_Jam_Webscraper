#include <iostream>
#include <string>
#include <list>
#include <vector>
#include <math.h>

using namespace std;
void ReadTheLastWordCases( list<string>& oStrings, int& oCount )
{
	string word;
	cin >> oCount;
	for( int i = 0; i < oCount; ++i )
	{
		cin >> word;
		oStrings.push_back(word);
	}
}


void OutputTheLastWord(int iIndex, list<char> iResult )//iResult[]
{

	cout << "Case #" << iIndex << ": ";
	for(list<char>::iterator it = iResult.begin(); it != iResult.end(); ++it)
	{
		cout << *it;
	}
	cout << endl;

}

list<char> FindLastWord(string iWord)
{
	list<char> result;
	result.push_back(iWord[0]);
	for( int i = 1; i < iWord.size(); ++i )
	{
		if(iWord[i] < result.front())
		{
			result.push_back(iWord[i]);
		}
		else
		{
			result.push_front(iWord[i]);
		}
	}
	return result;
}

int main()
{

	//Read cases
	list<string> strings;
	int count = 0;
	ReadTheLastWordCases( strings,count );

	int index = 1;
	for (list<string>::iterator it = strings.begin(); it != strings.end(); ++it)
	{
		list<char> result = FindLastWord(*it);
		OutputTheLastWord(index, result);
		++index;
	}
	return 0;
}