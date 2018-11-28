#include<iostream>
#include<string>
#include<vector>
#include<stack>
#include<queue>
#include<map>
#include<algorithm>
using namespace std;
bool max_row(int a[101][101],int x,int y,int rows)
{
	int ele = a[x][y];
	int maxi = ele;
	for(int i = 0; i < rows;i++)
		maxi = max(maxi,a[i][y]);
	return ele==maxi;
}
bool max_column(int a[101][101],int x,int y,int cols)
{
	int ele = a[x][y];
	int maxi = ele;
	for(int i = 0 ;i < cols;i++)
		maxi = max(maxi,a[x][i]);
	return ele==maxi;
}
int main()
{
	int t;
	cin >> t;
	for(int tc = 1; tc <= t;tc++)
	{
		int n,m;
		int a[101][101];
		cin >> n >> m;
		int flag = 0;
		for(int i = 0; i < n;i++)
		{
			for(int j = 0;j < m;j++)
			{
				cin >> a[i][j];
			}
		}
		for(int i = 0; i < n;i++)
		{
			for(int j = 0; j < m;j++)
			{
				if(!max_row(a,i,j,n) && !max_column(a,i,j,m))
				{
					flag = 1;
					break;
				}
			}
			if(flag)
				break;
		}
		cout << "Case #" << tc << ": ";
		if(flag)
			cout << "NO";
		else
			cout << "YES";
		cout << endl;
	}
}
