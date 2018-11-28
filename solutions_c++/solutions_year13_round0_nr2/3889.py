#include <fstream>
#include <vector>
#include <algorithm>

using namespace std;

bool check(int N, int M, vector<vector<int> > lawn, vector<int> max_row, vector<int> max_col);

int main()
{
	ifstream cin;
	cin.open("B-large.in");
	ofstream cout;
	cout.open("B_res_large.txt");

	int T;
	cin >> T;
	for(int t = 1; t <= T; t++)
	{
		int N, M;
		cin >> N >> M;
		vector<vector<int> > lawn;
		vector<int> max_row;
		vector<int> max_col;
		for(int i = 0; i < N; i++)
		{
			vector<int> row;
			int maxi = 0;
			for(int j = 0; j < M; j++)
			{
				int val;
				cin >> val;
				row.push_back(val);
				maxi = max(maxi, val);
			}
			lawn.push_back(row);
			max_row.push_back(maxi);
		}

		for(int j = 0; j < M; j++)
		{
			int maxi = 0;
			for(int i = 0; i < N; i++)
			{
				maxi = max(maxi, lawn[i][j]);
			}
			max_col.push_back(maxi);
		}

		cout << "Case #" << t << ": ";

		if(check(N,M,lawn,max_row,max_col)) cout << "YES" << endl;
		else cout << "NO" << endl;
	}

	cin.close();
	cout.close();

	return 0;
}

bool check(int N, int M, vector<vector<int> > lawn, vector<int> max_row, vector<int> max_col)
{
	for(int i = 0; i < N; i++)
	{
		for(int j = 0; j < M; j++)
		{
			if(lawn[i][j] < max_row[i] && lawn[i][j] < max_col[j])
				return false;
		}
	}

	return true;
}
