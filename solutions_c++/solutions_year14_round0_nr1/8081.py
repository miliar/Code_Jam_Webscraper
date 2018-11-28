#include <iostream>
#include <vector>

using namespace std;

int main(int args, char** argv)
{
	int T = 0;
	cin >> T >> ws;

	for(int i = 1; i <= T; i++)
	{
		int first_row;
		cin >> first_row >> ws;

		vector<int> row1;
		int a,b,c,d;

		// get first row
		for(int j = 1; j <= 4; j++)
		{
			cin >> a >> b >> c >> d >> ws;
			if(j == first_row)
			{
				row1.push_back(a);
				row1.push_back(b);
				row1.push_back(c);
				row1.push_back(d);
			}
		}

		int second_row;
		cin >> second_row >> ws;

		vector<int> row2;

		// get second row
		for(int j = 1; j <= 4; j++)
		{
			cin >> a >> b >> c >> d >> ws;
			if(j == second_row)
			{
				row2.push_back(a);
				row2.push_back(b);
				row2.push_back(c);
				row2.push_back(d);
			}
		}

		// compare rows
		int finds = 0;
		int ans = 0;
		for(int j = 0; j < 4; j++)
		{
			if(find(row2.begin(), row2.end(), row1[j]) != row2.end())
			{
				finds++;
				ans = row1[j];
			}
		}

		if(finds == 0)
			cout << "Case #" << i << ": Volunteer cheated!" << endl;
		else if(finds == 1)
			cout << "Case #" << i << ": " << ans << endl;
		else
			cout << "Case #" << i << ": Bad magician!" << endl;
	}
	return 0;
}
