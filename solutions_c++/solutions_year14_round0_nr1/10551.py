#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <cmath>
#include <string>
#include <sstream>
#include <algorithm>
#include <iomanip>
#include <cmath>
#include <cstring>
#include <math.h>
#include <vector>
#include <fstream>
#include <stack>
using namespace std;
#define READ(s) freopen(s, "r", stdin)
#define WRITE(s) freopen(s, "w", stdout)
typedef pair<int, int> pii;
int main()
{
	READ("A-small-attempt0.in");
	WRITE("A-small-attempt0.out");
	int t;
	cin >> t;
	int *cases  = new int[t];
	int arr1[4][4], arr2[4];
	int g;
	for (int z = 0; z < t; z++)
	{
		cin >> g;
		for (int i = 0; i < 4; i++)
		for (int j = 0; j < 4; j++)
			cin >> arr1[i][j];

		for (int i = 0; i < 4; i++)
			arr2[i] = arr1[g - 1][i];

		cin >> g;
		for (int i = 0; i < 4; i++)
		for (int j = 0; j < 4; j++)
			cin >> arr1[i][j];

		int ans, count = 0;
		for (int i = 0; i < 4; i++)
		for (int j = 0; j < 4; j++)
		if (arr1[g - 1][i] == arr2[j])
		{
			ans = arr2[j];
			count++;
		}
		if (count > 1)
			cases[z] = -1;
		else if (count < 1)
			cases[z] = 0;
		else
			cases[z] = ans;

	}
	for (int i = 0; i < t; i++)
	{
		cout << "Case #" << i + 1 << ": ";
		if (cases[i] == -1)
			cout << "Bad magician!";
		else if (cases[i] == 0)
			cout << "Volunteer cheated!";
		else
			cout << cases[i];
		cout << endl;
	}
	return 0;
}