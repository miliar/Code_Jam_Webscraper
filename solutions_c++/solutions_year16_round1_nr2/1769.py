//be naame khodaa

#include <iostream>
#include <cmath>
#include <vector>
#include <queue>
#include <stack>
#include <map>
#include <string>
#include <cstdio>
#include <algorithm>
#include <set>
#include <cassert>
#include <iomanip>
typedef long long ll;

using namespace std;
typedef pair <int, int> pii;

int cnt[5005];

int main()
{
	ios_base::sync_with_stdio(false);
	int t;
	cin >> t;
	for (int it = 1; it <= t; it++)
	{
		int n, x;
		cin >> n;
		for (int i = 0; i < 2*n-1; i++)
			for (int j = 0; j < n; j++)
				cin >> x, cnt[x]++;
		cout << "Case #" << it << ":";
		int ii = 0;
		for (int i = 1; i <= 2500; i++)
		{
			if (cnt[i]%2)
			{
				cout << ' ' << i;
				ii++;
			}
			cnt[i] = 0;
		}
		cout << endl;
		assert(ii == n);
	}
	return 0;
}
