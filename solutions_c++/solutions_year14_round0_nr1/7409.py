#include <vector>
#include <algorithm>
#include <iostream>
using namespace std;

int main()
{
	int num_cases;
	cin >> num_cases;
	for(int c = 0; c < num_cases; c++)
	{
		vector<vector<int>> first_grid(4, vector<int>(4));
		auto second_grid = first_grid;
		int first_row, second_row;
		cin >> first_row;
		for(int n = 0; n < 4; n++)
			for(int m = 0; m < 4; m++)
				cin >> first_grid[n][m];
		cin >> second_row;
		for(int n = 0; n < 4; n++)
			for(int m = 0; m < 4; m++)
				cin >> second_grid[n][m];

		vector<int> first_ans, ans;
		for(int n = 0; n < 4; n++)
			first_ans.push_back(first_grid[first_row-1][n]);
		for(int n = 0; n < 4; n++)
		{
			int cur = second_grid[second_row-1][n];
			if( find(first_ans.begin(), first_ans.end(), cur) != first_ans.end() )
				ans.push_back(cur);
		}

		cout << "Case #" << c+1 << ": ";
		if( ans.size() == 0 )
			cout << "Volunteer cheated!";
		else if( ans.size() == 1 )
		{
			 cout << ans.back();
		}
		else
			cout << "Bad magician!";
		cout << endl;
	}
	return 0;
}
