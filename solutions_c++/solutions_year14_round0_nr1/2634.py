#include <iostream>
#include <vector>
using namespace std;

int main ()
{
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	int grid[4][4];
	int T;
	cin >> T;
	int row;
	int rowEl[4];
	int rowEl2[4];
	for (int t=0; t<T; t++)
	{
		cin >> row; 
		row-=1;
		for (int i=0; i<4; i++)
			for (int j=0; j<4; j++)
				cin >> grid[i][j];
		for (int i=0; i<4; i++)
			rowEl[i]=grid[row][i];
		cin >> row;
		row-=1;
		for (int i=0; i<4; i++)
			for (int j=0; j<4; j++)
				cin >> grid[i][j];
		for (int i=0; i<4; i++)
			rowEl2[i]=grid[row][i];
		vector<int> matches;
		for (int i=0; i<4; i++)
		{
			for (int j=0; j<4; j++)
			{
				if (rowEl[i]==rowEl2[j])
					matches.push_back(rowEl[i]);
			}
		}
		if (matches.size()==0)
			cout << "Case #" << t+1 << ": Volunteer cheated!" << endl;
		else if (matches.size()!=1)
			cout << "Case #" << t+1 << ": Bad magician!" << endl;
		else cout << "Case #" << t+1 << ": " << matches[0] << endl;
		matches.clear();
	}
	return 0;
}