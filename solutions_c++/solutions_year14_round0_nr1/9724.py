#include <iostream>
#include <set>

using namespace std;

int main()
{
	freopen("in.txt", "rt", stdin);
	freopen("out.txt", "wt", stdout);
	int T;

	cin >> T;

	for(int t = 1; t <= T; t++)
	{
		cout << "Case #" << t << ": ";

		set<int> s;

		int row1, row2, first[5][5], second[5][5];

		cin >> row1;

		for(int i = 1; i <= 4; i++)
			for(int j = 1; j <= 4; j++)
				cin >> first[i][j];

		cin >> row2;

		for(int i = 1; i <= 4; i++)
			for(int j = 1; j <= 4; j++)
				cin >> second[i][j];

		for(int j = 1; j <= 4; j++)
			s.insert(first[row1][j]);

		int found = 0, notfound = 0, ans;

		for(int j = 1; j <= 4; j++)
		{
			int current = second[row2][j];

			if(s.find(current) != s.end())
			{
				found++;
				ans = current;
			}
			else
				notfound++;
		}

		if(found == 1 && notfound == 3)
			cout << ans << endl;
		else if(found > 1)
			cout << "Bad magician!" << endl;
		else if(notfound == 4)
			cout << "Volunteer cheated!" << endl;
	}

	return 0;
}