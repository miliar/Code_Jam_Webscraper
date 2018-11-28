#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <vector>
#include <list>
#include <map>
#include <string>
#include <algorithm>

using namespace std;

#define ProblemName "A"
#define InputSize   "small"

typedef unsigned long long _uint64_t;

_uint64_t solve(list<int>& a, _uint64_t cur_size, _uint64_t cur_steps)
{
	if ( a.size() == 0 )
	{
		return cur_steps;
	} else if ( cur_size > a.front() )
	{
		int z = a.front();
		a.erase(a.begin());
		_uint64_t ret = solve(a, cur_size + z, cur_steps);
		a.insert(a.begin(), z);
		return ret;
	} else
	{
		_uint64_t s1 = -1;
		if ( cur_size > 1 )
		{
			a.insert(a.begin(), cur_size - 1);
			s1 = solve(a, cur_size, cur_steps + 1);
			a.erase(a.begin());
		}
		int z = a.front();
		a.erase(a.begin());

		_uint64_t s = min(s1, solve(a, cur_size, cur_steps + 1));

		a.insert(a.begin(), z);

		return s;
	}
}

int main(int argc, char **argv)
{
	freopen(ProblemName "-" InputSize ".in", "rb", stdin);
	freopen(ProblemName "-" InputSize ".out", "wb", stdout);

	int T;
	scanf("%d", &T);
	for ( int t = 1;
		  t <= T;
		  t++ )
	{
		int A, N;
		vector<int> s;
		scanf("%d %d", &A, &N);
		s.resize(N);
		for(int i = 0; i < N; i++)
		{
			scanf( "%d", &s[i]);
		}

		sort(s.begin(), s.end());

		list<int> l(s.begin(), s.end());

		printf("Case #%d: %d\n", t, solve(l, A, 0));
	}

	fclose(stdin);
	fclose(stdout);
	return 0;
}