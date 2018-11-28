#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;

#define forsn(i,s,n) for (int i = (s);i < (int)(n);i++)
#define forn(i,n) forsn(i,0,n)
#define dforsn(i,s,n) for (int i = (n - 1);i >= (int)(s);i--)
#define dforn(i,n) dforsn(i,0,n)
#define all(v) (v).begin(), (v).end()

string s;
int cant(char c) {
	return count(s.begin(), s.end(), c);
} 

int main() {
	int t; cin >> t;
	forn(caso, t) {
		cin >> s;
		
		cout << "Case #" << caso + 1 << ": ";

		
		forn(i, cant('Z')) cout << 0;
		int unos = cant('O') - cant('U') - cant('Z') - cant('W');
		forn(i, unos) cout << 1;
		forn(i, cant('W')) cout << 2;
		forn(i, cant('R') - cant('Z') - cant('U')) cout << 3;
		forn(i, cant('U')) cout << 4;
		forn(i, cant('V') - (cant('S') - cant('X'))) cout << 5;
		forn(i, cant('X')) cout << 6;
		int sietes = cant('S') - cant('X');
		forn(i, sietes) cout << 7;
		forn(i, cant('H') - (cant('R') - cant('Z') - cant('U'))) cout << 8;
		forn(i, (cant('N') - unos - sietes) / 2) cout << 9;
		
		cout << endl;
	}
}
