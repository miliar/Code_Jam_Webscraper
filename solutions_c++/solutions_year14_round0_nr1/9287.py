

#include <iostream>
#include <string>
#include <sstream>
#include <cstdlib>

using namespace std;


string compArray(int* myArr1, int* myArr2)
{
	int myNum;
	bool match = false;
	bool badM = false;
	bool volCheat = false;
	ostringstream Convert;

	for(int arr1= 0; arr1 < 4; arr1++)
	{

		
		for(int arr2= 0; arr2 < 4; arr2++)
		{
			if (myArr1[arr1] == myArr2[arr2])
			{
    			myNum = myArr1[arr1];
			   if (match)
			   	 badM = true;	
			   match = true;
			}
		} 	
	}
	
	if ( match && badM )
		return "Bad magician!";
	if ( match && !badM )
	{
		Convert << myNum;
	    return Convert.str();
	}
	if (!match)
		return "Volunteer cheated!";
}

int main(void) //Main Routine where the above written functions are called
{
	int numTestCases;
	cin >> numTestCases;
	
	int Arrangement[4][2][numTestCases][4];
	int cardsPicked[numTestCases][2];
	
	for (int tCaseCount = 0; tCaseCount < numTestCases; tCaseCount++)
	{
		int myRow;
	    cin >> myRow;
	    cardsPicked[tCaseCount][0] = myRow - 1;
		for (int rowCount = 0; rowCount < 4; rowCount++)
		{
			for (int colCount = 0; colCount < 4; colCount++)
			{
				cin >> Arrangement[rowCount][0][tCaseCount][colCount];
			}
		}
		
	    cin >> myRow;
	    cardsPicked[tCaseCount][1] = myRow - 1;
	  
		for (int rowCount = 0; rowCount < 4; rowCount++)
		{
			for (int colCount = 0; colCount < 4; colCount++)
			{
				cin >> Arrangement[rowCount][1][tCaseCount][colCount];
			}
		}
	}
	
	for (int tCaseCount = 0; tCaseCount < numTestCases; tCaseCount++)
	{
		cout << "Case #" << (tCaseCount + 1) << ": " << compArray(Arrangement[cardsPicked[tCaseCount][0]][0][tCaseCount], Arrangement[cardsPicked[tCaseCount][1]][1][tCaseCount]) << endl; 
	}
	
}

