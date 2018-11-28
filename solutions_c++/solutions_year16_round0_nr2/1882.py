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
	cin.ignore();

	for (int t = 0; t < T; t++)
	{
		string line;
		getline(cin, line);

		long long count = 0;
		if (line.size() > 0)
		{
			char last = '+';
			for (int i = line.size() - 1; i >= 0; i--)
			{
				char c = line[i];
				if (c != last)
				{
					count++;
					last = c;
				}
			}
		}

		cout << "Case #" << t + 1 << ": " << count << endl;
	}

	return 0;
}
