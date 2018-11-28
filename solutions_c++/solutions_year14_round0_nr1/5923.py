#include <fstream>
#include <iostream>
#include <cstdlib>
using namespace std;



int main(void)
{
	std::ifstream fileIn("A-small-attempt0.in");
	int caseNum;
	fileIn >> caseNum;
	int rowNum0, rowNum1;
	int array0[4][4];
	int array1[4][4];

	ofstream fileOut("output.txt");
	for(int i = 0; i < caseNum; i++)
	{
		fileIn >> rowNum0;
		for(int j = 0; j<4; j++)
		{
			for(int k=0;k<4;k++)
			{
				fileIn >> array0[j][k];
			}
		}
		fileIn >> rowNum1;
		for(int j = 0; j<4; j++)
		{
			for(int k=0;k<4;k++)
			{
				fileIn >> array1[j][k];
			}
		}

		int count = 0, result = 0;
		for(int l=0; l < 4; l++)
		{
			for(int m =0; m <4; m++)
			{
				if(array0[rowNum0-1][l]==array1[rowNum1-1][m])
				{
					count++;
					result = array0[rowNum0-1][l];
				}
			}
		}
		switch(count)
		{
			case 1:
				fileOut << "Case #" << i+1 << ": " << result << endl;
				break;
			case 0:
				fileOut << "Case #" << i+1 << ": Volunteer cheated!" << endl;
				break;
			default:
			 	fileOut << "Case #" << i+1 << ": Bad magician!" << endl;
			 	break;
		}

	}
	fileIn.close();
	fileOut.close();



	return 0;
}