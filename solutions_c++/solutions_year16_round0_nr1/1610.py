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
ifstream in( "a.in" );
#else
istream & in = cin;
#endif
//ostream & out = cout;
ofstream out("a.out");

int main() {
    ios_base::sync_with_stdio(false);
	int ntests;
	in >> ntests;
	vll ans(1000001);
	for (int i = 1; i < ans.size(); ++i) {
		int seen[10] = {};
		ans[i] = i;
		for (;;) {
			ll x = ans[i];
			while (x) {
				seen[x % 10] = 1;
				x = x /= 10;
			}
			if (find(seen, seen + 10, 0) == seen + 10)
				break;
			ans[i] += i;
			assert(ans[i] <= 2000000000);
		}
	}
	for (int test = 1; test <= ntests; ++test) {
		int n;
		in >> n;
		out << "Case #" << test << ": " << (ans[n] == 0 ? "INSOMNIA" : to_string(ans[n])) << "\n";
	}
    return 0;
}