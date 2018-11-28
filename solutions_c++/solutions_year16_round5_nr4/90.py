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
		unsigned N, L;
		cin >> N >> L;
		vector<string> s(N);
		for (unsigned i = 0; i < N; ++i)
		{
			cin >> s[i];
		}
		string b;
		cin >> b;
		auto sit = find(s.begin(), s.end(), b);
		if (sit == s.end())
		{
			cout << "0";
			for (unsigned i = 1; i < L; ++i)
				cout << "?";
			cout << " ";
			for (unsigned i = 1; i < L; ++i)
				cout << "10";
			cout << "?1";
		}
		else
		{
			cout << "IMPOSSIBLE";
		}
		cout << endl;
	}
	return 0;
}
