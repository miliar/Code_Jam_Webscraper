// D-Small.cpp : main project file.

//#include "stdafx.h"
#include <stdio.h>
#include <vector>
#include <algorithm>
using namespace std;

vector<double> v1, v2;

int main()
{
	//freopen("in.txt", "rt", stdin);
	//freopen("out.txt", "wt", stdout);
	//freopen("inL.txt", "rt", stdin);
	//freopen("outL.txt", "wt", stdout);

	int t, n;
	scanf("%d", &t);
	for (int z = 1; z <= t; z++)
	{
		v1.clear();
		v2.clear();
		scanf("%d", &n);
		v1.resize(n);
		v2.resize(n);
		
		for (int i = 0; i < n; i++)
			scanf("%lf", &v1[i]);

		for (int i = 0; i < n; i++)
			scanf("%lf", &v2[i]);

		sort(v1.begin(), v1.end());
		sort(v2.begin(), v2.end());

		int nDW = 0, nW = 0;
		for (int i = n - 1, j = n - 1; i >= 0 && j >= 0; j--)
		{
			if (v1[i] > v2[j])
			{
				nDW++;
				i--;
			}
		}
		for (int i = n - 1, j = n - 1; i >= 0 && j >= 0; i--)
		{
			if (v2[j] > v1[i])
			{
				j--;
			}
			else if (v1[i] > v2[j])
			{
				nW++;
			}
		}
		printf("Case #%d: %d %d\n", z, nDW, nW);
	}
	return 0;
}
