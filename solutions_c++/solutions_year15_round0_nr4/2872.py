#include <bits/stdc++.h>
using namespace std;

/*
 * You got a dream, you gotta protect it.
 */

typedef long long ll;

int main(int argc, char **argv) {
//	freopen("D-small-attempt0.in", "r", stdin);
//	freopen("output.txt", "w", stdout);
	int t, k = 1;
	scanf("%d", &t);
	while (t--) {
		int x, r, c;
		scanf("%d%d%d", &x, &r, &c);
		printf("Case #%d: ", k++);
		if (r == 1 && c == 1) {
			if (x == 1)
				puts("GABRIEL");
			else
				puts("RICHARD");
			continue;
		}
		if (r == 1 && c == 2) {
			if (x <= 2)
				puts("GABRIEL");
			else
				puts("RICHARD");
			continue;
		}
		if (r == 1 && c == 3) {
			if (x == 1)
				puts("GABRIEL");
			else
				puts("RICHARD");
			continue;
		}
		if (r == 1 && c == 4) {
			if (x <= 2)
				puts("GABRIEL");
			else
				puts("RICHARD");
			continue;
		}
		if (r == 2 && c == 1) {
			if (x <= 2)
				puts("GABRIEL");
			else
				puts("RICHARD");
			continue;
		}
		if (r == 2 && c == 2) {
			if (x <= 2)
				puts("GABRIEL");
			else
				puts("RICHARD");
			continue;
		}
		if (r == 2 && c == 3) {
			if (x <= 3)
				puts("GABRIEL");
			else
				puts("RICHARD");
			continue;
		}
		if (r == 2 && c == 4) {
			if (x <= 2)
				puts("GABRIEL");
			else
				puts("RICHARD");
			continue;
		}
		if (r == 3 && c == 1) {
			if (x == 1)
				puts("GABRIEL");
			else
				puts("RICHARD");
		}
		if (r == 3 && c == 2) {
			if (x <= 3)
				puts("GABRIEL");
			else
				puts("RICHARD");
			continue;
		}
		if (r == 3 && c == 3) {
			if (x & 1)
				puts("GABRIEL");
			else
				puts("RICHARD");
			continue;
		}
		if (r == 3 && c == 4) {
			puts("GABRIEL");
			continue;
		}
		if (r == 4 && c == 1) {
			if (x <= 2)
				puts("GABRIEL");
			else
				puts("RICHARD");
			continue;
		}
		if (r == 4 && c == 2) {
			if (x <= 2)
				puts("GABRIEL");
			else
				puts("RICHARD");
			continue;
		}
		if (r == 4 && c == 3) {
			puts("GABRIEL");
			continue;
		}
		if (r == 4 && c == 4) {
			if (x != 3)
				puts("GABRIEL");
			else
				puts("RICHARD");
			continue;
		}
	}
	return 0;
}