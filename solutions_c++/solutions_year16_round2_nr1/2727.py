#include <iostream>
#include <string>
#include <algorithm>
#include <vector>

using namespace std;

#define l(c) c-65

int main()
{
	int t, T;
	int i, j;
	char c;

	freopen("input.txt", "rb", stdin);
	freopen("output.txt", "w", stdout);

	cin >> T;
	c = getc(stdin);
	for (t = 1; t <= T; t++)
	{
		vector<int> lt(26, 0);
		vector<int> d(10, 0);

		while (1)
		{
			c = getc(stdin);
			if (c == 13 | c == 10 || c <= 0) break;
			lt[c - 65]++;
		}

		d[0] = lt[l('Z')];
		d[2] = lt[l('W')];
		d[4] = lt[l('U')];
		d[6] = lt[l('X')];
		d[8] = lt[l('G')];

		d[3] = lt[l('H')] - d[8];
		d[7] = lt[l('S')] - d[6];

		d[5] = lt[l('V')] - d[7];
		
		d[9] = lt[l('I')] - d[8] - d[6] - d[5];
		
		d[1] = lt[l('N')] - d[7] - 2*d[9];

		cout << "Case #" << t << ": ";
		for (i = 0; i < 10; i++)
			for (j = 0; j < d[i]; j++)
				cout << i;
		cout << endl;
	}

	return 0;
}