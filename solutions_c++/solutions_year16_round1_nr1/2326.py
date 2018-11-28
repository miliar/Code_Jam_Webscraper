#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <time.h>

using namespace std;
const int N = 1e6 + 5;

int main() {
#ifdef _DEBUG 
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif 
	cin.tie(0);
	cout.sync_with_stdio(false);

	int t;
	cin >> t;
	for (int i = 1; i <= t; i++) {
		string s;
		cin >> s;
		string temp;
		temp += s[0];
		for (int j = 1; j < s.length(); j++) {
			if (s[j] >= temp[0]) {
				temp.insert(temp.begin(), s[j]);
			}
			else temp.push_back(s[j]);
		}

		cout << "Case #" << i << ": " << temp << endl;
	}
	return t;
}