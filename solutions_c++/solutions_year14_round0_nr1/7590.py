#include <iostream>
#include <algorithm>
#include <string>
#include <utility>
#include <cstdio>
#include <vector>
#include <cmath>
#include <ctime>
#include <queue>
#include <map>

typedef long long LL;

using namespace std;


int main ()
{
    freopen ("input.txt", "r", stdin);
    freopen ("output.txt", "w", stdout);
    int t;
    cin >> t;
    int m;
    int d;
    int ans1, ans2;
    int arr1[4][4];
    int arr2[4][4];
    for (int i = 0;i < t;i++)
	{
		m = 0;
		cout << "Case #" << i + 1 << ": ";
		cin >> ans1;
		for (int j = 0;j < 4;j++)
		{
			for (int k = 0;k < 4;k++)
			{
				cin >> arr1[j][k];
			}
		}
		cin >> ans2;
		for (int j = 0;j < 4;j++)
		{
			for (int k = 0;k < 4;k++)
			{
				cin >> arr2[j][k];
			}
		}
		for (int j = 0;j < 4;j++)
		{
			for (int k = 0;k < 4;k++)
			{
				if (arr1[ans1 - 1][j] == arr2[ans2 - 1][k])
				{
					m++;
					d = arr1[ans1 - 1][j];
				}
			}
		}
		if (m == 1)
		{
			cout << d << endl;
		}
		else if (m == 0)
		{
			cout << "Volunteer cheated!" << endl;
		}
		else
		{
			cout << "Bad magician!" << endl;
		}
	}
    return 0;
}
