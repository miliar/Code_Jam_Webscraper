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
#include <string>
#include <cstring>
#include <queue>
using namespace std;

int arr[1010];
char str[1010];

int main() {
	freopen("A-large.in", "rt", stdin);
	freopen("out", "wt", stdout);

	int tests, cases = 1;
	scanf("%d" , &tests);
	while (tests--) {
		int n, num, cur;
		num = cur = 0;
		scanf("%d%s" , &n , str);
		for (int i = 0; i < n + 1; i++)
			arr[i] = str[i] - '0';
		for (int i = 0; i < n + 1; i++) {
			if (arr[i] && cur < i)
				num += (i - cur), cur += (i - cur);
			cur += arr[i];
		}
		printf("Case #%d: %d\n" , cases++ , num);
	}
	return 0;
}
