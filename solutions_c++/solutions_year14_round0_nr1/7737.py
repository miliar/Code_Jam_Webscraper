#include "iostream"
#include "vector"
#include <stdio.h>
#include <stdlib.h>

using namespace std;

int main ()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int T;
	cin >> T;
	for (int test = 0; test < T; ++test)
	{
		vector<int> marks(17);
		int cards[16][16];
		for (int h = 0; h < 2; ++h)
		{
			int answer1 = 0;
			cin >> answer1;
			for (int i = 0; i < 4; ++i)
			{
				for (int j = 0; j < 4; ++j)
				{
					cin >> cards[i][j];
				}
			}
			for (int j = 0; j < 4; ++j)
			{
				marks[cards[answer1 - 1][j]]++;
			}
		}
		int answer = 0;
		int number = 0;
		for (int s = 1; s < 17; ++s)
		{
			if (marks[s] == 2)
			{
				answer++;
				number = s;
			}
		}
		cout << "Case #"<< test + 1 << ": ";
		if (answer == 0)
		{
			cout << "Volunteer cheated!" << endl;
		}
		else if (answer == 1)
		{
			cout << number<< endl;
		}
		else
		{
			cout << "Bad magician!" << endl;
		}
	}
	return 0;
}