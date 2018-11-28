// Magic Trick.cpp : Defines the entry point for the console application.
//

#include <iostream>

using namespace std;

int main()
{
	int maze[4][4],maze2[4][4];
	int t,ans1,ans2,ansFinal,count;
	freopen("A-small-attempt0.in", "r", stdin);
	freopen("A-small-attempt0.out", "w", stdout);
	cin >> t;
	for (int i = 0; i < t; i++)
	{
		ansFinal = -1;
		count = 0;
		cin >> ans1;
		ans1--;
		for (int j = 0; j < 4; j++)
		{
			for (int k = 0; k < 4; k++)
			{
				cin >> maze[j][k];
			}
		}
		cin >> ans2;
		ans2--;
		for (int j = 0; j < 4; j++)
		{
			for (int k = 0; k < 4; k++)
			{
				cin >> maze2[j][k];
			}
		}

		for (int j = 0; j < 4; j++)
		{
			for (int k = 0; k < 4; k++)
			{
				int temp1 = maze[ans1][j];
				int temp2 = maze2[ans2][k];
				if (maze[ans1][j] == maze2[ans2][k]){
					ansFinal = maze[ans1][j];
					count++;
					continue;
				}
			}
		}
		if (count == 0){
			cout << "Case #" << (i + 1) << ": Volunteer cheated!" << endl;
		}
		else if (count == 1){
			cout << "Case #" << (i + 1) << ": "<<ansFinal << endl;
		}
		else{
			cout << "Case #" << (i + 1) << ": Bad magician!" << endl;
		}
	}
}