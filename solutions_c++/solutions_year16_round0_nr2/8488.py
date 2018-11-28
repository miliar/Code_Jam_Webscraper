#include <iostream>
#include <cmath>
#include <cstdio>
#include <algorithm>
#include <set>
#include <cstring>
#include <climits>
#include <map>
#include <vector>
#include <queue>
#include <string>

using namespace std;

int main() {
	freopen("B-large.in", "r", stdin);
	freopen("output.txt", "w", stdout);
	
	int test, cnt;
	string s;
	char sign;

	cin >> test;
	for (int t = 0; t < test; t++) {
		cin >> s;
		sign = '+';
		cnt = 0;
		for (int i = s.length()-1; i >= 0; i--)
			if (s[i] != sign) {
				cnt++;
				if (sign == '+') sign = '-';
				else sign = '+';
			}
		cout << "Case #" << t+1 << ": " << cnt << "\n";
	}

	//system("pause");
    return 0;
}