#include <iostream>
#include <string>

#define min(a, b) ((a) < (b) ? (a) : (b))

void flip(std::string &n, int s) {
	s = min(s, n.length());
	if (s == 0) {
		n[0] = n[0] == '-' ? '+' : '-';
		return;
	}
	for (int i = 0; i <= s; ++i, --s) {
		char tmp = n[i];
		n[i] = n[s] == '+' ? '-' : '+';
		n[s] = tmp == '+' ? '-' : '+';
	}
}

bool check(const std::string &n, int &a) {
	if (n.length() == 1) {
		a = 0;
		return n[0] == '+' ? true : false;
	}
	for (int i = 0; i < n.length() - 1; ++i)
		if (n[i] != n[i + 1]) {
			a = i;
			return false;
		}
	a = n.length() - 1;
	return n[0] == '+' ? true : false;
}

int do_work(std::string &n) {
	int i;
	int a = 0;
	bool ret = check(n, i);
	while (!check(n, i)) {
		flip(n, i);
		++a;
	}
	return a;
}

int main() {
	int t;
	std::string n;
	std::cin >> t;
	for (int i = 1; i <= t; ++i) {
		std::cin >> n;
		std::cout << "Case #" << i << ": " << do_work(n) << std::endl;
	}
	return 0;
}
