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

using namespace std;

int main()
{
	int MAX = 1000;

	size_t T; cin >> T;
	for (size_t t = 0; t < T; ++t)
	{
		size_t N, J; cin >> N >> J;

		cout << "Case #" << t + 1 << ": " << endl;

		string o;
		while (o.length() != N ) o.push_back('1');

		size_t found = 0;
		for (size_t i = 0; i < ((size_t)1 << (N - 2)) && found < J; ++i)
		{
			string x;
			size_t j = i;
			while (j != 0) {
				if (j & 1) {
					x = "1" + x;
				} else {
					x = "0" + x;
				}
				j >>= 1;
			}
			while (x.length() != N - 2) x = "0" + x;
			x = "1" + x + "1";

			vector<uint64_t> vs;
			for (int s = 2; s <= 10; ++s)
			{
				uint64_t v = strtoull(x.c_str(), nullptr, s);

				bool notprime = false;
				uint64_t uu;
				for (uu = 2; uu < v && uu <= MAX; ++uu)
				{
					if (v % uu == 0) {
						notprime = true;
						break;
					}
				}

				if(!notprime) {
					break;
				}
				vs.push_back(uu);
			}
			if (vs.size() == 9)
			{
				cout << x;
				for (size_t u = 0; u < vs.size(); ++u) cout << " " << vs[u];
				cout << endl;
				++found;
				// cout << "found" << found << endl;
			}
		}
	}

	return 0;
}
