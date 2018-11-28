#include <iostream>
#include <algorithm>
#include <string>
#include <vector>
#include <cstring>
using namespace std;

int main()
{
	int t;
	cin >> t;
	
	for (int tt = 1; tt <= t; ++tt)
	{
		int i, j, n, m, w;
		vector<int>	v;
	
		cin >> n >> w;
		for (i = 0; i < n; ++i)
		{
			cin >> j;
			v.push_back(j);
		}
	
		sort(v.begin(), v.end());
		i = 0;
		j = v.size() - 1;
		m = 0;
		while (i < j)
		{
			if (v[i] + v[j] <= w)
			{
				i++;
				j--;
				m++;
			}
			else
			{
				j--;
				m++;
			}
		}
		if (i == j)
			m++;
	
		cout << "Case #" << tt << ": " << m << endl;
	}

	return 0;
}
