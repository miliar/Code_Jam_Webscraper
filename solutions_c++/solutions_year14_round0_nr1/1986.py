#include <iostream>
#include <cstdlib>
#include <string>
#include <cmath>
#include <algorithm>
using namespace std;
typedef long long ll;
typedef unsigned long long ul;
long T, i, j, k, x, y;
long a[5][5], b[5][5],d[17];
int main()
{
	freopen("A-small-attempt0.in", "r", stdin);
	freopen("A.out", "w", stdout);
	cin >> T;
	for (i = 1; i <= T; i++)
	{
		cin >> x;
		cout << "Case #" << i << ": ";
		long res = 0;
		long ans;
		memset(d, 0, sizeof(d));
		for (j = 1; j <= 4; j++)
		{
			for (k = 1; k <= 4; k++)
			{
				cin >> a[j][k];
				if (j == x) d[a[j][k]]++;
			}
		}
		cin >> y;
		for (j = 1; j <= 4; j++)
		{
			for (k = 1; k <= 4; k++)
			{
				cin >> b[j][k];
				if (j == y) d[b[j][k]]++;
			}
		}
		for (j = 1; j <= 16; j++)
		{
			if (d[j] == 2)
			{
				res++;
				ans = j;
			}
		}
		if (res == 0) cout << "Volunteer cheated!"; 
		else if (res > 1) cout << "Bad magician!";
		else cout << ans;
		cout << endl;
	}
	//system("pause");
	return 0;
}
