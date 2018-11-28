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

	for (size_t i = 0; i < T; ++i)
	{
		size_t N; cin >> N;
		deque<pair<size_t, char>> P;
		for (size_t n = 0; n < N; ++n)
		{
			size_t p; cin >> p;
			P.push_back({ p, 'A' + n });
		}
		cout << "Case #" << i + 1 << ":";
		while (P.size() != 0)
		{
			sort(P.begin(), P.end(), greater<pair<size_t, char>>());

			if (P.size() == 2 && P.at(0).first == P.at(1).first) {
				cout << " " << P.at(0).second << P.at(1).second;
				P.at(0).first -= 1;
				P.at(1).first -= 1;
				if (P.at(0).first == 0) {
					P.pop_front();
				}
				if (P.at(0).first == 0) {
					P.pop_front();
				}
			} else {
				cout << " " << P.at(0).second;
				P.at(0).first -= 1;
				if (P.at(0).first == 0) {
					P.pop_front();
				}
			}
		}
		cout << endl;
	}

	return 0;
}
