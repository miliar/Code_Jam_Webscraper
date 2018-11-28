#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <stdio.h>
#include <math.h>
#include <map>
#include <set>
using namespace std;
int main()
{
	freopen("src.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	int t;
	cin >> t;
	for (int i = 0; i < t; i++)
	{
		int ans1, ans2;
		cin >> ans1;
		int data[4][4];
		int data2[4][4];

		for (int j = 0; j < 4; j++)
			for (int k = 0; k < 4; k++)
				cin >> data[j][k];

		cin >> ans2;
		for (int j = 0; j < 4; j++)
			for (int k = 0; k < 4; k++)
				cin >> data2[j][k];

		int count = 0;
		int TO;

		ans1--;
		ans2--;

		for (int j = 0; j < 4; j++)
			for (int k = 0; k < 4; k++)
				if (data[ans1][j] == data2[ans2][k])
				{
					count++;
					TO = data[ans1][j];
					data2[ans2][k] = -1;
				}
		cout << "Case #" << i +1 << ": ";

		if (count == 1)
			cout << TO << endl;
		else if (count > 1)
			cout << "Bad magician!" << endl;
		else cout << "Volunteer cheated!" << endl;
	}
	return 0;
}