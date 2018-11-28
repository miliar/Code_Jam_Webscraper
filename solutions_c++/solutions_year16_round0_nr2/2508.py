#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <iostream>
#include <fstream>
#include <algorithm>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>

typedef long long LL;

char s[107];

int main() {
	int T;
	scanf("%d", &T);
	for (int TI = 1; TI <= T; ++TI) {
		scanf("%s", s + 1);
		int n = 0;
		for (int i = 1; s[i] != '\0'; ++i)
			if (s[i] != s[i - 1]) ++n;
		if (s[strlen(s + 1)] == '+') --n;
		printf("Case #%d: %d\n", TI, n);
	}
	return 0;
}
