#include <iostream>
#include <fstream>
#include <cstdio>
#include <vector>

using namespace std;

string GetResult(vector<int> row1, vector<int> row2)
{
	int result = -1;
	bool found = false;

	for (int i = 0; i < 4; i++)
	{
		for (int j = 0; j < 4; j++)
		{
			if (row1.at(i) == row2.at(j))
			{
				if (!found) 
				{
					result = row1.at(i);
					found = true;
				}
				else
				{
					result = -2;
				}
			}
		}
	}

	if (!found)
		result = -3;

	char buffer[5] = { 0 };

	switch (result)
	{
	case -3:
		return "Volunteer cheated!";
	case -2:
		return "Bad magician!";
	default:
		sprintf_s(buffer, "%d", result);
		return buffer;
	}
}

/*
	-3 = VOLUNTEER CHEATED
	-2 = MAGICIAN CHEATED
	1-16= ANSWER
*/

vector<int> StringToVector(string x)
{
	vector<int> temp;
	int num = 0;
	for (int i = 0; i < x.size(); i++)
	{
		char c = x.at(i);
		if (c == ' ')
		{
			temp.push_back(num);
			num = 0;
		}
		else
		{
			num *= 10;
			int digit = (int) (c - '0');
			num += digit;
		}
	}
	temp.push_back(num);
	return temp;
}

int main()
{
	ifstream fin("input.txt", ios::in);
	ofstream fout("output.txt", ios::out);

	char buffer[5] = { 0 };
	fin.getline(buffer, 5, '\n');
	int nTests = atoi(buffer);

	for (int _case = 1; _case <= nTests; ++_case)
	{
		fin.getline(buffer, 5, '\n');
		int ans1 = atoi(buffer);

		vector<string> arr1;
		char temp [15] = { 0 };
		for (int i = 0; i < 4; i++)
		{
			fin.getline(temp, 15, '\n');
			arr1.push_back(temp);
		}

		char strAns2[5] = { 0 };
		fin.getline(strAns2, 5, '\n');
		int ans2 = atoi(strAns2);

		vector<string> arr2;
		for (int i = 0; i < 4; i++)
		{
			fin.getline(temp, 15, '\n');
			arr2.push_back(temp);
		}

		vector<int> row1 = StringToVector(arr1.at(ans1-1));
		vector<int> row2 = StringToVector(arr2.at(ans2-1));

		string result = GetResult(row1, row2);

		fout << "Case #" << _case << ": " << result.c_str() << endl;
	}

	fin.close();
	fout.close();
	return 0;
}