#include <algorithm>
#include <bitset>
#include <cassert>
#include <climits>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <deque>
#include <fstream>
#include <functional>
#include <iostream>
#include <limits>
#include <list>
#include <map>
#include <numeric>
#include <queue>
#include <random>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <tuple>
#include <vector>
#include <unordered_map>
#include <unordered_set>
#include <utility>

using namespace std;

int main()
{
	unsigned T;
	cin >> T;
	for (unsigned it = 0; it < T; ++it)
	{
		cout << "Case #" << it + 1 << ": ";
		unsigned N, K;
		cin >> N >> K;
		vector<double> vp(N);
		for (unsigned i = 0; i < N; ++i)
		{
			cin >> vp[i];
		}
		vector<vector<double>> vvp((1 << N), vector<double>(N + 1, 0.0));
		vvp[0][0] = 1.0;
		for (unsigned i = 1; i < (1u << N); ++i)
		{
			for (unsigned j = 0; j < N; ++j)
			{
				if (i & (1 << j))
				{
					unsigned ip = i ^ (1 << j);
					vvp[i][0] = vvp[ip][0] * (1 - vp[j]);
					for (unsigned k = 1; k <= N; ++k)
					{
						vvp[i][k] = vvp[ip][k - 1] * vp[j] + vvp[ip][k] * (1 - vp[j]);
					}
					break;
				}
			}
		}
		double maxp = 0;
		for (unsigned i = 1; i < (1u << N); ++i)
		{
			unsigned k = 0;
			for (unsigned x = i; x; x /= 2) k += (x & 1);
			if (k == K)
			{
				maxp = max(maxp, vvp[i][K / 2]);
			}
		}
		cout << maxp << endl;
	}
	return 0;
}
