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
ifstream in( "b.in" );
#else
istream & in = cin;
#endif
//ostream & out = cout;
ofstream out("b.out");

int main() {
	ios_base::sync_with_stdio(false);
	int ntests;
	in >> ntests;
	for (int test = 1; test <= ntests; ++test) {
		string s;
		in >> s;
		int ans = s.back() == '-';
		for (int i = 1; i < s.size(); ++i) {
			ans += s[i] != s[i - 1];
		}
		out << "Case #" << test << ": " << ans << "\n";
	}
	return 0;
}