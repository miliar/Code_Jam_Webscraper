#include <iostream>
#include <stdio.h>
#include <vector>
#include <algorithm>
#include <string>
#include <assert.h>
#include <ctype.h>
#include <limits.h>
#include <math.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>
#include <bitset>
#include <deque>
#include <map>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
using namespace std;

typedef long long ll;

const int N = 101;
char s[N];

int main(int argc, char **argv) {
	freopen("B-large.in", "r", stdin);
	freopen("out.txt", "w", stdout);
	int t, cas = 1;
	scanf("%d", &t);
	while (t--) {
		scanf("%s", s);
		int n = strlen(s);
		int res = 0, at = 0;
		while (at < n) {
			if (s[at] == '+') {
				if (at != 0)
					++res;
				break;
			}
			++at;
			if (at == n)
				++res;
		}
		int with = 0;
		while (at < n) {
			if (s[at] == '+') {
				if (with != 0) {
					res += 2;
					with = 0;
				}
				++at;
				continue;
			}
			++with;
			++at;
		}
		if (with != 0)
			res += 2;
		printf("Case #%d: %d\n", cas++, res);
	}
	return 0;
}