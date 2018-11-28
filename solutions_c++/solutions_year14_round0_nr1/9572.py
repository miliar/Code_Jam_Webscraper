#include <iostream>
#include <string.h>
#include <set>
#include <stdio.h>
#include <algorithm>
using namespace std;
int main()
{
	freopen("A.in","r",stdin);
	freopen("A.out", "w", stdout);
	int t;
	cin >> t;
	for (int i = 0; i < t; i++)
	{
		int x, y;
		int f[16];
		memset(f, 0, sizeof(f));
		cin >> x;
		for (int j = 0; j < 4; j++)
		{
			for (int k = 0; k < 4; k++)
			{
				cin >> y;
				if (j == x - 1) f[y - 1]++;
			}
		}
		cin >> x;
		for (int j = 0; j < 4; j++)
		{
			for (int k = 0; k < 4; k++)
			{
				cin >> y;
				if (j == x - 1) f[y - 1]++;
			}
		}
		int two = 0,ret;
		for (int j = 0; j < 16; j++)
		{
			if (f[j] == 2)
			{
				ret = j + 1;
				two++;
			}
		}
		cout << "Case #"<<i+1<<": ";
		if (two == 0) cout << "Volunteer cheated!";
		else if (two == 1) cout << ret;
		else cout << "Bad magician!";
		cout<<endl;
	}
	return 0;
}

