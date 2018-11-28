#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <queue>
#include <map>
#include <set>
#include <utility>
#include <stack>
#include <cstring>
#include <math.h>
#include<cstdio>
#include<deque>
#include<sstream>
using namespace std;
#define mp make_pair
#define eps 1e-6
int dx[] = { 0, 0, 1, -1, 1, 1, -1, -1 };
int dy[] = { 1, -1, 0, 0, 1, -1, 1, -1 };

int main() {
	freopen("a.txt", "rt", stdin);
	freopen("out.txt", "w", stdout);

	int t, n, tt = 1;
	scanf("%d", &t);
	while (t--) {
		scanf("%d", &n);
		long long res, tmp;
		printf("Case #%d: ", tt++);

		if (n == 0)
			puts("INSOMNIA");
		else {
			bool a[11] = { };
			bool g = 0;
			int m = 0;
			while (!g) {
				m++;
				res = (long long) n * (long long) m;
				tmp = res;
				while (res) {
					a[res % 10] = 1;
					res /= 10;
				}

				int cnt = 0;
				for (int i = 0; i < 10; i++)
					cnt += a[i];
				if (cnt == 10)
					g = 1;

			}
			printf("%lld\n", tmp);
		}
	}

	return 0;
}
