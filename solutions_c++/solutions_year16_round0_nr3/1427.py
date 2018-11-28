#include <algorithm>
#include <bitset>
#include <cassert>
#include <cctype>
#include <cmath>
#include <complex>
#include <cstdlib>
#include <fstream>
#include <iomanip>
#include <iostream>
#include <iterator>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <string>
#include <vector>
#pragma warning( disable : 4244 4267 4018 4996 4800 )
//#pragma comment( linker, "/stack:10000000" )
using namespace std; 
typedef vector< int > vi; typedef vector< vector< int > > vvi; typedef vector< string > vs; typedef vector< double > vd;
typedef vector< vd > vvd; typedef long long ll; typedef vector< ll > vll; typedef vector< vll > vvll; typedef pair< int, int > pii;
#define all( v ) (v).begin( ), (v).end( )

#ifdef LOCAL
ifstream in( "c.in" );
#else
istream & in = cin;
#endif
//ostream & out = cout;
ofstream out("c.out");

int bit_count(int x) {
	int res = 0;
	while (x) {
		res += x & 1;
		x = x >> 1;
	}
	return res;
}

int main() {
    ios_base::sync_with_stdio(false);
	int n, cnt;
	in >> n >> n >> cnt;
	vi v;
	for (int i = 0; i < 1 << (n - 2) / 2; ++i) {
		if (bit_count(i) == 5)
			v.push_back(i);
	}
	out << "Case #1:\n";
	int div[] = { 3, 2, 3, 2, 7, 2, 3, 2, 3 };
	for (int i = 0; i < v.size(); ++i) {
		for (int j = 0; j < v.size(); ++j) {
			string str;
			str.push_back('1');
			int l = v[i], r = v[j];
			for (int k = 0; k < (n - 2) / 2; ++k) {
				str.push_back((l & 1) ? '1' : '0');
				str.push_back((r & 1) ? '1' : '0');
				l >>= 1;
				r >>= 1;
			}
			str.push_back('1');
			out << str;
			for (int i = 0; i < 9; ++i)  out << ' ' << div[i];
			out << "\n";
			/*for (int base = 2; base <= 10; ++base) {
				ll num = 0;
				for (int k = 0; k < str.size(); ++k) {
					num = num * base + (str[k] == '1');
				}
				assert(num % div[base - 2] == 0);
			}*/
			if (--cnt == 0)
				return 0;
		}
	}
    return 0;
}