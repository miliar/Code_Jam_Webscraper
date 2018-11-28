#include <vector>
#include <iterator>
#include <list>
#include <map>
#include <math.h>
#include <cmath>
#include <set>
#include <queue>
#include <deque>
#include <string>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <string.h>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cstdlib>
#include <ctime>
#define pi 3.14159
#define inf 9e10
using namespace std;
int main()
{
	freopen("A-small-attempt1.in", "r", stdin);
	freopen("output.txt", "w", stdout);
	int test;
	cin >> test;
	for (int tc = 1; tc <= test; tc++)
	{
		vector <int> list1, diff;
		int arr[4][4];
		int row, ans;
		cin >> row;
		for (int i = 0; i < 4; i++)
		for (int j = 0; j < 4; j++)
			cin >> arr[i][j];
		for (int i = 0; i < 4; i++)	list1.push_back(arr[row-1][i]);
		cin >> row;
		for (int i = 0; i < 4; i++)
    		for (int j = 0; j < 4; j++)
			cin >> arr[i][j];
		for (int i = 0; i < 4; i++)
			for (int j = 0; j < 4; j++)
			if (list1[i] == arr[row-1][j]) diff.push_back(list1[i]);
		if (diff.size() > 1)
			cout << "Case #" << tc << ": Bad magician!" << endl;
		else if (diff.size() == 1)
			cout << "Case #" << tc << ": " << diff[0] << endl;
		else
			cout << "Case #" << tc << ": Volunteer cheated!" << endl;
	}
	return 0;
}