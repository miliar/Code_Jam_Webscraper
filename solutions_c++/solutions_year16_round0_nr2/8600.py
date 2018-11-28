#include <iostream>
#include <string>
#include <list>
#include <vector>

using namespace std;

void ReadCasesPancakes( list<string>& oStacks, int& oCount )
{
	string pancakes;
	cin >> oCount;
	for( int i = 0; i < oCount; ++i )
	{
		cin >> pancakes;
		oStacks.push_back(pancakes);
	}
}


void OutputPancakes(int iIndex, int iResult )//iResult[]
{
	
	cout << "Case #" << iIndex << ": " << iResult<< endl;
	
}


int Resort(string pancakes)
{
	int size =  pancakes.size();

	int pointer = 0;
	bool head = true;
	int countFlipped = 0;
	bool numberMinus = 0;	//how many elements are there in a group of '-'
	bool numberPlus = 0;
	while ( pointer < size  )
	{
		if( pancakes[pointer] == '+')	//is not 0th, and elements before it are all '-'
		{
			
			if( numberMinus > 0 ) ++countFlipped;
			++numberPlus;
			numberMinus = 0;
			
			
		}
		else if( pancakes[pointer] == '-')
		{
			if( numberPlus > 0 )
			{
				countFlipped += numberPlus;
			}
			
			numberPlus = 0;
			++numberMinus;
		}
		++pointer;
	}

	if(numberMinus>0) ++countFlipped;
	return countFlipped;
}

int main()
{
	//Read cases
	list<string> stacks;
	int count = 0;
	ReadCasesPancakes( stacks,count );

	int index = 1;
	for (list<string>::iterator it = stacks.begin(); it != stacks.end(); ++it)
	{
		int result = Resort(*it);
		OutputPancakes(index, result);
		++index;
	}
	return 0;

}