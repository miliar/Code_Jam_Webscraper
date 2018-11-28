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
char s[105];
int main() {
	int t, cas = 0;
	int n, i, j;
	int flag[10];
	scanf("%d", &t);
	while (t--) {
		cas++;
		scanf("%s", s);
		int ans = 0;
		for (i = 0; s[i]; ++i) {
			if (i == 0 || s[i] != s[i - 1]) {
				ans++;
			}
		}
		if (s[i - 1] == '+') {
			ans--;
		}
		printf("Case #%d: %d\n", cas, ans);
	}

}
