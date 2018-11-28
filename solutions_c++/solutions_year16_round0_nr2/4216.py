#include <algorithm>
#include <cmath>
#include <memory.h>
#include <iostream>
#include <fstream>
#include <vector>

using namespace std;

typedef long long ll;

int a[1000 + 100];

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int test;
	cin >> test;
	string s;
	getline(cin, s);
	for (int tst = 1; tst <= test; ++tst) {
		cout << "Case #" << tst << ": ";
		string s;
		getline(cin, s);  
		int ans = 0;
		int n = s.size();
		for (int i = 0; i < n; ++i) if (s[i] == '-') a[i + 1] = 1; else a[i + 1] = 0;
		for (int i = n; i >= 1; --i) {
			if (a[i] == 1) {
				++ans;
				for (int j = 1; j <= i; ++j) a[j] = 1 - a[j];
			}
		}
		cout << ans << endl;
	}
	return 0;           
}