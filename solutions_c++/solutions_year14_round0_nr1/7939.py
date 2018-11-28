#include<iostream>
#include<fstream>
#include<sstream>
#include<conio.h>
#include<cstring>

using namespace std;
typedef unsigned int uint;

int CheckEqual(uint *a, uint *b, uint n,uint &index)
{
	int count = 0;
	for (uint i = 0; i < n; i++)
	{
		for (uint j = 0; j < n; j++)
		{
			if (a[i] == b[j])
			{
				count++;
				index = i;
				break;
			}
		}
	}
	return count;
}

int main()
{
	uint testcases = 0;
	uint row1 = 0, row2 = 0;
	uint a[4];
	uint b[4];
	ifstream in("E:\\A-small-attempt0.in", ios::in);
	ofstream out("E:\\testout.in", ios::out);
	string line;
	getline(in, line);
	stringstream ss(line);
	ss >> testcases;
	int i = 0, j = 0;
	for (i = 1; i <= testcases; i++)
	{
		getline(in, line);
		stringstream ss1(line);
		ss1 >> row1;
		for (j = 1; j < row1; j++)
		{
			getline(in, line);
		}

		getline(in, line);
		stringstream ss3(line);
		ss3 >> a[0] >> a[1] >> a[2] >> a[3];
		for (j = row1; j < 4; j++)
		{
			getline(in, line);
		}
		getline(in, line);
		stringstream ss2(line);
		ss2 >> row2;
		for (j = 1; j < row2; j++)
		{
			getline(in, line);
		}

		getline(in, line);
		stringstream ss4(line);
		ss4 >> b[0] >> b[1] >> b[2] >> b[3];
		for (j = row2; j < 4; j++)
		{
			getline(in, line);
		}
		uint index = 0;
		uint count = CheckEqual(a, b, 4, index);
		switch (count)
		{
		case 0:
			out << "Case #" << i << ":" << " Volunteer cheated!" << endl;
			break;
		case 1:
			out << "Case #" << i << ":" << " " << a[index] << endl;
			break;
		default:
			out << "Case #" << i << ":" << " Bad magician!" << endl;
			break;
		}
	}
	_getch();
	return 0;
}