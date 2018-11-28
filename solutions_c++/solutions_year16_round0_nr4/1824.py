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

typedef unsigned long long BigInt;

BigInt pow(BigInt a, BigInt b)
{
	BigInt res = 1;
	for (int i = 0; i < b; i++)
		res *= a;
	return res;
}

BigInt posFunc(BigInt i, BigInt C, BigInt K)
{
	if (C == 1)
		return min(2 * i, K);

	return posFunc(i, C - 1, K) + 2 * (i - 1) * pow(K, C - 1);
}

int main()
{
	ios::sync_with_stdio(false);

	int T;
	cin >> T;
	for (int t = 0; t < T; t++)
	{
		int K, C, S;
		cin >> K >> C >> S;

		if (C != 1)
		{
			if (S < (K + 1) / 2)
			{
				cout << "Case #" << t + 1 << ": IMPOSSIBLE" << endl;
				continue;
			}

			cout << "Case #" << t + 1 << ':';
			for (int i = 1; i <= (K + 1) / 2; i++)
				cout << ' ' << posFunc(i, C, K);
			cout << endl;
		}
		else
		{
			if (S < K)
			{
				cout << "Case #" << t + 1 << ": IMPOSSIBLE" << endl;
				continue;
			}

			cout << "Case #" << t + 1 << ':';
			for (int i = 1; i <= K; i++)
				cout << ' ' << i;
			cout << endl;
		}
	}

	return 0;
}
