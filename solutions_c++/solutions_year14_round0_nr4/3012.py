#define _CRT_SECURE_NO_WARNINGS

#include <iostream>
#include <stdio.h>
#include <algorithm>

using namespace std;

int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt", "w", stdout);
	double a1[2000];
	double a2[2000];
	bool f1[2000];
	bool f2[2000];
	char* format = "Case #%d: %d %d\n";

	int t;
	cin >> t;
	for (int k = 0; k < t; k++)
	{
		int n;
		cin >> n;
		for (int i = 0; i < n; i++)
		{
			cin >> a1[i];
		}
		for (int i = 0; i < n; i++)
		{
			cin >> a2[i];
		}

		sort(a1, a1 + n);
		sort(a2, a2 + n);

		for (int i = 0; i < n; i++)
		{
			f1[i] = f2[i] = false;
		}
		int p1 = 0, p2 = 0;

		//war
		for (int i = 0; i < n; i++)
		{
			//get naomi
			f1[i] = true;
			bool isFound = false;
			for (int j = 0; j < n; j++)
			{
				if (a2[j] > a1[i] && !f2[j])
				{
					//get ken
					f2[j] = true;
					isFound = true;
					break;
				}
			}

			if (!isFound)
			{
				p2++;
				for (int j = 0; j < n; j++)
				{
					if (!f2[j])
					{
						//get ken
						f2[j] = true;
						break;
					}
				}
			}
		}

		for (int i = 0; i < n; i++)
		{
			f1[i] = f2[i] = false;
		}
		//fake war
		for (int i = 0; i < n; i++)
		{
			//get naomi
			f1[i] = true;

			bool isFound = false;
			for (int j = 0; j < n; j++)
			{
				if (a1[i] > a2[j] && !f2[j])
				{
					f2[j] = true;
					isFound = true;
					break;
				}
			}

			if (!isFound)
			{
				for (int j = n - 1; j >= 0; j--)
				{
					if (!f2[j])
					{
						f2[j] = true;
						break;
					}
				}
			}
			else
			{
				p1++;
			}
		}
		printf(format, k + 1, p1,p2);
	}
	return 0;
}