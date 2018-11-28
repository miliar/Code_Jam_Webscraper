#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

#define FILE_NAME "B-large"

using namespace std;

int main()
{
	freopen(FILE_NAME ".in", "r", stdin);
	freopen(FILE_NAME ".out", "w", stdout);
	
	int numTestCaces = 0;
	cin >> numTestCaces;
	for(int Case = 1; Case <= numTestCaces; ++Case)
	{
		int m, n;
		cin >> n >> m;
		vector<vector<int>> v(n, vector<int>(m));

		for(int i = 0; i < n; ++i)
		{
			for(int j = 0; j < m; ++j)
			{
				cin >> v[i][j];
			}
		}
		
		bool ok = true;
		//for(int h = 1; h <= 100; ++h)
		for(int i = 0; i < n && ok; ++i)
		{
			for(int j = 0; j < m && ok; ++j)
			{
				int c = v[i][j];
				//if(c == h)
				{
					bool r = true;
					for(int k = 0; k < n && r; ++k)
						if(c < v[k][j])
							r = false;
					if(!r)
					for(int k = 0; k < m && ok; ++k)
						if(c < v[i][k])
							ok = false;
				}
			}
		}

		cout << "Case #" << Case << ": ";
		if(ok)
			cout << "YES" << endl;
		else
			cout << "NO" << endl;
	}

	return 0;
}
