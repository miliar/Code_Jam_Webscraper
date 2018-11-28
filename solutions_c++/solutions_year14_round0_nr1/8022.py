#include <iostream>
#include <conio.h>
#include <fstream>

using namespace std;

int main()
{
	ifstream fin("input.in");
	ofstream fout("output.out");
	int countTest, a;
	fin >> countTest;
	pair<int, int>* strNumber = new pair<int, int>[countTest];
	int** matr = new int*[countTest];

	int* num = new int[countTest];

	for(int i = 0; i < countTest; ++i)
	{
		num[i] = -1;
		matr[i] = new int[4];
		fin >> strNumber[i].first;
		for(int j = 0; j < 4; ++j)
		{
			for(int k = 0; k < 4; ++k)
			{
				fin >> a;
				if(j == strNumber[i].first - 1) matr[i][k] = a;
			}
		}

		fin >> strNumber[i].second;
		for(int j = 0; j < 4; ++j)
		{
			for(int k = 0; k < 4; ++k)
			{
				fin >> a;
				if(j == strNumber[i].second - 1){
				for(int m = 0; m < 4; ++m)
				{
					if(a == matr[i][m])
					{
						if(num[i] == -1) num[i] = a;
						else
							{
								num[i] = -2;
								break;
						    } 
					}
				}
				}
			}
		}
	}

	for(int i = 0; i < countTest; ++i)
	{
		fout << "Case #" << i+1 << ": ";
		if(num[i] == -1) fout << "Volunteer cheated!" << endl;
		else if(num[i] == -2) fout << "Bad magician!" << endl;
		else fout << num[i] << endl;
	}

	_getch();
	return 0;
}