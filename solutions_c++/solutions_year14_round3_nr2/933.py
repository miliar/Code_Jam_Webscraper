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

#include <fstream>

template<typename T>
void print_result(ostream& out, int index, const T& result)
{
	out << "Case #" << (index + 1) << ": " << result << endl;
}
template<typename T = int, const T MOD = 10000007>
class t_mod_int
{

public:
	typedef T value_t;
	typedef t_mod_int<T, MOD> self;

private:
	value_t m_value;

public:
	t_mod_int(value_t value = 0) : m_value(adjust(value)) {}
	~t_mod_int() {}

	static inline value_t adjust(value_t value)
	{
		return value % MOD;
	}

public:
	value_t get() const { return m_value; }

	self operator +(const self& other) const	{ return self(m_value + other.m_value); }
	self& operator +=(const self& other)		{ m_value = adjust(m_value + other.m_value); return *this; }
	self operator -(const self& other) const	{ return self(m_value - other.m_value); }
	self& operator -=(const self& other)		{ m_value = adjust(m_value - other.m_value); return *this; }
	self operator *(const self& other) const	{ return self(m_value * other.m_value); }
	self& operator *=(const self& other)		{ m_value = adjust(m_value * other.m_value); return *this; }
	self operator /(const self& other) const	{ return self(m_value / other.m_value); }
	self& operator /=(const self& other)		{ m_value = adjust(m_value / other.m_value); return *this; }
	self operator %(const self& other) const	{ return self(m_value % other.m_value); }
	self& operator %=(const self& other)		{ m_value = adjust(m_value % other.m_value); return *this; }

	self& operator ++()							{ m_value = adjust(m_value + 1); return *this; }
	self& operator --()							{ m_value = adjust(m_value - 1); return *this; }
	self operator ++(int)						{ self ret(m_value); m_value = adjust(m_value + 1); return ret; }
	self operator --(int)						{ self ret(m_value); m_value = adjust(m_value - 1); return ret; }

	self& operator =(const self& other)			{ m_value = other.m_value; return *this; }

	bool operator ==(const self& other) const	{ return m_value == other.m_value; }
	bool operator !=(const self& other) const	{ return m_value != other.m_value; }

	friend bool operator ==(const self& obj, value_t value) { return obj.m_value == value; }
	friend bool operator ==(value_t value, const self& obj) { return obj.m_value == value; }
	friend bool operator !=(const self& obj, value_t value) { return obj.m_value != value; }
	friend bool operator !=(value_t value, const self& obj) { return obj.m_value != value; }

	friend std::ostream& operator <<(std::ostream& out, const self& obj) { return out << obj.m_value; }
	friend std::istream& operator >>(std::istream& in, self& obj) { value_t value; in >> value; obj = value; return in; }

};


bool is_valid(const string& s)
{
	bool used[26] = {false};
	auto ite = s.begin(), end = s.end();
	while(ite != end)
	{
		char ch = *ite;
		int index = ch - 'a';
		if(used[index]) { return false; }
		used[index] = true;
		++ite;
		while(ite != end && *ite == ch) { ++ite; }
	}
	return true;
}

int solve_greedy(vector<string> list)
{
	vector<int> order(list.size());
	REP(i, list.size()) { order[i] = i; }
	t_mod_int<> result;
	do
	{
		string s;
		REP(i, order.size())
		{
			s += list[order[i]];
		}

		if(is_valid(s)) { ++result; }
	}
	while(next_permutation(order.begin(), order.end()));
	return result.get();
}

void solve(istream& in, ostream& out)
{
	int t;
	in >> t;
	REP(i, t)
	{
		int n;
		in >> n;
		vector<string> list(n);
		REP(j, n) { in >> list[j]; }
		sort(list.begin(), list.end(), [](const string& a, const string& b) {
			return lexicographical_compare(a.begin(), a.end(), b.begin(), b.end());
		});
		cerr << "solving #" << (i + 1) << endl;
		print_result(out, i, solve_greedy(list));
	}
}

int main(int argc, char* argv[])
{
	ios::sync_with_stdio(false);
	if(argc == 2)
	{
		ifstream in(argv[1]);
		string out_path = argv[1];
		out_path += ".result";
		ofstream out(out_path);
		solve(in, out);
	}
	else
	{
		solve(cin, cout);
	}
	return 0;
}

