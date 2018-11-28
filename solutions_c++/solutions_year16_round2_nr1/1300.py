#include <sstream>
#include <string>
#include <vector>
#include <map>
#include <algorithm>
#include <iostream>
#include <utility>
#include <set>
#include <cctype>
#include <queue>
#include <stack>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cstring>

using namespace std;

int main() {
	int T;
	cin >> T;
	for (int t = 1; t <= T; t++) {
		string s;
		cin >> s;
		int n = s.size();
		string ret = "";
		string numStrs[] = {"ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"};
		int letter[26] = {0};
		char decisions[] = {'Z', 'W', 'U', 'X', 'G',   'O', 'H', 'F', 'S', 'I'};
		int indices[]    = {0, 2, 4, 6, 8, 1, 3, 5, 7, 9};
		int count[10] = {0};
		for (int i = 0; i < n; i++) {
			letter[s[i] - 'A']++;
		}
		for (int i = 0; i < 10; i++) {
			int tmp = letter[decisions[i] - 'A'];
			if (tmp > 0) {
				count[indices[i]] += tmp;
				for (int j = 0; j < numStrs[indices[i]].size(); j++) {
					letter[numStrs[indices[i]][j] - 'A'] -= tmp;
				}
			}
		}
		for (int i = 0; i < 10; i++) {
			for (int j = 0; j < count[i]; j++) {
				ret += (char)'0' + i;
			}
		}
		cout << "Case #" << t << ": " << ret << endl;
	}
}

