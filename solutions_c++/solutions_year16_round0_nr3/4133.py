#include <iostream>
#include <fstream>
#include <string>

#include <sstream>
#include <iomanip>

#include <map>
#include <set>
#include <vector>
#include <list>
#include <queue>
#include <stack>
#include <bitset>

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
#define REP(M_i, M_n)			FOR(M_i, 0, M_n)
#define FOREACH(M_ite, M_c)		for(decltype(M_c.begin()) M_ite = M_c.begin(); M_ite != M_c.end(); ++M_ite)

#define DUMP(x)			cerr << #x << " = " << (x) << endl
#define DUMP_C(M_c)		FOREACH(ite, M_c){ cerr << *ite << ", "; } cerr << endl
#define DUMP_CS(M_c)	FOREACH(ite, M_c){ cerr << *ite << " "; } cerr << endl
#define DUMP_CN(M_c)	FOREACH(ite, M_c){ cerr << *ite << endl; } cerr << endl

typedef char				sbyte;
typedef unsigned char		byte;
typedef unsigned short		ushort;
typedef unsigned int		uint;
typedef long long			ll;
typedef unsigned long long ull;


template<typename T>
void print_result(ostream& out, int index, const T& result)
{
	out << "Case #" << (index + 1) << ": " << result << endl;
}

void print_progress(int i) { cout << "solving #" << i + 1 << "..." << endl; }

bool find_divisor(ll value, ll& result)
{
	for(ll i = 2; i * i <= value; ++i)
	{
		if(value % i == 0)
		{
			result = i;
			return true;
		}
	}
	return false;
}

void solve(ostream& out, int n, int j)
{
	int h_bit = n - 1;
	int c = 0;
	for(uint32_t bit = 0; c < j; ++bit)
	{
		bool valid = true;
		vector<ll> list;
		for(int base = 2; base <= 10; ++base)
		{
			ll value = (ll)pow(base, h_bit) + 1;

			for(int col = 1; col <= n - 2; ++col)
			{
				if(bit & (1 << (col - 1))) { value += (ll)pow(base, col); }
			}

			ll div = 0;
			if(! find_divisor(value, div))
			{
				valid = false;
				break;
			}

			list.push_back(div);
		}

		if(valid)
		{
			++c;
			out << "1";
			for(int col = n - 2; col > 0; --col)
			{
				out << ((bit & (1 << (col - 1))) ? "1" : "0");
			}
			out << "1 ";

			for(auto v : list)
			{
				out << v << " ";
			}
			out << endl;
		}
	}

}

void solve(istream& in, ostream& out)
{
	int tt;
	in >> tt;
	for(int t = 0; t < tt; ++t)
	{
		print_progress(t);
		int n, j;
		in >> n >> j;
		out << "Case #1:" << endl;
		solve(out, n, j);
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

