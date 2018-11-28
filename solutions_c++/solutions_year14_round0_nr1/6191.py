// GCJ.cpp : Defines the entry point for the console application.
//
#include <cstdio>
#include <iostream>
#include <vector>
using namespace std;

int main()
{
	// First let's read the file
	freopen("gcj.in", "r", stdin);
	freopen("gcj.out", "w", stdout);

	int i, j, k, ans1, ans2, Ncases, tmp;

	cin >> Ncases;

	vector <vector<int>> first;
	vector <vector<int>> second;
	vector <int> row;

	// Outer loop is the number of cases
	for (k=0; k<Ncases; k++)
	{
		cin >> ans1;
		//cout << "Case #" << k+1 << ":" << ans1 << endl;
		// 1st matrix
		for (i=0; i<4; i++)
		{
			for (j=0; j<4; j++)
			{
				cin >> tmp;
				row.push_back(tmp);
			}
			//cout << "Row #" << i+1 << ":" << row[0] << " " << row[1] << " " << row[2] << " " << row[3] << endl;
			first.push_back(row);
			row.clear();
		}

		cin >> ans2;
		//cout << endl << "Case #" << k+1 << ":" << ans2 << endl;
		// 2nd matrix
		for (i=0; i<4; i++)
		{
			for (j=0; j<4; j++)
			{
				cin >> tmp;
				row.push_back(tmp);
			}
			//cout << "Row #" << i+1 << ":" << row[0] << " " << row[1] << " " << row[2] << " " << row[3] << endl;
			second.push_back(row);
			row.clear();
		}

		// Ok, lets figure out how to do this
		// Compare the values of ans1 to the values of ans2
		short numMatches = 0, theNum = 0;
		for (i=0; i<4; i++)
		{
			for (j=0; j<4; j++)
			{
				if(first[ans1-1][i] == second[ans2-1][j])
				{
					numMatches++;
					theNum = first[ans1-1][i];
				}
			}
		}

		cout << "Case #" << k+1 << ": ";
		switch(numMatches)
		{
		case 0:
			cout << "Volunteer cheated!" << endl;
			break;
		case 1:
			cout << theNum << endl;
			break;
		default:
			cout << "Bad magician!" << endl;
		}

		// Clean up
		for(i=0; i<4; i++)	first[i].clear();
		first.clear();
		for(i=0; i<4; i++)	second[i].clear();
		second.clear();
	}

	return 0;
}

