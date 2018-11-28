#include <vector>
#include <fstream>
#include <random>
#include <iostream>
using std::vector;
using std::cout;
using std::cin;
using std::endl;
int findMatch(vector<int> &v1, vector<int> &v2)
{
	vector<int> maybe;
	for (int i = 0; i < 4; i++)
	{
		for (int j = 0; j < 4; j++)
		{
			if (v1[i] == v2[j])
			{
				maybe.push_back(v1[i]);
			}
		}
	}
	if (maybe.size() == 1)
	{
		return maybe.back();
	}
	else if (maybe.size() > 1)
	{
		return -1;
	}
	else
	{
		return 0;
	}
}
void main()
{
	std::ifstream inFile;
	std::ofstream outFile;
	vector<int> rows;
	vector<int> tempVector;
	//vector<int> output;
	inFile.open("C:/Users/Brendan/Dropbox/Compsci/test.in");
	cout << "test.txt opened fine" << endl;
	int T;
	int temp;
	vector<vector<vector<int>>> victor;
	inFile >> T;
	for (unsigned int i = 0; i < T * 2; i++)
	{
		victor.push_back(vector<vector<int>>(4, vector<int>(4)));
		inFile >> temp;
		rows.push_back(temp);
		cout << temp << endl;
		for (unsigned int j = 0; j < 4; j++)
		{
			for (unsigned int k = 0; k < 4; k++)
			{
				inFile >> temp;
				cout << temp << " ";
				victor[i][j][k] = temp;

			}
			cout << endl;
		}
	}

	inFile.close();
	outFile.open("C:/Users/Brendan/Dropbox/Compsci/jam.txt");
	cout << "jam.txt opened fine" << endl;
	int num = 0;
	for (unsigned int i = 0; i < 2 * T;)
	{
		num = rows[i] - 1;
		tempVector = victor[i][num];
		int output = findMatch(tempVector, victor[i + 1][rows[i + 1] - 1]);
		outFile << "Case #";
		outFile << i/2 + 1;
		outFile << ": ";
		if (output == -1)
		{
			cout << "Case #" << i / 2 + 1 << ": " << "Bad magician!" << endl;
			outFile << "Bad magician!";
		}
		else if (output == 0)
		{
			cout << "Case #" << i / 2 + 1 << ": " << "Volunteer cheated!" << endl;
			outFile << "Volunteer cheated!";
		}
		else
		{
			cout << "Case #" << i / 2 + 1 << ": " << output << endl;
			outFile << output;
		}
		outFile << "\n";
		i += 2;
	}
	outFile.close();
	system("PAUSE");
}
