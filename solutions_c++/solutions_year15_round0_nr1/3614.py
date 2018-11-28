#define _CRT_SECURE_NO_WARNINGS

#include <stdio.h>
#include <algorithm>
#include <fstream>
#include <vector>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <string>
#include <utility>
#include <iomanip>
#include <iostream>
#include <cmath>
#include <bitset>
#include <time.h>
#include <iterator>

using namespace std;

int main() {
	freopen("A-large.in", "r", stdin);
	freopen("output.txt", "w", stdout);

	int T, k = 1;
	cin >> T;
	while (T--) {
		int N;
		cin >> N;
		string s;
		cin >> s;
		int cnt = 0,ans = 0; 
		for (int i = 0; i < N + 1; i++) {
			if (s[i] != '0') {
				ans += max(0, i - cnt);
				cnt += max(0, i - cnt);
			}
			cnt += (s[i] - '0');
		}
		cout << "Case #" << k << ": " << ans << endl;
		k++;
	}
	return 0;
}