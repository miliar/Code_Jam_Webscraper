#include<iostream>
#include<string>
#include<vector>
using namespace std;
int x, y;
int arr[110][110];
bool connectedWithedge(int a, int b, int n)
{
	int q = 0;
	for (int i = 0; i < x; i++)
	{
		if(arr[a][i] > n)
		{
			q++;
			break;
		}
	}
	for (int i = 0; i < y; i++)
	{
		if(arr[i][b] > n)
		{
			q++;
			break;
		}
	}
	return (q<=1);
}


int main()
{
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	string str;
	int t;
	cin >> t;
	for (int i = 0; i < t; i++)
	{
		cin >> y >> x;
		for (int j = 0; j < y; j++)
		{
			for (int k = 0; k < x; k++)
			{
				cin >> arr[j][k];
			}
		}
		bool  con = true;
		cout << "Case #" << i+1 << ": ";
		for (int k = 0; k < y; k++)
		{
			for (int j = 0; j < x; j++)
			{
				if(connectedWithedge(k, j, arr[k][j]) == false)
				{
					con = false;
					break;
				}
			}
			if(!con)
				break;
		}
		if(con)
			cout << "YES" << endl;
		else
			cout << "NO" << endl;
	}
}
