#include <algorithm>
#include <array>
#include <chrono>
#include <climits>
#include <cmath>
#include <cstdlib>
#include <deque>
#include <forward_list>
#include <functional>
#include <iostream>
#include <iterator>
#include <limits>
#include <list>
#include <locale>
#include <map>
#include <numeric>
#include <queue>
#include <random>
#include <regex>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <unordered_map>
#include <unordered_set>
#include <utility>
#include <valarray>
#include <vector>

using namespace std;

int main()
{
	ios::sync_with_stdio(false);

	int T;
	cin >> T;

	for (int t = 0; t < T; t++)
	{
		long long N;
		cin >> N;

		if (N == 0)
		{
			cout << "Case #" << t + 1 << ": INSOMNIA" << endl;
			continue;
		}

		unordered_set<int> digits;
		for (int k = 0; k < 10; k++)
			digits.insert(k);

		long long last = N;
		while (true)
		{
			{
				long long v = last;
				while (true)
				{
					if (v == 0)
					{
						digits.erase(0);
						break;
					}
					long long rem = v % 10;
					v /= 10;
					digits.erase(rem);
					if (v == 0)
						break;
				}
			}
			if (!digits.empty())
				last += N;
			else
				break;
		}
		cout << "Case #" << t + 1 << ": " << last << endl;
	}

	return 0;
}
