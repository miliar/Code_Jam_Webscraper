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
		string s; cin >> s;
		char cur = '+';
		int tot = 0;
		for (int i = s.size() - 1;i >= 0;i--) {
			if (s[i] != cur) {
				tot++;
				cur = s[i];
			}
		}
		cout << "Case #" << caso + 1 << ": " << tot << endl;
	}
}
