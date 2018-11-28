#include <iostream>
#include <vector>
#include <algorithm>
#include <cassert>

using namespace std;

void doCase()
{
	int R, C;
	
	cin >> R >> C;
	vector<vector<char> > grid(R,vector<char>(C));
	
	for (int i=0; i<R; i++)
	{
		for (int j=0; j<C; j++)
		{
			cin >> grid[i][j];
		}
	}
	
	vector<vector<int> > locInRow(R);
	vector<vector<int> > locInCol(C);
	
	for (int i=0; i<R; i++)
	{
		for (int j=0; j<C; j++)
		{
			if (grid[i][j] == '.')
				continue;
			
			locInRow[i].push_back(j);
			locInCol[j].push_back(i);
		}
	}
	
	for (int i=0; i<R; i++)
		sort(locInRow[i].begin(), locInRow[i].end());
	
	for (int j=0; j<C; j++)
		sort(locInCol[j].begin(), locInCol[j].end());
	
	int nChange = 0;
	
	for (int i=0; i<R; i++)
	{
		for (int j=0; j<C; j++)
		{
			if (grid[i][j] == '.')
				continue;
			
			if (locInCol[j].size() == 1 && locInRow[i].size() == 1)
			{
				cout << "IMPOSSIBLE" << endl;
				return;
			}
			
			switch(grid[i][j])
			{
			case '^':
				if (locInCol[j][0] == i)
					nChange++;
				break;
			case '<':
				if (locInRow[i][0] == j)
					nChange++;
				break;
			case 'v':
				if (locInCol[j].back() == i)
					nChange++;
				break;
			case '>':
				if (locInRow[i].back() == j)
					nChange++;
				break;
			default:
				assert(0);
			}
		}
	}
	
	cout << nChange << endl;
}

int main()
{
	int T;
	cin >> T;
	for (int i=0; i<T; i++)
	{
		cout << "Case #" << i+1 << ": ";
		doCase();
	}
	return 0;
}
