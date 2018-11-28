#include <array>
#include <cassert>
#include <iomanip>
#include <set>
#include <fstream>
#include <iostream>
#include <iterator>
#include <vector>
#include <numeric>
#include <algorithm>
#include <map>
using namespace std;

set<char> q = {'1', 'i', 'j', 'k'};

map<pair<char,char>, char> m = {
	{{'1', '1'}, '1'},
	{{'1', 'i'}, 'i'},
	{{'1', 'j'}, 'j'},
	{{'1', 'k'}, 'k'},

	{{'i', '1'}, 'i'},
	{{'i', 'i'}, -'1'},
	{{'i', 'j'}, 'k'},
	{{'i', 'k'}, -'j'},

	{{'j', '1'}, 'j'},
	{{'j', 'i'}, -'k'},
	{{'j', 'j'}, -'1'},
	{{'j', 'k'}, 'i'},

	{{'k', '1'}, 'k'},
	{{'k', 'i'}, 'j'},
	{{'k', 'j'}, -'i'},
	{{'k', 'k'}, -'1'},
};

map<string, char> memo;

char mult ( char a, char b ) {
	int sign = a * b < 0 ? -1 : 1;
	a = abs(a);
	b = abs(b);
	//assert(q.count(a) != 0);
	//assert(q.count(b) != 0);
	pair<char, char> index(a, b);
	//assert(m.count(index) != 0);
	return sign * m[index];
}

char reduce ( string s ) {
	//assert(s.length() > 0);
	if (s.length() == 1) return s[0];

	int k = s.length() / 2;
	return mult(reduce(s.substr(0,k)), reduce(s.substr(k)));
}

/* compute the power s^x, x >= 0
char reduce ( string s, int x ) {
	if ( x == 0 ) return '1';
	if ( x == 1 ) return reduce(s);

	int k = x / 2;
	return mult(reduce(s, k), reduce(s, x-k));
}*/

int solve ( string& input, int x ) {
	int total = input.length() * x;
	string s;
	if ( total < 3 ) return false;

	while ( x-- > 0 ) s += input;
	//cout << s << endl;

	char icurrent = s[0];
	for ( int i = 1; i < total; ++i ) {
		// if [0,i) reduces to 'i'
		if ( icurrent == 'i' ) {
			char jcurrent = s[i];
			for ( int j = i + 1; j < total; ++j ) {
				// if [i,j) reduces to 'j'
				if ( jcurrent == 'j' ) {
					string c = s.substr(j);
					char rc = memo.count(c) != 0 ? memo[c] : reduce(c);
					if (!memo.count(c)) memo[c] = rc;
					if ( rc == 'k' ) return true;
				}

				jcurrent = mult(jcurrent, s[j]);
			}
		}

		icurrent = mult(icurrent, s[i]);
	}

	return false;
}


void readcase ( int n, ifstream& infile ) {
	int l, x;
	string s;

	infile >> l >> x >> s;

	cout << "Case #" << n+1 << ": " << (solve(s, x) ? "YES" : "NO") << endl;
}




int main ( int argc, char** argv ) {
	/*cout << reduce("jij") << endl;
	cout << reduce("iji") << endl;
	cout << reduce("jijiji") << endl;*/


	if ( argc < 2 ) {
		cout << "Give me one file as input." << endl;
		return 1;
	}

	ifstream infile(argv[1]);

	int t;
	infile >> t;
	for ( int i = 0; i < t; ++i ) {
		readcase(i, infile);
	}

	return 0;
}