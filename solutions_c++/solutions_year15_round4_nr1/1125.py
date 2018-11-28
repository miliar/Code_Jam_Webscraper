#include <bits/stdc++.h>

#define F first
#define S second
#define pb push_back
#define INF (1 << 30)
#define SQR(a) ((a) * (a))

using namespace std;

const int N = 1111;

int dx[] = {1, -1, 0, 0};
int dy[] = {0, 0, 1, -1};

char a[N][N];
int ra[N], ca[N];
int r, c;

bool check(int x, int  y)
{
	int dir = 0;
	if (a[x][y] == '^')
		dir = 1;
	else if (a[x][y] == 'v')
		dir = 0;
	else if (a[x][y] == '>')
		dir = 2;
	else if (a[x][y] == '<')
		dir = 3;
	else
		return false;

	x += dx[dir];
	y += dy[dir];

	while (x >= 0 && y >= 0 && x < r && y < c && a[x][y] == '.')
	{
		x += dx[dir];
		y += dy[dir];
	}

	return !(x >= 0 && y >= 0 && x < r && y < c);
}

int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("output.txt", "w", stdout);

	int tst;
	cin >> tst;

	for (int t = 1; t <= tst; t++)
	{
		cin >> r >> c;	
		fill(ra, ra + N, 0);
		fill(ca, ca + N, 0);
	
		for (int i = 0; i < r; i++)
		{
			for (int j = 0; j < c; j++)
			{
				cin >> a[i][j];
				if (a[i][j] != '.')
				{
					ra[i]++;
					ca[j]++;				
				}
			}
		}
		
		int ans = 0;
		bool flag = false;
		for (int i = 0; i < r; i++)
			for (int j = 0; j < c; j++)
			{
				ans += check(i, j);
				if (a[i][j] != '.' && ra[i] == 1 && ca[j] == 1)
					flag = true;
			}
		
		if (flag)
			printf("Case #%d: IMPOSSIBLE\n", t);
		else
			printf("Case #%d: %d\n", t, ans);
	}	

	return 0;
}
