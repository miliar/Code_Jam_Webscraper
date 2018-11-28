#include<algorithm>
#include<cctype>
#include<cinttypes>
#include<climits>
#include<cmath>
#include<complex>
#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<ctime>
#include<deque>
#include<fstream>
#include<functional>
#include<iostream>
#include<list>
#include<map>
#include<numeric>
#include<queue>
#include<set>
#include<string>
#include<utility>
#include<vector>
#include<memory>
#include<array>

using namespace std;

int main()
{
	size_t T; cin >> T;

	std::vector<std::string> NUMS = { "ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE" };

	for (size_t t = 0; t < T; ++t)
	{
		std::string v; cin >> v;
		map<char, size_t> vs;
		for (size_t i = 0; i < v.length(); ++i)
		{
			++vs[v.at(i)];
		}

		size_t r[10];
		r[0] = vs['Z'];
		r[6] = vs['X'];
		r[2] = vs['W'];
		r[4] = vs['U'];
		r[8] = vs['G'];
		r[5] = vs['F'] - r[4];
		r[7] = vs['V'] - r[5];
		r[9] = vs['I'] - r[5] - r[6] - r[8];
		r[3] = vs['T'] - r[2] - r[8];
		r[1] = vs['O'] - r[0] - r[2] - r[4];

		cout << "Case #" << t + 1 << ": ";
		for (int i = 0; i < 10; ++i)
		{
			for (int j = 0; j < r[i]; ++j)
			{
				cout << i;
			}
		}
		cout << endl;
	}

	

	return 0;
}
