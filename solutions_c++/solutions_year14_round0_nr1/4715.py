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


const string BAD_MAG = "Bad magician!";
const string BAD_VOL = "Volunteer cheated!";

string solve(int row1, int table1[4][4], int row2, int table2[4][4])
{
	--row1;
	--row2;

	map<int, int> m;
	map<int, int> m2;
	for(int x = 0; x < 4; ++x)
	{
		m[table1[row1][x]]++;
		m[table2[row2][x]]++;
	}

	int val = -1;
	for(auto ite = m.begin(); ite != m.end(); ++ite)
	{
		if(ite->second == 2)
		{
			if(val >= 0) { return BAD_MAG; }
			val = ite->first;
		}
	}

	if(val < 0) { return BAD_VOL; }
	stringstream s;
	s << val;
	return s.str();
}

void solve(istream& in, ostream& out)
{
	int n = 0; in >> n;

	REP(i, n)
	{
		int row1, row2;
		int table1[4][4] = {0};
		int table2[4][4] = {0};
		in >> row1;
		REP(y, 4) REP(x, 4)
		{
			in >> table1[y][x];
		}
		in >> row2;

		REP(y, 4) REP(x, 4)
		{
			in >> table2[y][x];
		}
		out << "Case #" << (i + 1) << ": " << solve(row1, table1, row2, table2) << endl;
	}	
}

int main(int argc, char* argv[])
{
	ios::sync_with_stdio(false);
	solve(cin, cout);
	return 0;
}

