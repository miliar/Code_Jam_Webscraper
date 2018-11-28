#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <cmath>

using namespace std;

int a[4], b[4];

void input()
{
	int c, d, i, n, e;
	cin >> c;
	for (i = 1; i < c; i++)
		for (n = 0; n < 4; n++)
			cin >> e;
	for (n = 0; n < 4; n++)
		cin >> a[n];
	for (; i < 4; i++)
		for (n = 0; n < 4; n++)
			cin >> e;
	
	cin >> d;
	for (i = 1; i < d; i++)
		for (n = 0; n < 4; n++)
			cin >> e;
	for (n = 0; n < 4; n++)
		cin >> b[n];
	for (; i < 4; i++)
		for (n = 0; n < 4; n++)
			cin >> e;
}

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int count, x;
	int n1, n2, c = 0, out;
	cin >> x;
	for (count = x; count > 0; count--)
	{
		input();
		for (n1 = 0, c = 0; n1 < 4; n1++)
			for (n2 = 0; n2 < 4; n2++)
				if (a[n1] == b[n2])
				{
					out = a[n1];
					c++;
				}
		switch (c)
		{
		case 0:
			cout << "Case #" <<  x - count +1 << ": Volunteer cheated!" << endl;
			break;
		case 1:
			cout << "Case #" << x - count +1 << ": " << out << endl;
			break;
		default:
			cout << "Case #" << x - count +1 << ": Bad magician!" << endl;
			break;
		}
	}
	return 0;
}