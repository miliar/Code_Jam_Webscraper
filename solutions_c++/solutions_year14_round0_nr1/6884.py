#include <functional>
#include <algorithm>
#include <iostream>
#include <cstdlib>
#include <numeric>
#include <utility>
#include <sstream>
#include <iomanip>
#include <cstdio>
#include <vector>
#include <bitset>
#include <queue>
#include <deque>
#include <stack>
#include <cmath>
#include <ctime>
#include <list>
#include <map>
#include <set>

using namespace std;


int main()
{
#ifndef ONLINE_JUDGE
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
#endif

	int T;
	cin >> T;

	for(int t=0; t < T; ++t)
	{
		int r1,r2;
		vector<vector<int> > a1(4, vector<int>(4)), a2(4, vector<int>(4));

		cin >> r1;
		for(int i=0;i<4;++i)
			for(int j=0;j<4;++j)
				cin >> a1[i][j];

		cin >> r2;
		for(int i=0;i<4;++i)
			for(int j=0;j<4;++j)
				cin >> a2[i][j];


		int common = -1;

		for(int i = 0; i < 4; ++i)
		{
			for(int j = 0; j < 4; ++j)
			{
				if (a1[r1-1][i] == a2[r2-1][j])
				{
					if (common == -1)
						common = a1[r1-1][i];
					else
						common = -2;
				}
			}
		}

		if (common == -1)
		{
			cout << "Case #" << (t+1) << ": Volunteer cheated!\n";
		}
		else if (common == -2)
		{
			cout << "Case #" << (t+1) << ": Bad magician!\n";
		}
		else 
		{
			cout << "Case #" << (t+1) << ": " << common << "\n";
		}
	}


}