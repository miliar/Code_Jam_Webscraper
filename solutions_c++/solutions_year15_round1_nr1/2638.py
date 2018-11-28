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
const int MAXN = 10010;
int data[MAXN];

int main() {
	int T, N, M;
	scanf("%d", &T);
	for (int t = 1; t <= T; t++) {
		scanf("%d", &N);
		for (int i = 0; i < N; i++) {
			scanf("%d", &data[i]);
		}
		int first = 0, second = 0, max = 0, tmp;
		for (int i = 1; i < N; i++) {
			if (data[i - 1] > data[i]) {
				tmp = data[i - 1] - data[i];
				first += tmp;
				if (tmp > max) {
					max = tmp;
				}
			}
		}
		for (int i = 0; i < N - 1; i++) {
			if (data[i] >= max) {
				second += max;
			} else {
				second += data[i];
			}
		}
		printf("Case #%d: %d %d\n", t, first, second);
	}
	return 0;
}


