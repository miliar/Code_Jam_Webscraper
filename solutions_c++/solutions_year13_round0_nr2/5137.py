#include <iostream>
#include <fstream>
#include <conio.h>
#include <ios>

using namespace std;

void main()
{
	cout << "Press any key to execute." << endl;
	_getch();

	/*loading file section*/
	ifstream inFile;
	inFile.open("B-large.in");
	if (!inFile.is_open())
	{
		cout << "Input File dose not exist." << endl;
		return;
	}

	/*reading file section*/
	//pre-reading
	ofstream outFile;
	outFile.open("B-large.out", ios_base::out|ios_base::trunc);
	if (!inFile.is_open())
	{
		cout << "Output File could not open." << endl;
		return;
	}
	int case_Count;
	//add parameter to be used here

	//reading procedure
	inFile >> case_Count;
	for (int i=0; i<case_Count; i++)
	{
		int N, M; // an N metre by M metre rectangle
		//输入
		inFile >> N >> M;
		int lawn[100][100];
		for (int j = 0; j < N; j++)
		{
			for (int k = 0; k < M; k++)
			{
				inFile >> lawn[j][k];
			}
		}
		//操作区
		// check every unit is the highest either in row or column
		bool bPossible = true;
		for (int j = 0; j < N; j++)
		{
			for (int k = 0; k < M; k++)
			{
				bool possible_row = true, possible_col = true;
				int unit = lawn[j][k];
				for (int _j = 0; _j < N; _j++)
				{
					if(unit < lawn[_j][k])
					{
						possible_row = false;
						break;
					}
				}
				for (int _k = 0; _k < M; _k++)
				{
					if(unit < lawn[j][_k])
					{
						possible_col = false;
						break;
					}
				}
				if (!possible_row && !possible_col) // row is false, col is false
				{
					bPossible = false;
					goto print_result;
				}
			}
		}
		//输出
print_result:
		if (bPossible)
		{
			outFile << "Case #" << i+1 << ": " << "YES" << endl;
		}
		else
		{
			outFile << "Case #" << i+1 << ": " << "NO" << endl;
		}
		outFile.flush();
	}

	/*exit section*/
	cout << "Press any key to exit." << endl;
	_getch();
	inFile.close();
	outFile.close();
	return;
}