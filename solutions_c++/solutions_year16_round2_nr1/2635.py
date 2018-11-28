#include <iostream>
#include <cstdio>
#include <algorithm>
#include <map>
#include <cmath>
#include <cstdlib>
#include <cmath>
#include <string>
#include <cstring>
#include <vector>

using namespace std;

int n, m, i, j, T, ti;
string s;
int c[27], a[12];

int co(char x) {
	return c[x - 'A'];
}

int main() {
	freopen("./a.in", "r", stdin);
	freopen("./a.out", "w", stdout);
	scanf("%d", &T);
	for (ti = 1; ti <= T; ++ti) {

		cin >> s;
		for (i = 0; i < 26; ++i) c[i] = 0;
		for (i = 1; i < 10; ++i) a[i] = 0;
		for (i = 0; i < s.size(); ++i) {
			c[s[i] - 'A']++;
        }
		a[0] = co('Z');
		a[2] = co('W');
		a[4] = co('U');
		a[6] = co('X');
		a[8] = co('G');
		a[7] = co('S') - a[6];
		a[5] = co('V') - a[7];
		a[3] = co('T') - a[2] - a[8];
		a[1] = co('O') - a[2] - a[4] - a[0];
		a[9] = co('I') - a[5] - a[6] - a[8];
		printf("Case #%d: ", ti);
		for (i = 0; i < 10; ++i) {
			for (j = 1; j <= a[i]; ++j)
				printf("%d", i);
		}
		printf("\n");

	}
	return 0;
}
