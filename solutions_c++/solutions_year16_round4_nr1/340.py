#include <bits/stdc++.h>

int n;
int cnt[5];
char ch[5] = {'R', 'P', 'S'};

void init() {
	std::cin >> n >> cnt[0] >> cnt[1] >> cnt[2];
}

std::string getString(int deep, int x) {
	if (deep == n) {
		std::string result;
		result += ch[x];
		return result;
	}
	std::string s1 = getString(deep + 1, x);
	std::string s2 = getString(deep + 1, (x + 2) % 3);
	return std::min(s1 + s2, s2 + s1);
}

bool check(const std::string &str) {
	static int toDigit[1000];
	toDigit['R'] = 0;
	toDigit['P'] = 1;
	toDigit['S'] = 2;
	
	int cc[5] = {0, 0, 0};
	for (int i = 0; i < (int)str.length(); i ++) {
		cc[toDigit[str[i]]] ++;
	}
	return cc[0] == cnt[0] && cc[1] == cnt[1] && cc[2] == cnt[2];
}

void work() {
	std::string answer;
	for (int i = 0; i < 3; i ++) {
		std::string str = getString(0, i);
		//std::cout << str << std::endl;
		if (check(str)) {
			if (answer.empty() || str < answer) {
				answer = str;
			}
		}
	}
	if (answer.empty()) {
		printf("IMPOSSIBLE\n");
	} else {
		printf("%s\n", answer.c_str());
	}
}

int main() {
	freopen("a1.in", "r", stdin);
	freopen("a1.out", "w", stdout);
	
	int testCnt;
	std::cin >> testCnt;
	for (int i = 1; i <= testCnt; i ++) {
		printf("Case #%d: ", i);
		init();
		work();
	}
	
	return 0;
}
