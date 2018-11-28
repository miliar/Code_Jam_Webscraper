#include <cstdio>
#include <iostream>
using namespace std;

int main () {
	int _, t;
	char c, l;
	cin >> _;
	for (int i = 1; i <= _; ++i) {
		printf("Case #%d: ", i);
		c = ' ';
		l = ' ';
		t = 0;
		while (c != '-' && c != '+') c = getchar();
		while (c == '-' || c == '+') {
			if (c != l) {
				l = c;
				++t;
			}
			c = getchar();
		}
		if (l == '+') --t;
		printf("%d\n", t);
	}
}