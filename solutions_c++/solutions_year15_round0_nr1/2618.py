#include <iostream>
#include <algorithm>
#include <cstdio>
#include <vector>
#include <cstring>
#include <string>
#include <map>
#include <set>
#include <queue>
using namespace std;

int T, S, c;
string STR;

int main() {
	cin >> T;
	while (T--) {
		cin >> S >> STR;
		int s = 0, ans = 0;
		for (int i = 0; i <= S; i++) {
			if (s < i) {
				ans += i - s;
				s = i;
			}
			s += STR[i] - '0';
		}
		printf("Case #%d: %d\n", ++c, ans);
	}
	return 0;
}