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
		int N; cin >> N;
		map<int, int> s;
		for (int n = 0; n < (2*N-1); ++n)
		{
			for (int j = 0; j < N; ++j)
			{
				int v; cin >> v;
				s[v]=s[v]+1;
			}
		}

		std::vector<int> A;
		for (auto itr = s.begin(); itr != s.end(); ++itr)
		{
			if (itr->second % 2) {
				A.push_back(itr->first);
			}
		}
		std::sort(A.begin(), A.end());
		cout << "Case #" << i + 1 << ": ";
		for (size_t j = 0; j < A.size(); ++j)
		{
			cout << (j==0 ? "" : " ") << A.at(j);
		}
		cout << endl;
	}
	return 0;
}
