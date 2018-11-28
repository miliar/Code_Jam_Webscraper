// GCJ.cpp : Defines the entry point for the console application.
//
#include <cstdio>
#include <iostream>
#include <vector>
#include <list>
#include <map>
#include <string>
#include <math.h>
#include <functional>

//#define verbose

using namespace std;

int main()
{
	// First let's read the file
	freopen("gcj.in", "r", stdin);
	freopen("gcj.out", "w", stdout);

	int i, j, k, l, p, q, Ncases;

	cin >> Ncases;

	for (i = 1; i <= Ncases; i++)
	{
		int n, z=0, m=0;
		cin >> n;
		vector<int> allHts;
		int arr[100][50];
		int res[50];
		// init
		for (j = 0; j < 100; j++)
		{
			for (k = 0; k < 50; k++)
			{
				arr[j][k] = -1;
			}
		}
		for (k = 0; k < 50; k++)
		{
			res[k] = -1;
		}

		// read in
		for (j = 0; j < (2*n)-1; j++)
		{
			for (k = 0; k < n; k++)
			{
				cin >> arr[j][k];
			}
		}

		// look for odds
		for (j = 0; j < 100; j++)
		{
			for (k = 0; k < 50; k++)
			{
				int tmp = arr[j][k];
				if (tmp == -1)
					continue;
				bool already = false;
				for (q = 0; q < 50; q++)
				{
					if (res[q] == -1)
						break;
					else if (res[q] == tmp)
					{
						already = true;
						break;
					}
				}
				if (already)
					continue;
				int count = 0;
				for (l = 0; l < 100; l++)
				{
					for (p = 0; p < 50; p++)
					{
						if (arr[l][p] == -1)
							continue;
						if (arr[l][p] == tmp)
							count++;
					}
				}
				if (count % 2 != 0)
				{
					res[m++] = tmp;
				}
			}
		}

		cout << "Case #" << i << ": ";
		for (l = 0; l < m; l++)
		{
			int low = res[l];
			int lastK = l;
			for (k = 0; k < m; k++)
			{
				if (res[k] < low)
				{
					low = res[k];
					lastK = k;
				}
			}
			res[lastK] = 2501;	// magic height limit
			cout << low << " ";
		}

		cout << endl;
	}

	return 0;
}

