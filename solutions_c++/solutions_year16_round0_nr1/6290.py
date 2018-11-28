#include <iostream>
#include <sstream>
#include <cstdio>
#include <cstdlib>
#include <ctime>
#include <cmath>
#include <cctype>
#include <cstring>
#include <string>
#include <vector>
#include <deque>
#include <queue>
#include <stack>
#include <list>
#include <map>
#include <set>
#include <algorithm>

using namespace std;

typedef long long LL;
typedef unsigned long long ULL;
typedef long double LD;

const int D = 10;

int vis[D];
int testCases, n;

int main() {
	scanf("%d", &testCases);
	for (int _ = 1; _ <= testCases; ++_) {
		memset(vis, 0, sizeof vis);
		scanf("%d", &n);
		if (n == 0) {
			printf("Case #%d: INSOMNIA\n", _);
		} else {
			int num = n;
			for (int visCnt = 0; visCnt < 10; num += n) {
				for (int tmp = num; tmp > 0; tmp /= 10) {
					int digit = tmp % 10;
					if (!vis[digit]) {
						vis[digit] = 1;
						++visCnt;
					}
				}
			}
			printf("Case #%d: %d\n", _, num - n);
		}
	}
	return 0;
}
