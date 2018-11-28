/*
 * Author    : ben
 */
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <ctime>
#include <iostream>
#include <algorithm>
#include <queue>
#include <set>
#include <map>
#include <stack>
#include <string>
#include <vector>
#include <deque>
#include <list>
#include <functional>
#include <numeric>
#include <cctype>
using namespace std;
typedef long long LL;

int main() {
	int T;
	int k, c, s;
	scanf("%d", &T);
	for (int t = 1; t <= T; t++) {
		scanf("%d %d %d", &k, &c, &s);
		printf("Case #%d:", t);
		for (int i = 1; i <= k; i++) {
			printf(" %d", i);
		}
		putchar('\n');
	}
	return 0;
}


