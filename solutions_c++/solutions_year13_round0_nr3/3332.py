#include <sstream>
#include <cstring>
#include <string>
#include <iostream>
#include <fstream>
#include <iomanip>
#include <cmath>
#include <climits>
using namespace std;

typedef long long ll;

bool hwpd(ll num) {
	string s;
	ostringstream oss;
	oss << num;
	s = oss.str();
	for (int i = 0; i < s.size() / 2; i++) {
		if (s[i] != s[s.size() - i - 1]) return false;
	}
	return true;
} 

int main() {
	freopen("c.in", "r", stdin);
	freopen("c.out", "w", stdout);
	int t;
	cin >> t;
	bool x = hwpd(123456654321);
	for (int l = 1; l <= t; l++) {
		ll st, ed;
		cin >> st >> ed;
		ll s, e;
		s = sqrt(st);
		e = sqrt(ed);
		if (s * s < st) s++;
		int res = 0;	
		for (int i = s; i <= e; i++) {
			if (hwpd(i) && hwpd(i * i)) res++;
		}
		cout << "Case #" << l << ": " << res << "\n";
	}
	return 0;
}
 
