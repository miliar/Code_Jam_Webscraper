#include <iostream>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <cstring>
#include <vector>
#include <string>

using namespace std;

const int maxN = 110, maxLen = 1000000, oo = 23041997;

#define fo "A.txt"
#define foru(i, l, r) for (int i = l; i <= r; ++i)
#define ford(i, r, l) for (int i = r; i >= l; --i)
#define repu(i, r) for (int i = 0; i < r; ++i)
#define ll long long

int n, test;
char s[maxN];

int main() {
	scanf("%d\n", &test);
	freopen(fo, "w", stdout);
	int i = 0, curr;
	while (test--) {
		scanf("%s\n", s);
		int res = 0;
		++i;
		cout << "Case #" << i << ": ";
		int len = strlen(s);
		repu(i, len) {
			if (i == 0) { curr = (s[i] == '+'); continue; }
			int temp = (s[i] == '+');
			if (curr != temp) ++res, curr = 1 - curr;
		}
		if (!curr) ++res;
		cout << res << endl;
	}
}