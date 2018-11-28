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


int calc_win_normal(vector<double> a, vector<double> b)
{
	sort(a.begin(), a.end());
	sort(b.begin(), b.end());

	int win_count = 0;
	size_t n = a.size();
	REP(i, n)
	{
		double a_value = a[0];
		auto ite = b.begin();
		while(ite != b.end() && a_value > *ite) { ++ite; }
		if(ite == b.end()) { ite = b.begin(); }
		if(a_value > *ite) { ++win_count; }
		a.erase(a.begin());
		b.erase(ite);
	}

	return win_count;
}

int calc_win_dec(vector<double> a, vector<double> b)
{
	size_t n = a.size();

	sort(a.begin(), a.end(), greater<double>());
	sort(b.begin(), b.end(), greater<double>());

	int win_count2 = 0;
	REP(i, n)
	{
		bool all_bigger = true;
		REP(j, a.size())
		{
			if(a[j] <= b[j]) { all_bigger = false; break; }
		}

		if(all_bigger) { win_count2 += a.size(); break; }
		a.erase(a.end() - 1);
		b.erase(b.begin());
	}
	return win_count2;

}

void solve(istream& in, ostream& out)
{
	int t; in >> t;
	REP(i, t)
	{
		int n; in >> n;
		vector<double> a, b;
		read(in, a, n);
		read(in, b, n);

		out << "Case #" << (i + 1) << ": " << calc_win_dec(a, b) << " " << calc_win_normal(a, b) <<endl;
	}
}

int main(int argc, char* argv[])
{
	ios::sync_with_stdio(false);
	solve(cin, cout);
	return 0;
}

