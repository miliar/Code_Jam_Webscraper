// GoogleCodeJam.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
#include <cstring>
using namespace std;


int _tmain(int argc, _TCHAR* argv[])
{
	int t;
	cin >> t;

	for (int i = 1; i <= t; i++)
	{
		int n;
		cin >> n;

		int k = 0;
		int done[10];
		memset(done, 0, sizeof(done));
		int cnt = 0;
		cout << "Case #" << i << ": ";
		bool found = false;
		for (int j = 1; j <= 100; j++)
		{
			k = k + n;
			int r = k;
			while (true)
			{
				int dig = r % 10;
				if (r < 10)
				{
					if (done[dig] == 0)
					{
						done[dig] = 1;
						cnt++;
					}
					break;
				}
				if (done[dig] == 0)
				{
					done[dig] = 1;
					cnt++;
				}
				r /= 10;
			}
			if (cnt == 10)
			{
				cout << k << "\n";
				found = true;
				break;
			}
		}
		if (!found)
		{
			cout << "INSOMNIA\n";
		}
	}
	return 0;
}

