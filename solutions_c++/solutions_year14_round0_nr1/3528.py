#include <vector>
#include <fstream>
using namespace std;
int main()
{
	ifstream cin("A-small-attempt0.in");
	ofstream cout("A-small-attempt0.out");

	int t;
	cin >> t;
	int firstguess, secondguess;
	int first[4][4], second[4][4];
	bool comp[4];
	for (int l = 1; l <= t; ++l)
	{
		for (int i = 0; i < 4; ++i)
			comp[i] = false;
		cin >> firstguess;
		--firstguess;
		for (int i = 0; i < 4; ++i)
			for (int j = 0; j < 4; ++j)
				cin >> first[i][j];
		cin >> secondguess;
		--secondguess;
		for (int i = 0; i < 4; ++i)
			for (int j = 0; j < 4; ++j)
				cin >> second[i][j];

		//row,row
		for (int i = 0; i < 4; ++i)
		{
			for (int j = 0; j < 4; ++j)
			{
				if (second[secondguess][i] == first[firstguess][j])
				{
					comp[j] = 1;
				}
			}
		}
		int count = 0, r;
		for (int i = 0; i < 4; ++i)
		{
			count += comp[i];
			if (comp[i] != 0)
				r = i;
		}
		cout << "Case #" << l << ": ";
		if (count > 1)
			cout << "Bad magician!";
		else if (count == 0)
			cout << "Volunteer cheated!";
		else
			cout << first[firstguess][r];
		cout << endl;
	}
}