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
ifstream in( "d.in" );
#else
istream & in = cin;
#endif
//ostream & out = cout;
ofstream out("d.out");

int main() {
    ios_base::sync_with_stdio(false);
	int ntests;
	in >> ntests;	
	for (int test = 1; test <= ntests; ++test) {		
		ll k, c, s;
		in >> k >> c >> s;
		vll ans;
		if (c == 1) {
			for (int i = 0; i < k; ++i)
				ans.push_back(i + 1);
		} else {
			for (int i = 0; i < k; i += 2) {
				int idx = i;
				ll pos = idx;
				for (int j = 1; j < c; ++j) {
					pos = s * pos + idx;
				}
				ans.push_back(i == k - 1 ? pos + 1 : pos + 2);
			}
		}
		out << "Case #" << test << ": ";
		if (s < ans.size())
			out << "IMPOSSIBLE";
		else
			copy(all(ans), ostream_iterator<ll>(out, " "));
		out << "\n";
	}
    return 0;
}