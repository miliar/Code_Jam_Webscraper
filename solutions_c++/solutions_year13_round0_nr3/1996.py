#include <cstdio>
#include <vector>
#include <map>
#include <iostream>
#include <algorithm>
#include <string.h>

using namespace std;

long long number[(int)1e7];
int sz = 0;

bool pal(char s[]) {
	       int i = 0, j = strlen(s) - 1;
        bool ok = 1;
        while (i < j) {
            if (s[i] != s[j]) {
                ok = 0; break;
            }
            i++, j--;
        }
		return ok;
}
int main() {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int test; cin >> test;
    for (int it=1; it <= 1e7; it++) {
        char s[16], t[10];
        sprintf(s, "%lld", it * 1LL * it);
		sprintf(t, "%d", it);
		bool ok = pal(s) && pal(t);
		if (ok) {
            number[sz++] = it * 1LL * it;
        }
    }
    for (int it = 0; it < test; it++) {
        long long a, b; cin >> a >> b;
        int x = lower_bound(number, number + sz, b) - number;
        int y = lower_bound(number, number + sz, a - 1) - number;
        if (x >= sz || number[x] > b) x--;
        if (y >= sz || number[y] > a - 1) y--;
        printf("Case #%d: %d\n", it + 1, x - y);
    }


	return 0;
}
