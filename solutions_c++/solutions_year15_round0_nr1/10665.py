#include <iostream>
#include <cmath>
#include <cstring>
#include <vector>
#include <set>
#include <map>
#include <iomanip>
#include <algorithm>
#include <stack>
#include <queue>
#include <deque>
#include <cstdio>
#include <string>

using namespace std;

void Solve()
{
	int n, sum = 0, ans = 0;
	cin >> n;
	for (int i = 0; i <= n; ++i)
	{
		char c;
		cin >> c;
		int m = c - '0';
		if (i > sum && m != 0)
		{
			ans += i - sum;
			sum += ans;
		}
		sum += m;
	}
	cout << ans << endl;
	return;
}	

int main()
{
	int T;
	cin >> T;
	for (int i = 1; i <= T; ++i)
	{
		cout << "Case #" << i << ": ";
		Solve();
	}

	return 0;
}
