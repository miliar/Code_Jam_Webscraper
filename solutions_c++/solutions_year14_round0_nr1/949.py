#include <stdio.h>
#include <string.h>
#include <math.h>
#include <cstdio>
#include <stdlib.h>
#include <iostream>
#include <string>
#include <vector>
#include <map>
#include <queue>
#include <set>
#include <algorithm>
#include <time.h>
using namespace std;


int main ()
{
	int arr[2][5][5];
	int ans[2];
	int t;

	freopen ("A-small.in", "r", stdin);
	freopen ("A-small.out", "w", stdout);

	scanf ("%d", &t);

	for (int c=1;c<=t;c++)
	{
		printf ("Case #%d: ", c);
		for (int i=0;i<2;i++)
		{
			scanf ("%d", &ans[i]);
			for (int j=0;j<4;j++)
				for (int k=0;k<4;k++)
					scanf ("%d", &arr[i][j][k]);
		}
		vector <int> v;
		for (int i=1;i<=16;i++)
		{
			bool can = true;
			bool val[2] = {false};
			for (int j=0;j<2;j++)
			{
				int cr = ans[j] - 1;
				for (int k=0;k<4;k++)
					if (arr[j][cr][k] == i)
					{
						val[j] = true;
						break;
					}
			}
			if (val[0] && val[1])
				v.push_back(i);
		}
		if (v.size()==1)
			cout << v[0] << endl;
		else if (v.size()==0)
			cout << "Volunteer cheated!\n";
		else
			cout << "Bad magician!\n";
	}

	return 0;
}
