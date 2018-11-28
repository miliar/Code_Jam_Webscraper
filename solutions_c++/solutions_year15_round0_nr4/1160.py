#include <iostream>
#include <cstring>
#include <cstdio>
#include <string>
#include <ctime>
#include <vector>
#include <algorithm>
#include <ctime>
#include <set>
#include <map>
using namespace std;

int main()
{
	//D-small-attempt0.in
	freopen("D-small-attempt1.in", "r", stdin);
	freopen("out.txt", "w", stdout);
	int T, index = 1;
	cin >> T;
	while (T--)
	{
		int X, R, C;
		cin >> X >> R >> C;
		if (X == 1)
		{
			cout << "Case #" << index++ << ": GABRIEL" << endl;
		}
		else if (X == 2)
		{
			if ((R*C) % X == 0)
			{
				cout << "Case #" << index++ << ": GABRIEL" << endl;
			}
			else
			{
				cout << "Case #" << index++ << ": RICHARD" << endl;
			}
		}
		else if (X == 3)
		{
			if ((R*C) % X == 0)
			{
				if (R == 1 || C == 1)
				{
					cout << "Case #" << index++ << ": RICHARD" << endl;
				}
				else
				{
					cout << "Case #" << index++ << ": GABRIEL" << endl;
				}
			}
			else
			{
				cout << "Case #" << index++ << ": RICHARD" << endl;
			}
		}
		else
		{
			if ((R*C) % X == 0)
			{
				if (R == 1 || C == 1 || R==2 || C==2)
				{
					cout << "Case #" << index++ << ": RICHARD" << endl;
				}
				else
				{
					if (R*C == 8)cout << "Case #" << index++ << ": RICHARD" << endl;
					else if (R*C == 12)cout << "Case #" << index++ << ": GABRIEL" << endl;
					else cout << "Case #" << index++ << ": GABRIEL" << endl;
				}
			}
			else
			{
				cout << "Case #" << index++ << ": RICHARD" << endl;
			}
		}
	}
	return 0;
}