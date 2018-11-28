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

size_t solve(const std::string& v)
{
	size_t c = 1;
	char b = v[0];

	for (size_t i = 1; i < v.size(); ++i)
	{
		if (v[i] != b) {
			++c;
			b = v[i];
		}
	}

	if (*v.rbegin() == '+') --c;

	return c;
}

int main()
{
	size_t N; cin >> N;
	for (size_t n = 0; n < N; ++n)
	{
		std::string v; cin >> v;
		cout << "Case #" << n+1 << ": " << to_string(solve(v)) << endl;
	}

	return 0;
}
