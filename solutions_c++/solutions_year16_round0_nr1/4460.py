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

size_t getbin(size_t v)
{
	size_t r = 0;
	while (v != 0)
	{
		r |= ((size_t)1 << (v % 10));
		v /= 10;
	}
	return r;
}

size_t solve(size_t v)
{
	size_t x = 0x3FF;
	size_t a = v;
	size_t b = getbin(v);
	while (b != 0x3FF)
	{
		a += v;
		b |= getbin(a);
	}
	return a;
}

int main()
{
	size_t N; cin >> N;
	for (size_t n = 0; n < N; ++n)
	{
		size_t v; cin >> v;
		cout << "Case #" << n+1 << ": " << (v == 0 ? "INSOMNIA" : to_string(solve(v)).c_str()) << endl;
	}

	return 0;
}
