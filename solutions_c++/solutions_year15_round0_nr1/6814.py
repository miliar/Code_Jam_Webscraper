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

#define FILE_NAME "A-large"

using namespace std;

int main()
{
	freopen(FILE_NAME ".in", "r", stdin);
	freopen(FILE_NAME ".out", "w", stdout);

	int numTestCaces = 0;
	cin >> numTestCaces;
	for (int Case = 1; Case <= numTestCaces; ++Case)
	{
		int smax;
		cin >> smax;
		int res = 0;
		int sum = 0;
		for (int i = 0; i <= smax; ++i)
		{
			char c;
			cin >> c;
			if (c - '0' > 0)
			if (sum < i)
			{
				res += i - sum;
				sum = i;
			}
			sum += c - '0';
		}
		cout << "Case #" << Case << ": ";
		cout << res << endl;
	}

	return 0;
}
