#define _CRT_SECURE_NO_WARNINGS

#include <iostream>
#include <string>

using namespace std;

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int t;
	cin >> t;
	for (int g = 1; g <= t; ++g) {
		string str;
		cin >> str;
		int k = 0, i = 0;
		bool wasM, wasP = false;
		while (i < str.length()) {
			wasM = false;
			while (i < str.length() && str[i] == '-') {
				++i;
				wasM = true;
			}
			if (!wasP && wasM) {
				++k;
			}
			else if (wasM && wasP){
				k += 2;
			}
			while (i < str.length() && str[i] == '+') {
				++i;
				wasP = true;
			}
		}
		cout << "Case #" << g << ": " << k << '\n';
	}
	return 0;
}