#include <iostream>

using namespace std;

int l[100][100], n, m;

bool isPossible(const int p1, const int p2)
{
	bool possible = true;
	for (int i = 0; i < n && possible; i++)
	{
		possible = l[p1][p2] >= l[i][p2];
	}
	if (possible)
		return true;
	possible = true;
	for (int i = 0; i < m && possible; i++)
	{
		possible = l[p1][p2] >= l[p1][i];
	}
	return possible;
}

int main(int argc, char* argv[])
{
	int T;
	cin>>T;
	bool possible;
	for (int t = 1; t <= T; t++)
	{
		possible = true;
		cout<<"Case #"<<t<<": ";
		cin>>n>>m;
		for (int i = 0; i < n; i++)
		{
			for (int j = 0; j < m; j++)
			{
				cin>>l[i][j];
			}
		}
		for (int i = 0; i < n && possible; i++)
		{
			for (int j = 0; j < m && possible; j++)
			{
				possible = isPossible(i, j);
			}
		}
		cout<<(possible ? "YES" : "NO");
		cout<<endl;
	}
	return 0;
}

