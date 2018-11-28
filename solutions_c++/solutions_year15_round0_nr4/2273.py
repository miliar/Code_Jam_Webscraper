#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

int main () { 
	int t;
	cin >> t;
	for (int cas = 1; cas <= t; cas++) {
		printf("Case #%d: ", cas);
		int x, r, c;
		cin >> x >> r >> c;
		int minimum = min(r, c);
		int s = r * c;
		if (x == 1) {
			printf("GABRIEL\n");
		} else if (x == 2) {
			if (s % 2 == 0) {
				printf("GABRIEL\n");
			} else {
				printf("RICHARD\n");
			}
		} else if (x == 3) {
			if (s % 3 != 0) {
				printf("RICHARD\n");
			} else {
				if (minimum == 1) {
					printf("RICHARD\n");
				} else {
					printf("GABRIEL\n");
				}
			}
		} else {
			if (s % 4 != 0) {
				printf("RICHARD\n");
			} else {
				if (minimum == 1) {
					printf("RICHARD\n");
				} else if (minimum == 2) {
					printf("RICHARD\n");
				} else if (minimum == 3) {
					printf("GABRIEL\n");
				} else {
					printf("GABRIEL\n");
				}
			}
		}
	}
	return 0;
}
