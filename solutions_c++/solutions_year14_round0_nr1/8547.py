#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>

using namespace std;

int main()
{
	int T;
	ifstream fin("A-small-attempt0.in");
	ofstream fout("A-small-attempt0.out");
	fin >> T;
	int mat[4][4];
	for (int t = 0; t < T; ++t)
	{
		int row;
		vector<int> cards;
		fin >> row;
		for (int i = 0; i < 4; ++i)
		{
			for (int j = 0; j < 4; ++j)
			{
				fin >> mat[i][j];
			}
		}
		for (int j = 0; j < 4; ++j)
			cards.push_back(mat[row-1][j]);

		vector<int> cards2;
		fin >> row;
		for (int i = 0; i < 4; ++i)
		{
			for (int j = 0; j < 4; ++j)
			{
				fin >> mat[i][j];
			}
		}
		for (int j = 0; j < 4; ++j)
		{
			if (find(cards.begin(), cards.end(), mat[row-1][j]) != cards.end())
				cards2.push_back(mat[row-1][j]);
		}
		cout << "Case #" << t + 1 << ":" << endl;
		cout << "\tCards 1: ";
		for (vector<int>::iterator it = cards.begin(); it != cards.end(); ++it)
			cout << *it << " ";
		cout << endl << "\tCards 2: ";;
		for (vector<int>::iterator it = cards2.begin(); it != cards2.end(); ++it)
			cout << *it << " ";
		cout << endl;
		switch (cards2.size())
		{
		case 0:
			fout << "Case #" << t + 1 << ": Volunteer cheated!" << endl;
			break;
		case 1:
			fout << "Case #" << t + 1 << ": "<< cards2.front() << endl;
			break;
		default:
			fout << "Case #" << t + 1 << ": Bad magician!" << endl;
			break;
		}

	}
}