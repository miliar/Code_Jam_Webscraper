#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <cassert>
#include <map>
using namespace std;

const int INF = 2e9;
const int N = 5555;


int main() {
#if _DEBUG
	freopen("testLarge.in", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif 
	cout.sync_with_stdio(false);
	cin.tie(0);

	int n;
	cin >> n;
	for (int i = 0; i < n; i++) {
		string s;
		cin >> s;
		string res = "";
		res += s[0];

		for (int j = 1; j < s.length(); j++) {
			if (s[j] >= res[0]) {
				res.insert(res.begin(), s[j]);
			}
			else {
				res.push_back(s[j]);
			}
		}

		cout << "Case #" << i + 1 << ": " << res << endl;
	}
}