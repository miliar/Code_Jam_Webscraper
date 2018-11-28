#include<iostream>

using namespace std;

int a[105][105];
int ix[] = {0, -1, 0, 0, 1}, iy[] = {0, 0, -1, 1, 0};

int main()
{
	int t;
	cin >> t;
	for(int tt = 1; tt <= t; tt++)
	{
		int n, m;
		cin >> n >> m;
		int r[105] = {}, c[105] = {};
		for(int i = 0; i < n; i++)
		{
			string s;
			cin >> s;
			for(int j = 0; j < m; j++)
			{
				r[i]++, c[j]++;
				if(s[j] == '<')
					a[i][j] = 1;
				else if(s[j] == '>')
					a[i][j] = 4;
				else if(s[j] == '^')
					a[i][j] = 2;
				else if(s[j] == 'v')
					a[i][j] = 3;
				else
				{
					a[i][j] = 0;
					r[i]--, c[j]--;
				}
			}
		}
		int ans = 0;
		cout << "Case #" << tt << ": ";
		bool imp = false;
		for(int i = 0; i < n; i++)
			for(int j = 0; j < m; j++)
			{
				int y = i, x = j;
				bool flag = false;
				if(a[i][j] == 0)
					continue;
				for(; x >= 0 && y >= 0 && x < m && y < n; x += ix[a[i][j]], y += iy[a[i][j]])
				{
					if(!(y == i && j == x) && a[y][x])
					{
						flag = true;
						break;
					}
				}
				if(!flag)
				{
					if(r[i] > 1 || c[j] > 1)
						ans++;
					else if(!imp)
					{
						imp = true;
						cout << "IMPOSSIBLE" << endl;
					}
				}
			}
		if(!imp)
			cout << ans << endl;
	}
	return 0;
}	
