#include <bits/stdc++.h>

std::string str;

void init() {
	std::cin >> str;
}

void work() {
	int answer = 0;
	for (int i = 0; i < (int)str.length(); i ++) {
		if (i == 0 || str[i] != str[i - 1]) {
			answer ++;
		}
	}
	answer -= (*str.rbegin() == '+');
	std::cout << answer << std::endl;
}

int main() {
	freopen("b.in", "r", stdin);
	freopen("b2.out", "w", stdout);
	
	int testCnt;
	std::cin >> testCnt;
	for (int i = 1; i <= testCnt; i ++) {
		printf("Case #%d: ", i);
		init();
		work();
	}
	
	return 0;
}
