/*  
    f1zz0_13
*/

#include <cstdio>
#include <iostream>
#include <vector>
#include <algorithm>
#include <cstring>
#include <string>
#include <cstdlib>
#include <cmath>
#include <ctype.h>
#include <stack>
#include <queue>
#include <limits.h>
#include <fstream>
#include <map>
#include <set>

#define rep(i, a) for(int i = 0; i < a; i++)
#define fo(i, a, b) for(int i = a; i < b; i++)
#define defo(i, a, b) for(int i = a; i >= b; i--)
#define ll long long
#define pb  push_back
#define mp  make_pair
#define sz(a)   ((int)(a.size()))
#define x first
#define y second
#define SET(x, a) memset(x, a, sizeof(x));

using namespace std;

typedef vector<int> vi;
typedef vector<string> vs;
typedef pair<int, int> pii;

inline bool isNP (ll q) {
	rep (i, 41)
		if (pow(2, i) == q)
			return false;
	return true;
}

int main() {
	ifstream fin ("A-small-attempt0.in");
	ofstream fout ("a.txt");

 	int t, n, l;
 	fin >> t;
 	rep (z, t) {
 		string s;
 		fin >> s;
 		ll p, q, foo = 0;
 		rep (i, s.size()) {
 			if (s[i] == '/') {
 				p = foo;
 				foo = 0;
 			}
 			else {
 				foo *= 10;
 				foo += s[i] - '0';
 			}
 		}
 		q = foo;
 		while (p % 2 == 0 && q % 2 == 0) {
 			p /= 2;
 			q /= 2;
 		}

 		if (q % p == 0) {
 			q /= p;
 			p = 1;
 		}

 		// printf("%s, %lld, %lld\n", s.c_str(), p, q);

 		int steps = 0;
 		if (isNP(q))
 			steps = 41;
 		ll a, b, c, d;
 		while (steps <= 40) {
 			if (q <= p)
 				break;
 			else
 				q /= 2;
 			steps++;
 		}
 		if (steps > 40)
 			fout << "Case #" << z+1 << ": impossible\n";
 		else 
 			fout << "Case #" << z+1 << ": " << steps << "\n";
 	}
	return 0;
}