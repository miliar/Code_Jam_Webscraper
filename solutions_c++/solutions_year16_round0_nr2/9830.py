#include <cstdio>
#include <cmath>
#include <cstring>
#include <cstdlib>
#include <string>
#include <algorithm>
#include <set>
#include <queue>
#include <stack>
#include <map>
#include <vector>
#include <iostream>
#include <iomanip>
#include <complex>
#define MP make_pair
#define PUF push_front
#define POF pop_front
#define PUB push_back
#define POB pop_back
#define RESET(i, x) memset(i, x, sizeof(i))
using namespace std;
typedef long long LL;
typedef unsigned long long ULL;
typedef pair<int, int> PII;
typedef pair<LL, LL> PLL;

	int cases, cnt;
	char in[105];

int main() {
	freopen("in.txt", "r+", stdin);
	freopen("out.txt", "w+", stdout);
	scanf("%d", &cases);
	for (int tc = 1; tc <= cases; ++tc) {
		scanf("%s", in);
		printf("Case #%d: ", tc);
		int len = strlen(in);
		cnt = 0;
		for (int i = 0; i < len; ++i) {
			if (i > 0) {
				if (in[i] != in[i - 1])
					++cnt;
			}
		}
		if (in[len - 1] == '-')
			++cnt;
		printf("%d\n", cnt);
	}
	return 0;
}
/*
4
10 5
10 1
3 2
3 4
*/
