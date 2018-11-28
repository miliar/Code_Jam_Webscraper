#include <iostream>
#include <fstream>
#include <cstdio>
#include <climits>
#include <vector>
#include <map>
#include <list>
#include <deque>
#include <stack>
#include <set>
#include <string>
#include <cstring>
#include <algorithm>
#include <bitset>
#include <cmath>

using namespace std;

#define ll long long
#define vt vector

int main()
{
	freopen("output.txt", "w", stdout);
	freopen("A-small-attempt0.in", "r", stdin);
	int t;
	cin >> t;
	for(int cases = 1; cases <= t; cases ++)
	{
		vt<int> ans(17, 0);
		for(int runme = 0; runme < 2; runme++)
		{
			int r, temp;
			cin >> r;
			for(int i = 1; i <= 4; i++)
				for(int j = 0; j < 4; j++)
				{
					cin >> temp;
					if (i == r)
						ans[temp]++;
				}
		}
		vt<int> output;
		for(int i = 1; i <= 16; i++)
			if (ans[i] == 2)
				output.push_back(i);
		if (output.size() > 1)
			cout << "Case #" << cases << ": " << "Bad magician!" << endl;
		else if (output.size() == 0)
			cout << "Case #" << cases << ": " << "Volunteer cheated!" << endl;
		else
			cout << "Case #" << cases << ": " << output[0] << endl;

	}
	return 0;
}