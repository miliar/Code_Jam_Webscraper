#include <string>
#include <vector>
#include <algorithm>
#include <iostream>
#include <sstream>
#include <fstream>
#include <map>
#include <set>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstring>
using namespace std;

const int N = 10010;

int a[N];
bool flag[N];

int main() {
	int T;
	scanf("%d\n", &T);
	for (int test = 1; test <= T; ++test) {
		int n, x;
		scanf("%d%d", &n, &x);
		for (int i = 0; i < n; ++i) {
			scanf("%d", &a[i]);
			flag[i] = false;
		}
		sort(a, a + n);
		int ans = 0;
		for (int i = 0; i < n; ++i) {
			if (flag[i]) continue;
			for (int j = n - 1; j > i; --j) {
				if (flag[j]) continue;
				if (a[i] + a[j] <= x) {
					flag[j] = true;
					break;
				}
			}
			++ans;
			flag[i] = true;
		}
		printf("Case #%d: %d\n", test, ans);
	}
	return 0;
}