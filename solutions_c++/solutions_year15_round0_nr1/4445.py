/**
* File:		Round00_ProbA.cpp
* Title:	Google Code Jam 2015 - Qualification Round - Problem A - Standing Ovation
* Author:	R.Quatrefoil
* Date:		2015-04-10
* Purpose:	Calculate minimum number of friends needed to overcome shyness levels of audience
* Notes:	Created using Microsoft Visual Studio 2013
*
*			String of members at each shyness level will never end in a 0
*			
*			Was going to read in to string, then convert to int array, but decided was unnecessary
*/

#include <iostream>
#include <fstream>

using namespace std;

int main()
{
	ifstream iFile("A-large.in", ios::in);
	ofstream oFile;		//will only open if iFile opens correctly

	int testCasesTotal = 0;		//total number of test cases to evaluate (from 1 to 1000)
	int extraMembers = 0;		//number of extra friends needed in audience to make everyone stand
	int standingMembers = 0;		//num audience members that are standing (don't care how many are sitting)
	int maxShyLevels = 0;		//num shyness levels in audience (0 to 6 levels in small; 0 to 1000 levels in large)
	int shyMembersCount = 0;		//num shy people of each level who stand if standingMembers >= their shyness level (0 to 9 for each level)

	if (iFile)
	{
		oFile.open("Round00_ProbA_Output.txt", ios::out | ios::trunc);

		iFile >> testCasesTotal;
		for (int currCase = 0; currCase < testCasesTotal; currCase++)		//evaluate all test cases
		{
			extraMembers = 0;		//re-init for each case
			standingMembers = 0;		//re-init for each case

			iFile >> maxShyLevels;		//re-read for each case
			iFile.get();		//remove the space between shyness levels and shyMembersCount

			//find the number of extra members needed to get everyone to stand in current case
			for (int currShyLevel = 0; currShyLevel <= maxShyLevels; currShyLevel++)		//<= needed as need enough audience members for last level, even though don't care how many stand then
			{
				shyMembersCount = int(iFile.get()) - int('0');		//convert input char to int

				if (standingMembers >= currShyLevel)
				{
					standingMembers += shyMembersCount;
				}
				else
				{
					extraMembers += (currShyLevel - standingMembers);
					standingMembers = currShyLevel;
					standingMembers += shyMembersCount;
				}
			}

			//output case to file
			oFile << "Case #" << (currCase + 1) << ": " << extraMembers << endl;		//not sure if last endl at very end is a problem
		}

		iFile.close();
		oFile.close();
		cout << "Output successful!!" << endl;
	}
	else
	{
		cout << "Error opening input file!!" << endl;
	}

	cout << endl << endl << "Press Enter key to continue..." << endl;
	cin.get();
	return 0;
}//endfcn main