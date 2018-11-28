#include <iostream>
#include <cstdio>
#include <string>
#include <vector>
#include <cmath>
#include <algorithm>
#include <cstring>
#include <set>
#include <map>
#include <queue>
#include <deque>
#include <stack>
#include <ctime>
#include <cassert>
#include <climits>
#include <memory.h>
#include <bitset>

using namespace std;

int t;
string s, s1, s2;

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	cin >> t;
	for (int ii = 0; ii < t; ii++) {
		cin >> s;
		string cur = "";
		for (int i = 0; i < s.length(); i++) {
			s1 = cur;
			s2 = cur;
			s1 += s[i];
			s2 = s[i] + s2;
			if (s1 > s2) {
				cur += s[i];
			}
			else {
				cur = s[i] + cur;
			}
		}
		cout << "Case #" << ii + 1 << ": " << cur << endl;
	}

	return 0;
}