#include <bits/stdc++.h>
using namespace std;
#define int long long

int rows, cols, dx[] = {0, 1, 0, -1}, dy[] = {1, 0, -1, 0};

bool isIn(int x, int y)	{
	if(x >= 0 and x < rows and y >= 0 and y < cols)	{
		return true;
	}
	return false;
}

string grid[110];

void pre()	{

}

void pain()	{
	cin >> rows >> cols;
	for(int i=0; i<rows; i++)	{
		cin >> grid[i];
	}
	bool there = false;
	int ans = 0;
	for(int i=0; i<rows; i++)	{
		for(int j=0; j<cols; j++)	{
			if(grid[i][j] != '.')	{
				there = true;
				int cnt1 = 0, cnt2 = 0;
				for(int k=0; k<cols; k++)	{
					cnt1 += (grid[i][k] != '.');
				}
				for(int k=0; k<rows; k++)	{
					cnt2 += (grid[k][j] != '.');
				}
				if(cnt1 == 1 and cnt2 == 1)	{
					cout << "IMPOSSIBLE\n";
					return;
				}
				if(grid[i][j] == '>')	{
					bool ok = true;
					for(int k=j+1; k<cols; k++)	{
						if(grid[i][k] != '.')	{
							ok = false;
						}
					}
					ans += ok;
				}
				if(grid[i][j] == '<')	{
					bool ok = true;
					for(int k=0; k<j; k++)	{
						if(grid[i][k] != '.')	{
							ok = false;
						}
					}
					ans += ok;
				}
				if(grid[i][j] == '^')	{
					bool ok = true;
					for(int k=0; k<i; k++)	{
						if(grid[k][j] != '.')	{
							ok = false;
						}
					}
					ans += ok;
				}
				if(grid[i][j] == 'v')	{
					bool ok = true;
					for(int k=i+1; k<rows; k++)	{
						if(grid[k][j] != '.')	{
							ok = false;
						}
					}
					ans += ok;
				}
			}
		}
	}
	cout << ans << "\n";
}

#undef int
int main()	{
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	string input = "1ain.txt";
	string output = "1aout.txt";
	freopen(input.c_str(), "r", stdin);
	freopen(output.c_str(), "w", stdout);
	int tt; cin >> tt;
	pre();
	for(int iii=1; iii<=tt; iii++)	{
		cout << "Case #" << iii << ": ";
		pain();
	}
}

