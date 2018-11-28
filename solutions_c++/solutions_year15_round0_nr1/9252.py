//////////////////////////////////////////////////////////////////////
/// @file ovation.cpp
/// @author "Jerry" Gerald Linder
/// @brief Google Code Jam 2015 Problem A: Standing Ovation
//////////////////////////////////////////////////////////////////////

#include <iostream>
#include <sstream>

using namespace std;

int main()
{
   //cout << "program started" << endl;
   //Static Variable Declarations:
   int numCases = 0;
   int numLevels = 0;
   //char * levels;
   int * intlevels;
   
   cin >> numCases;
   for (int j = 1; j <= numCases; j++)
   {
	
   int friendsNeeded = 0;
   int numClapping = 0;
   
	//cout << "main loop iteration " << h << endl;
	cin >> numLevels;
	numLevels++;
	//cout << "numlevels = " << numLevels << endl;
	
	//Dynamically allocate 1D array:
	/*
	levels = new char[numLevels+1];
	
	cin >> *levels;
	
	cout << "levels = " << *levels << endl;
	*/
	
	intlevels = new int[numLevels];
	
	//Populate int array from input file string:
	
	for (int i = 0; i < numLevels; i++)
	{	
		char c;
		cin >> c;
		//cout << c << endl;
		stringstream s;
		s << c;
		s >> intlevels[i];
	}
	
	//cout << "done with input loop" << endl;
	
	//Loop through shyness levels:
	
	numClapping = intlevels[0];
	
	for (int i = 1; i < numLevels; i++)
	{
		if (numClapping < i)
		{
			//cout << "numClapping = " << numClapping << endl;
			//cout << "level = " << intlevels[i] << endl;
			int numAdded = i - numClapping;
			numClapping += numAdded;
			friendsNeeded += numAdded;
		}
		numClapping += intlevels[i];
		//cout << "numClapping = " << numClapping << endl;

	}
	
	
	//Output Result:
	cout << "Case #" << j << ": " << friendsNeeded << endl;
	
	//Free arrays' memory:
	delete [] intlevels;
	
   }

   return 0;
}