#include <iostream>
#include <fstream>
#include <map>
#include <stack>
#include <queue>
#include <deque>
#include <set>
#include <cmath>
#include <vector>
#include <algorithm>
#include <string>
#include <time.h>
#include <memory.h>
#include <sstream>

using namespace std;


int main() {
	ios_base::sync_with_stdio(false);

	ifstream cin("input.txt");
	ofstream cout("output.txt");

	int tests;
	cin >> tests;
	for (int t = 1; t <= tests; t++) {
		string s;
		cin >> s;
		int ans = 0;
		for (int i = s.length() - 1; i >= 0; i--) {
			if (s[i] == '+') {
				continue;
			}
			if (i == 0) {
				ans++;
				break;
			}
			if (s[0] == '-') {
				for (int l = 0, r = i; l < r; l++, r--) {
					swap(s[l], s[r]);
				}
				for (int j = 0; j <= i; j++) {
					s[j] = (s[j] == '-' ? '+' : '-');
				}
				ans++;
			}
			else {
				for (int j = 0; j < i && s[j] == '+'; j++) {
					s[j] = '-';
				}
				ans++;
				i++;
				continue;
			}
		}

		cout << "Case #" << t << ": " << ans << endl;
	}

	//system("pause");
	return 0;
}