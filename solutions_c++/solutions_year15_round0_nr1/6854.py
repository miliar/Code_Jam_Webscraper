#include <iostream>
#include <fstream>
#include <vector>
#include <string>

using namespace std;

int main()
{
	fstream fin;
	fin.open("data.txt", ios::in);
	fstream fout;
	fout.open("dataOut.txt", ios::out);

	int numCases = 0;

	fin >> numCases;
	vector<int> cases;

	
	int maxShyness;
	vector<int> values;


	for(int i = 0; i < numCases; i++)
	{
		fin >> maxShyness;
		maxShyness += 1;
		int tempVal;
		char tempChar[1];
		fin.get();
		for (int i = 0; i < maxShyness; i++)
		{
			tempChar[0] = fin.get();
			values.push_back(atoi(tempChar));
		}
		fin.get();
		int tempSum = 0;
		int missingValues = 0;
		for (int j = 0; j < maxShyness; j++)
		{
			if (tempSum < j)
			{
				missingValues++;
				tempSum++;
			}
			tempSum += values[j];
		}
		fout << "Case #" << i + 1 << ": " << missingValues << endl;
		values.clear();
	}

	system("pause");

};