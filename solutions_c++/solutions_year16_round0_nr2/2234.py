#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <iostream>
#include <cstring>
#include <string>
using namespace std;

string s;

int main() {
	int tests;
	scanf("%d", &tests);
	for (int i = 0; i < tests; i++) {
		cin >> s;
		int answer = 0;
		for (int j = 1; j < (int)s.size(); j++) {
			answer += (s[j] != s[j - 1]);
		}
		printf("Case #%d: %d\n", i + 1, answer + (s.back() == '-'));
	}
	return 0;
}
