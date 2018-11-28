#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <queue>

using namespace std;
int main() {
	int t, cas = 0;
	int n, i, j;
	int flag[10];
	scanf("%d", &t);
	while (t--) {
		cas++;
		scanf("%d", &n);
		memset(flag, 0, sizeof(flag));
		int flagcnt = 0;
		for (i = 1; i <= 100; ++i) {
			char s[100];
			sprintf(s, "%d", n * i);
			for (j = 0; s[j]; ++j) {
				if (flag[s[j] - '0'] == 0) {
					flag[s[j] - '0'] = 1;
					flagcnt++;
				}
			}
			if (flagcnt == 10) {
				break;
			}
		}
		if (i == 101) {
			printf("Case #%d: INSOMNIA\n", cas);
		} else {
			printf("Case #%d: %d\n", cas, i * n);
		}
	}

}
