#include <algorithm>
#include <iostream>
#include <sstream>
#include <iomanip>
#include <cstring>
#include <bitset>
#include <string>
#include <vector>
#include <cstdio>
#include <stack>
#include <queue>
#include <list>
#include <set>
#include <map>
using namespace std;

void flip(string &s, int e) {
	reverse(s.begin(), s.begin() + e + 1);
	for (int i = 0; i <= e; ++i)
	if (s[i] == '+')
		s[i] = '-';
	else
		s[i] = '+';
}

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	
	int t, e, cnt;
	string s;
	cin >> t;
	for (int i = 1; i <= t; ++i) {
		cin >> s;
		e = s.length() - 1;
		cnt = 0;
		while (true) {
			while (e > -1 && s[e] == '+')
				--e;
			if (e == -1)
				break;			
			if (s[0] == '-') {
				++cnt;
				flip(s, e);
			}
			else {
				++cnt;
				int i = 0;
				while (i <= e && s[i] == '+')
					++i;
				flip(s, i - 1);
			}
		}
		printf("Case #%d: %d\n", i, cnt);
	}
	
	return 0;
}