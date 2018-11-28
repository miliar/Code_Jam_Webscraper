#include <iostream>
#include <fstream>
#include <conio.h>
#include <ios>
#include <vector>
#include <algorithm>
#include <functional>

using namespace std;

void main()
{
	cout << "Press any key to execute." << endl;
	_getch();

	/*loading file section*/
	ifstream inFile;
	inFile.open("A-large.in");
	if (!inFile.is_open())
	{
		cout << "Input File dose not exist." << endl;
		return;
	}

	/*reading file section*/
	//pre-reading
	ofstream outFile;
	outFile.open("A-large.out", ios_base::out|ios_base::trunc);
	if (!inFile.is_open())
	{
		cout << "Output File could not open." << endl;
		return;
	}
	int case_Count;
	//add parameter to be used here
	long long Amote, N;

	//reading procedure
	inFile >> case_Count;
	for (int i=0; i<case_Count; i++)
	{
		//����
		inFile >> Amote >> N /*input data receiver*/;
		//������
		vector<long long> motes, ops;
		for (int j = 0; j < N; j++)
		{
			int t;
			inFile >> t;
			motes.push_back(t);
			ops.push_back(101);
		}

		sort(motes.begin(), motes.end(), less<long long>());

		long long Sum = Amote, op_count = 0;

		int jMax = motes.size()- op_count;
		for (int j = 0; j < jMax; j++)
		{
			if (Sum > motes[j])
			{
				Sum += motes[j];
			}
			else
			{ 
				ops[j] = op_count + (motes.size() - j); //quit
				while (Sum <= motes[j])
				{
					Sum += (Sum - 1);
					op_count++;
					if (op_count > jMax)
					{
						break;
					}
				}
				Sum += motes[j];
			}
		}

		for (int j=0; j<ops.size(); j++)
		{
			op_count = min(op_count, ops[j]);
		}
		
		//���
		outFile << "Case #" << i+1 << ": " << op_count << endl;
		outFile.flush();
	}

	/*exit section*/
	cout << "Press any key to exit." << endl;
	_getch();
	inFile.close();
	outFile.close();
	return;
}