#include <iostream>
#include <fstream>
#include <vector>
using namespace std;

bool checkArr(int[]);

int main()
{
	ifstream myInput;
	ofstream myOutput;
	char inputFileName[] = "//home//alex//Desktop//GoogleJam//Question 1//v3//A-large.in";
	char outputFileName[] = "//home//alex//Desktop//GoogleJam//Question 1//v3//A-large-attemptX.txt";


	myInput.open(inputFileName, ios::in);
	myOutput.open(outputFileName, ios::out);
	
	int x;
	myInput >> x;
	
	for ( int i = 0; i < x; i++)
	{
		int sheep;
		myInput >> sheep;
		
		if (sheep == 0)
		{
			myOutput << "Case #" << i + 1 << ": INSOMNIA" << endl;
			continue;
		} // end if

		const int SIZE = 10;
		int array[SIZE] = {0};
		int max = 0;
		int count = 1;
		vector<int> digits;
		
		while (checkArr(array) == false)
		{
			int x = sheep * count;
			int temp = x;
			while (x)
			{
				digits.push_back(x % 10);
				x /= 10;
			} // end while
			
			for (unsigned i = 0; i < digits.size(); i++)
			{
				int current = digits[i];
				array[current]++;
			} // end for
				
				max = temp;
				count++;
		} // end while
		myOutput << "Case #" << i + 1 << ": " << max << endl;
	} // end for
} // end main

bool checkArr(int name[])
{
	for (int i = 0; i < 10; i++)
	{
		if (name[i] == 0)
		{
			return false;
		} // end if
	} // end for
	return true;
} // end checkArr
