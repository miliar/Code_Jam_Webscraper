#include <cstdio>
#include <math.h>
#include <iostream>
#include <vector>
#include <string>
#include <bitset>
#include <cassert>
#include <tuple>
#include <map>
#include <algorithm>
#include <set>

using namespace std;

void GetArrangement(map<int, set<int>>& arr)
{
	for (int i = 1; i <= 4; i++)
	{
		for (int j = 1; j <= 4; j++)
		{
			int c;
			cin >> c;
			arr[i].insert(c);
		}
	}
}


int main(int argc, char *argv[])
{
	int T;
	cin >> T;

	for (int i = 1; i <= T; i++)
	{
		int a1, a2;
		map<int, set<int>> arr1, arr2;
		cin >> a1;
		GetArrangement(arr1);
		cin >> a2;
		GetArrangement(arr2);

		vector<int> v(4);
		vector<int>::iterator it = set_intersection(arr1[a1].begin(), arr1[a1].end(), arr2[a2].begin(), arr2[a2].end(), v.begin());
		v.resize(it-v.begin());

		cout << "Case #" << i << ": ";
		switch (v.size())
		{
		case 0:
			cout << "Volunteer cheated!";
			break;
		case 1:
			cout << v[0];
			break;
		default:
			cout << "Bad magician!";
			break;
		} 
		cout << endl;
	}
}
