#include <iostream>
#include <sstream>
#include <cmath>
#include <algorithm>
#include <string>
#include <string.h>
#include <cstdio>
#include <vector>
#include <map>
#include <set>
#include <cstring>
#include <queue>
#include <bitset>
#include <queue>
#include <unordered_map>


using namespace std;


int main() {
	freopen("output.txt", "w", stdout);
	int t;
	cin >> t;
	for (int iii = 0; iii < t; iii++) {
		string s;
		cin >> s;
		int n = (int)s.size();
		int c = 0;
		int ans = 0;
		for (int i = n - 1; i >= 0; i--) {
			if ((!c && s[i] == '-') || (c && s[i] == '+')) {
				ans++;
				c = 1 - c;
				continue;
			}
		}
		printf("Case #%d: %d\n", iii + 1, ans);
	}
    return 0;
}
