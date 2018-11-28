#include <iostream>
#include <algorithm>
#include <vector>
#include <sstream>
#include <string>
#include <array>

using namespace std;

void connectAll(vector<vector<int>>& matr, int ind)
{
	for (int i = 0; i <= ind; ++i)
	{
		for (int j = 0; j < i; ++j)
		{
			matr[j][i] = 1;
		}
	}
}

void testcase()
{
	long long b, m;
	cin >> b >> m;

	vector<vector<int>> matr(b);
	for (int i = 0; i < b; ++i)
	{
		matr[i].resize(b, 0);
	}

	vector<int> vals;
	long long m1 = m;
	while (m1 > 0)
	{
		int c = m1 & 1;
		vals.push_back(c);
		m1 = m1 >> 1;
	}

	int mx = vals.size() - 1;

	if (vals[mx] != 1)
		throw "fliduhgilu";

	int bind = mx + 1;

	if (bind >= b)
	{
		cout << "IMPOSSIBLE" << endl;
		return;
	}
	
	connectAll(matr, bind);

	vals[mx] = 0;

	for (int i = bind + 1; i < b; ++i)
	{
		matr[i - 1][i] = 1;
	}

	bool flag = true;

	int curind = mx;
	while (vals.size() > 0)
	{
		if (vals.back() == 1)
		{
			if ( bind >= b - 1)
			{
				flag = false;
				break;
			}
			matr[curind + 1][b - 1] = 1;
		}
		vals.pop_back();
		curind--;
	}

	if (flag)
	{
		cout << "POSSIBLE" << endl;
		for (int i = 0; i < b; ++i)
		{
			for (int j = 0; j < b; ++j)
			{
				cout << matr[i][j];
			}
			cout << endl;
		}
	}
	else
	{
		cout << "IMPOSSIBLE" << endl;
		return;
	}
} 

int main()
{
  int n;
	cin >> n;
	
	for (int i = 0; i < n; i++)
	{
    cout << "Case #" << i + 1 << ": ";
		testcase();
	}
	
	return 0;
}