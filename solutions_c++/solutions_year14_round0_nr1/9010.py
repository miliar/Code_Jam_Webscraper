#include <iostream>
#include <fstream>

using namespace std;

int main()
{
	ifstream fin("in.txt");
	ofstream fout("out.txt");
	cin.rdbuf(fin.rdbuf());
	cout.rdbuf(fout.rdbuf());
	int t;
	cin >> t;
	for (int i = 1;i <= t;i++)
	{
		int a1, r1[4][4], a2, r2[4][4];
		cin >> a1;
		for (int j = 0; j < 4; j++)
			for (int h = 0; h < 4; h++)
				cin >> r1[j][h];
		cin >> a2;
		for (int j = 0; j < 4; j++)
			for (int h = 0; h < 4; h++)
				cin >> r2[j][h];
		int answer = -1;
		for (int j = 0; j < 4; j++)
			for (int h = 0; h < 4; h++)
				if (r1[a1 - 1][j] == r2[a2 - 1][h])
				{
					if (answer == -1)
					{
						answer = r1[a1 - 1][j];
					}
					else 
					{
						answer = 0;
					}
				}
		cout << "Case #" << i << ": ";
		if (answer == -1)
			cout << "Volunteer cheated!";
		else if (answer == 0)
			cout << "Bad magician!";
		else
			cout << answer;
		cout << "\n";
	}
	return 0;
}