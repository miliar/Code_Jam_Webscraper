#include <vector>
#include <fstream>
#include <iostream>
#include <cstdlib>
#include <string>

using namespace std;

int main()
{
	ifstream inputFile;
	unsigned int numberOfTestCases = 0;
	unsigned int currentTestCase = 0;

	inputFile.open("A-large.in");

	if ( inputFile.good() )
	{
		inputFile >> numberOfTestCases;
		while (currentTestCase<numberOfTestCases)
		{
            string audienceShyness;
            unsigned int maxShynessLevel;

            inputFile >> maxShynessLevel >> audienceShyness;

            int friendsNeeded = 0;
            int onStandingTotal = 0;
            for(int shy=0; shy <= maxShynessLevel; shy++)
            {
                if( onStandingTotal >= shy )
                {
                    onStandingTotal += audienceShyness[shy] - 48;
                }
                else
                {
                    friendsNeeded++;
                    onStandingTotal++;

                    onStandingTotal += audienceShyness[shy] - 48;
                }
            }

            cout << "Case #" << ++currentTestCase << ": " << friendsNeeded << endl;
		}
	}
	else
	{
        cout << "File Not Found" << endl;
	}

	return 0;
}
