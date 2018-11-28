#include <iostream>
#include <fstream>
using namespace std;

int main()
{
	ifstream myInput;
	ofstream myOutput;
	char inputFileName[] = "//home//alex//Desktop//GoogleJam//Question 2//v2//B-large.in";
	char outputFileName[] = "//home//alex//Desktop//GoogleJam//Question 2//v2//B-large-attempt0.txt";

	myInput.open(inputFileName, ios::in);
	myOutput.open(outputFileName, ios::out);

	int T;
	myInput >> T;
	
	for (int x = 0; x < T; x++)
	{
		int pairCounter = 1;
		
		string cake;
		myInput >> cake;
		
		for (unsigned i = 1; i < cake.length(); i++)
		{ 
			if (cake[i] == cake[i - 1])
			{
				pairCounter--;
			} // end if
			
			pairCounter++;
		} // end for
			
		if (cake[cake.length() -1] == '+')
		{
			pairCounter --;
		} // end if

		myOutput << "Case #" << x + 1 << ": " << pairCounter << endl; 
	} // end for
} // end main
