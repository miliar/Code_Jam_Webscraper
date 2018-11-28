#include <iostream>
#include <cstring>
#include <cstdio>

using namespace std;

const int maxn(105);

int n,m, task ;
int a[maxn][maxn];
int row_max[maxn], col_max[maxn];

int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	cin >> task;
	for (int cases = 1; cases <= task; cases++)
	{
		cin >> n >> m;
		for (int i = 0; i < n; i++)
		for (int j = 0; j < m; j++)
		{
			cin >> a[i][j];
		}
		memset(row_max , 0 , sizeof(row_max));
		memset(col_max , 0 , sizeof(col_max));
		for (int i = 0; i < n; i++)
		for (int j = 0; j < m; j++)
		{
			row_max[i] = max(row_max[i] , a[i][j]);
			col_max[j] = max(col_max[j] , a[i][j]);
		}
		
		bool flag = true;
		for (int i = 0; i < n; i++)
		for (int j = 0; j < m; j++)
		{
			if (a[i][j] < row_max[i] && a[i][j] < col_max[j])
				flag = false;
		}
		
		cout << "Case #" << cases << ": ";
		if (flag)
			cout << "YES" << endl;
		else
			cout << "NO" << endl;
	}
	return 0;
}