#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <cmath>
#include <algorithm>
#include <cstdio>
#include <cstring>
#include <string>
#include <cstdlib>
#include <vector>
#include <bitset>
#include <map>
#include <queue>
#include <ctime>
#include <stack>
#include <set>
#include <list>
#include <deque>
#include <functional>
#include <sstream>
#include <fstream>
#include <complex>
#include <numeric>
#include <assert.h>
#include <iomanip>
#include <unordered_map>

using namespace std;

int main() {
	ios::sync_with_stdio(false);
	freopen("B-large.in", "r", stdin);
	freopen("output.txt", "w", stdout);
	
	int t;
	cin >> t;
	for (int i = 1; i <= t; i++) {
		string s;
		cin >> s;
		int cnt = 0;
		for (int j = (int)s.size() - 1; j >= 0; j--) {
			if (s[j] == '-') {
				cnt++;
				for (int k = 0; k <= j; k++) {
					if (s[k] == '+')
						s[k] = '-';
					else
						s[k] = '+';
				}
			}
		}
		cout << "Case #" << i << ": " << cnt << endl;
	}
	return 0;
}