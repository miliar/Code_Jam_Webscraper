#include <iostream>
#include <sstream>
#include <iomanip>

#include <map>
#include <set>
#include <vector>
#include <list>
#include <queue>
#include <stack>
#include <bitset>
#include <string>

#include <numeric>
#include <utility>
#include <functional>
#include <algorithm>
#include <complex>
#include <memory>

#include <cstdio>
#include <cstdlib>
#include <cassert>

#include <cmath>
#include <climits>
#include <cfloat>

#include <cctype>
#include <cstring>

using namespace std;

#define FOR(M_i, M_from, M_to)	for(int M_i = (M_from); M_i < (M_to); ++M_i)
#define REP(M_i, M_n)				FOR(M_i, 0, M_n)
#define FOREACH(M_ite, M_c) for(decltype(M_c.begin()) M_ite = M_c.begin(); M_ite != M_c.end(); ++M_ite)

template<typename CONTAINER_T>
void read(istream& in, CONTAINER_T& list, size_t n)
{
	for(size_t i = 0; i < n; ++i)
	{
		CONTAINER_T::value_type value;
		in >> value;
		list.push_back(value);
	}
};

template<typename T, typename INDEX_T = int>
struct t_indexed_value
{
	typedef t_indexed_value<T, INDEX_T> self; 
	typedef T		value_t;
	typedef INDEX_T	index_t;

	value_t value;
	index_t index;

	bool operator <(const self& obj) const { return value < obj.value; }
	bool operator ==(const self& obj) const { return value == obj.value; }
	bool operator !=(const self& obj) const { return !(*this == obj); }
};

template<typename FORWARD_ITE>
void write(ostream& out, FORWARD_ITE first, FORWARD_ITE last, const string& sep = " ")
{
	if(first != last) { out << *first; ++first; }
	while(first != last)
	{
		out << sep << *first;
		++first;
	}
	out << endl;
}


double solve_from(double c, double f, double x, int farm_count, double cur_cookie, double now, double time_limit)
{
	const double rate = 2 + (f * farm_count);
	double min_time = min(time_limit, now + x / rate);
	const double next_farm_time = (c - cur_cookie) / rate;
	const double next_rate = (2 + (f * (farm_count + 1)));

	if(now + next_farm_time + x / next_rate < time_limit)
	{
		min_time = min(min_time,
			solve_from(c, f, x, farm_count + 1, cur_cookie + (rate * next_farm_time) - c, now + next_farm_time, min_time));
	}

	return min_time;
}

double solve(double c, double f, double x)
{
	return solve_from(c, f, x, 0, 0, 0, x / 2);
}

void solve(istream& in, ostream& out)
{
	int n; in >> n;
	REP(i, n)
	{
		double c, f, x;
		in >> c >> f >> x;
		out << "Case #" << (i + 1) << ": " << fixed << setprecision(7) << solve(c, f, x) << endl;
	}
}

int main(int argc, char* argv[])
{
	ios::sync_with_stdio(false);
	solve(cin, cout);
	return 0;
}

