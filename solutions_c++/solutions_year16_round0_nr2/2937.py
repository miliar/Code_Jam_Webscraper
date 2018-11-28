#include <stdio.h>
#include <iostream>
#include <string>
using namespace std;

int main() {

	int T;
	scanf("%d", &T);

	for (int tt = 1; tt <= T; tt++) {

		string str;
		cin >> str;

		int cnt = 0;

		if (str.back() == '-') cnt++;

		for (int i = str.length() - 1; i > 0; i--) {
			if (str[i] != str[i - 1]) cnt++;
		}
		printf("Case #%d: %d\n", tt, cnt);
	}
}