# include <iostream>

using namespace std;

int p, q;

int a[8][8], b[8][8], used[32];

int main ()
{
	int i, j, br = 0, ans, k, t;
	cin >> t;
	for (k = 0; k < t; k ++)
	{
		br = ans = 0;
		cin >> p;
		for (i = 0; i < 4; i ++)
		for (j = 0; j < 4; j ++)
		cin >> a[i][j];
	
		cin >> q;
		for (i = 0; i < 4; i ++)
		for (j = 0; j < 4; j ++)
		cin >> b[i][j];
	
		for (i = 0; i < 4; i ++)
		{
			used[a[p - 1][i]] ++;
			used[b[q - 1][i]] ++;
		}
			
		for (i = 1; i <= 16; i ++)
		if (used[i] == 2)
		{
			br ++;
			ans = i;
		}
		cout << "Case #" << k + 1 << ": ";
		if (br == 0) cout << "Volunteer cheated!" << endl;
		else if (br == 1) cout << ans << endl;
		else cout << "Bad magician!" << endl;
		for (i = 0; i < 17; i ++)
		used[i] = 0;
	}
	return 0;
}

