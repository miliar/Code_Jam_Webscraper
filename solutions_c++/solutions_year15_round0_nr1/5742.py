#include <iostream>
#include <fstream>
#include <vector>
#include <string>

using namespace std;

void main()
{
	ifstream Input;
	ofstream Output;
	Input.open("A-large.in");
	Output.open("A-large.out");

	int Count , TotalMonth , DayCount , WeekCount;

	int i,j;
	Input >> Count;
	Count += 1;

	for (i = 1; i < Count; i++)
	{
		int Array = 0;
		int StandCount = 0;
		int TotalAddCount = 0;
		string ArrayValue;

		Input >> Array >> ArrayValue ;

		for(j = 0 ; j <= Array ; j++)
		{
			char NumberChar[2] = {};
			NumberChar[0] = ArrayValue.at(j);

			int Number = atoi(NumberChar);

			StandCount += Number;

			if(StandCount < j + 1)
			{
				int AddCount = j + 1 - StandCount + Number;
				
				StandCount += AddCount;
				TotalAddCount += AddCount;
			}
		}


		Output << "Case #" << i <<": " << TotalAddCount << endl;
	}

	return;
}