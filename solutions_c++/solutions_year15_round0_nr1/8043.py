#define _CRT_SECURE_NO_WARNINGS

#include <cstdio>
#include <cstring>
#include <string>
#include <iostream>

using namespace std;

int main() {
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);

	int T, n, count, need_people = 0;
	string s;

	scanf("%d", &T);

	for (int i = 0; i < T; i++) {
		scanf("%d", &n);
		cin >> s;
		count = 0, need_people = 0;
		for (int j = 0; j < s.length(); j++) {
			if (count < j) {
				need_people += (j - count);
				count = j;
			}
			count += s[j] - '0';
		}
		printf("Case #%d: %d\n", i + 1, need_people);
	}
}