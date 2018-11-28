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

void addDigits(set<int>& s, int n) {
	while (n) {
		s.insert(n % 10);
		n /= 10;
	}
}

int main() {
	int t; cin >> t;
	forn(caso, t) {
		set<int> s;
		int n, cur; cin >> n;
		for (cur = n;cur < 1000 * n;cur += n) {
			addDigits(s, cur);
			if (s.size() == 10) break;
		}
		cout << "Case #" << caso + 1 << ": ";
		if (s.size() == 10) {
			cout << cur;
		} else {
			cout << "INSOMNIA";
		} 
		cout << endl;
	}
}
