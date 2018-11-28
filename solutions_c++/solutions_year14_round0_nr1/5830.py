#include <iostream>

using namespace std;
int a[4][4], b[4][4];
int main()
{
	int t, x, y, ans, ans1;
	cin >> t;
	for(int i = 1;i <= t;++i)
	{
		cin >> x;
		x--;
		ans = 0;
		for(int j = 0;j < 4;++j)
			for(int k = 0;k < 4;++k)
				cin >> a[j][k];
		cin >> y;
		y--;
		//cout << x << ' ' << y << endl;
		for(int j = 0;j < 4;++j)
			for(int k = 0;k < 4;++k)
				cin >> b[j][k];
		for(int j = 0;j < 4;++j)
			for(int k = 0;k < 4;++k)
			{
				//cout << a[x][j] << ' ' << b[y][k] << endl;
				if(a[x][j] == b[y][k])
				{
					ans++;
					ans1 = a[x][j];
				}
			}
		cout << "Case #" << i << ": ";
		if(ans == 1)
			cout << ans1 << endl;
		else if(ans == 0)
			cout << "Volunteer cheated!\n";
		else
			cout << "Bad magician!\n";
	}
	return 0;
}