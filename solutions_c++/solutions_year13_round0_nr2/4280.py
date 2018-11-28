// Test.cpp : Defines the entry point for the console application.
//

#include <iostream>
#include <vector>

using namespace std;

bool calc (const vector<vector<int>> &a, int n, int m)
{
	for (int i = 0; i < n; ++i)
		for (int j = 0; j < m; ++j)
		{
			int h = a[i][j];
			int k = 0, t = 0;
			for (; k < m && a[i][k] <= h; ++k);
			for (; t < n && a[t][j] <= h; ++t);
			if (k < m && t < n)
				return false;
		}

	return true;
}
			
int main()
{
	int numCases = 0;
	cin >> numCases;

	for (int c = 0; c < numCases; ++c) 
	{
		int n, m;
		cin >> n >> m;
		vector<vector<int>> a(n);

		for (int i = 0; i < n; ++i)
		{
			a[i].resize(m);
			for (int j = 0; j < m; ++j)
				cin >> a[i][j];
		}

		bool res = calc(a, n, m);

		cout << "Case #" << c+1 << ": " << (res ? "YES" : "NO") << endl;
	}
		
	return 0;
}
