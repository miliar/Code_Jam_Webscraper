#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <algorithm>
#include <map>
#include <vector>
#include <list>
#include <queue>
#include <iostream>
#include <climits>
using namespace std;

typedef long long ll;
typedef long double ld;

#define SIZE 200

int board[SIZE][SIZE];
int row[SIZE];
int col[SIZE];
int t, m, n;
int main()
{
	int i, j, k;
	bool mark;
//	freopen("B-large.in", "r", stdin);
//	freopen("out", "w", stdout);
	cin >> t;
	for (i = 0; i < t; i++)
	{
		cin >> n >> m;
		memset(row, 0, sizeof(row));
		memset(col, 0, sizeof(col));
		mark = false;
		for (j = 0; j < n; j++)
		for (k = 0; k < m; k++)
		{	
			cin >> board[j][k];
			if (board[j][k] > row[j])
				row[j] = board[j][k];
			if (board[j][k] > col[k])
				col[k] = board[j][k];
		}
		printf("Case #%d: ", i+1);
		for (j = 0; j < n; j++)
		{
			
			for (k = 0; k < m; k++)
				if (board[j][k] != row[j] && board[j][k] != col[k])
				{
					mark = true;
					break;
				}
			if (mark)
				break;
		}
		if (mark)
			printf("NO\n");
		else
			printf("YES\n");	
	}
	return 0;
}
