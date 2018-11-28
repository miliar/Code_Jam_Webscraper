#include <iostream>
#include <limits>
#include <cstdlib>

using namespace std;

int main(int argc, char **argv){
	unsigned int countOfTestCases = 0;
	{
		char firstLine[5];
		cin.getline(firstLine, 5);
		countOfTestCases = atoi(firstLine);
	}
	for(unsigned int indexOfCurrentTestCase = 0; indexOfCurrentTestCase < countOfTestCases; indexOfCurrentTestCase++){
		unsigned int countOfShynessClusters = 0;
		{
			char shynessValue[6];
			cin.get(shynessValue,6,' ');
			countOfShynessClusters = atoi(shynessValue);
		}
		cin.ignore(1);
		unsigned long ovationLevel = 0;
		unsigned long friendCount = 0;
		for(unsigned int indexOfShynessCluster = 0; indexOfShynessCluster <= countOfShynessClusters; indexOfShynessCluster++){
			unsigned int peopleInCurrentCluster = cin.get() - '0';
			if(ovationLevel >= indexOfShynessCluster){
				ovationLevel += peopleInCurrentCluster;
			}else{
				unsigned int ovationMissing = indexOfShynessCluster - (unsigned int)ovationLevel;
				ovationLevel += ovationMissing + peopleInCurrentCluster;
				friendCount += ovationMissing;
			}
		}
		cout << "Case #" << (indexOfCurrentTestCase + 1) << ": " << friendCount << endl;
		if(indexOfCurrentTestCase < (countOfTestCases - 1)){
			cin.ignore(numeric_limits<streamsize>::max(), '\n');
		}
	}
	return 0;
}
