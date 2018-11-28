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

int main(int argc, char **argv) {
	freopen("A-large.in", "r", stdin);
	freopen("out.txt", "w", stdout);
	int t, cas = 1;
	scanf("%d", &t);
	while (t--) {
		printf("Case #%d: ", cas++);
		int n, freq[10] = {};
		scanf("%d", &n);
		if (n == 0) {
			puts("INSOMNIA");
			continue;
		}
		int res = -1;
		for (int i = 1; i <= 1000; ++i) {
			int at = n * i;
			for (; at != 0; at /= 10)
				++freq[at % 10];
			bool can = true;
			for (int j = 0; j < 10 && can; ++j)
				can &= freq[j] != 0;
			if (can) {
				res = n * i;
				break;
			}
		}
		assert(res != -1);
		printf("%d\n", res);
	}
	return 0;
}