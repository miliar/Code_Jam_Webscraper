#include "stdafx.h"
#include <fstream>
#include <vector>
//#include <string>

using namespace std;

int main() 
{
	int T;
	int curRow;
	int stupid;
	vector<int> row(4);
	vector<int> compareTo(4);
	int numCommon = 0;
	int ans;

	ofstream fout ("magic.out");
    ifstream fin ("A-small-attempt0.in");

	fin >> T;

	for (int i=0; i<T; i++)
	{
		fin >> curRow;
		for (int x=0; x<(curRow-1)*4; x++)
			fin >> stupid;
		for (int x=0; x<4; x++)
		{
			fin >> row[x];
			//fout << row[x];
		}
		for (int x=0; x<(4-curRow)*4; x++)
			fin >> stupid;

		//fout << endl;

		fin >> curRow;
		for (int x = 0; x<(curRow-1)*4; x++)
			fin >> stupid;
		for (int x=0; x<4; x++)
		{
			fin >> compareTo[x];
			//fout << compareTo[x];
		}
		for (int x=0; x<(4-curRow)*4; x++)
			fin >> stupid;


		for (int j = 0; j<4; j++)
			for (int k=0; k<4; k++)
				if (row[j] == compareTo[k])
				{
					numCommon++;
					ans = row[j];
				}

		if (numCommon == 0)
			fout << "Case #" << i+1 << ": Volunteer cheated!" << endl;
		else if (numCommon == 1)
			fout << "Case #" << i+1  << ": " << ans << endl;
		else
			fout << "Case #" << i+1 << ": Bad magician!" << endl;

		numCommon = 0;
	}

}