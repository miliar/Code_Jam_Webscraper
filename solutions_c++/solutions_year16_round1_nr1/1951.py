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
		std::string S; cin >> S;
		std::string A;
		for (size_t j = 0; j < S.length(); ++j)
		{
			if (A.empty()) {
				A.push_back(S.at(j));
			}
			else {
				if (A.at(0) <= S.at(j))
				{
					A.insert(A.begin(), S.at(j));
				} else {
					A.push_back(S.at(j));
				}
			}
		}
		cout << "Case #" << i+1 << ": " << A << endl;
	}
	return 0;
}
