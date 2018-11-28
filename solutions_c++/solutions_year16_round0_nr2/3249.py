#include <iostream>
#include <stdio.h>
#include <memory.h>
#include <string>
#include <algorithm>
#include <cmath>
using namespace std;

int main() {
	freopen("input.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	int T;
	cin >> T;
	for (int caseID = 1; caseID <= T; ++caseID) {
		string packs;
		cin >> packs;
		int ans = 0;
		for (int i = packs.length() - 1; i >= 0; --i) {
			if (packs[i] == '-') {
				bool needEx = false;
				for (int j = 0; j < i; ++j) {
					if (packs[j] == '+') {
						needEx = true;
						packs[j] = '-';
					}
					else break;
				}
				if (needEx) ++ans;
				for (int j = 0; j <= i / 2; ++j) {
					char x = packs[j];
					if (packs[i - j] == '-') packs[j] = '+';
					else packs[j] = '-';
					if (x == '-') packs[i - j] = '+';
					else packs[i - j] = '-';
				}
				++ans;
			}
		}
		printf("Case #%d: %d\n", caseID, ans);
	}
}