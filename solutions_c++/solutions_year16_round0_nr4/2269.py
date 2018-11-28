#include <iostream>
#include <algorithm>
#include <vector>
#include <cstring>
#include <queue>
#include <set>
#include <map>

using namespace std;

#define forsn(i,s,n) for(int i = (s);i < (int)(n);i++)
#define forn(i,n) forsn(i,0,n)

int main() {
	int t; cin >> t;
	forn(caso, t) {
		int k, c, s; cin >> k >> c >> s;
		
		cout << "Case #" << caso + 1 << ": ";
		forn(i, k) {
			if (i) cout << " ";
			cout << i + 1;
		}
		cout << endl;
	}
}
