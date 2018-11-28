// MagicTrick.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <fstream>
#include <vector>



#define INPUT_FILENAME		"infile.txt"
#define OUTPUT_FILENAME		"outfile.txt"



typedef int		ROW_T[4];



struct GRID_T
{
	ROW_T rows[4];

	bool CanFind(int num, int rowId) const
	{
		bool found=false;
		int idx=0;
		while (idx<4 && !found)
		{
			found = (rows[rowId][idx++] == num);
		}

		return found;
	}
};



struct TEST_CASE_T
{
	int answers[2];
	GRID_T grids[2];
};



void WriteOutputFile(const std::vector<TEST_CASE_T>* tc) 
{
	std::ofstream ofs(OUTPUT_FILENAME);

	for (int i=0; i<tc->size(); i++)
	{
		TEST_CASE_T tmp = tc->at(i);

		// Find how many numbers ........
		int howMany=0;
		int foundNum=-1;
		for (int j=0; j<4; j++)
		{
			int num = tmp.grids[0].rows[tmp.answers[0]-1][j];
			int rowId = tmp.answers[1]-1;
			if (tmp.grids[1].CanFind(num, rowId))
			{
				howMany++;
				foundNum = num;
			}
		}

		ofs << "Case #" << i+1 << ": ";
		if (howMany==0)
			ofs << "Volunteer cheated!";
		else if (howMany > 1)
			ofs << "Bad magician!";
		else ofs << foundNum;

		ofs << "\n";
	}

	ofs.close();
}



void ReadInputFile(std::vector<TEST_CASE_T>& tc) 
{
	std::ifstream ifs(INPUT_FILENAME);

	int nTestCases;

	ifs >> nTestCases;

	for (int i=0; i<nTestCases; i++)
	{
		TEST_CASE_T tmpTestCase;
		
		// Read single test case from file
		ifs >> tmpTestCase.answers[0];
		for (int j=0; j<4; j++)
			for (int k=0; k<4; k++)
				ifs >> tmpTestCase.grids[0].rows[j][k];
		ifs >> tmpTestCase.answers[1];
		for (int j=0; j<4; j++)
			for (int k=0; k<4; k++)
				ifs >> tmpTestCase.grids[1].rows[j][k];

		tc.push_back(tmpTestCase);
	}
	
	ifs.close();
}



int _tmain(int argc, _TCHAR* argv[])
{
	std::vector<TEST_CASE_T> testCases;

	ReadInputFile(testCases);
	WriteOutputFile(&testCases);

	return 0;
}