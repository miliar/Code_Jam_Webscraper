#include <iostream>
#include <cstdio>
#include <cstring>  
#include <string>
#include <cstdlib>
#include <cmath>
#include <cctype>
#include <ctime>
#include <algorithm>
#include <iomanip>
#include <vector>
#include <queue>
#include <map>
#include <set>
#include <cassert>
#include <bitset>

using namespace std;

char st[1000];

int main() {
	int cases;
	scanf("%d", &cases);
	for (int o = 0; o < cases; ++o) {
		scanf("%s", st);
		int n = strlen(st), ans = 0;
		while (n && st[n - 1] == '+') --n;
		for (int i = 0; i < n;) {
			int j = i;
			while (i < n && st[i] == st[j]) ++i;
			++ans;
		}
		printf("Case #%d: %d\n", o + 1, ans);
	}
	return 0;
}


