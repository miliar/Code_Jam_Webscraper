#include <iostream>
#include <fstream>
#include <cstdio>
#include <cmath>
#include <climits>
#include <vector>
#include <stack>
#include <list>
#include <deque>
#include <queue>
#include <map>
#include <bitset>
#include <string>
#include <sstream>
#include <algorithm>

using namespace std;

#define vt vector
#define ll long long

int main()
{
	freopen("B-small-attempt1.in", "r", stdin);
	freopen("output.txt", "w", stdout);
	int t;
	cin >> t;
	for(int cases = 1; cases <= t; cases++)
	{
		int x, y, z;
		cin >> x >> y >> z;
		int count = 0;
		for(int i = 0; i < x; i++)
			for(int j = 0; j < y; j++)
				if ((i&j) < z)
					count++;
		cout << "Case #" << cases << ": " << count << endl;
	}
	return 0;
}