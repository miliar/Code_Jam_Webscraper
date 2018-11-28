#include <iostream>
#include <vector>
using namespace std;

int a[128][128];

int main()
{
	//freopen("input.in", "r", stdin);
	//freopen("output.txt", "w", stdout);
	int T;
	cin >> T;
	for(int test = 1; test <= T; test++)
	{
		int n, m;
		cin >> n >> m;
		for(int i = 0; i < n; i++)
			for(int j = 0; j < m; j++)
				cin >> a[i][j];

		bool okr, okc;
		bool res = true;
		for(int i = 0; i < n; i++)
		{
			for(int j = 0; j < m; j++)
			{
				okr = true, okc = true;
				int cur = a[i][j];
				for(int k = 0; k < m; k++)
				{
					if(a[i][k] > cur)
					{
						okr = false;
						break;
					}
				}
				for(int k = 0; k < n; k++)
				{
					if(a[k][j] > cur)
					{
						okc = false;
						break;
					}
				}
				if(!okc && !okr)
				{
					res = false;
					break;
				}
			}
		}
		cout << "Case #" << test << ": ";
		if(res) cout << "YES" << endl;
		else cout << "NO" << endl;
	}
	return 0;
}