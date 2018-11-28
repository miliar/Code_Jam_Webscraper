#include <cstdio>
#include <string>
#include <cmath>
#include <vector>
#include <algorithm>
#include <set>
#include <map>
#include <iostream>
#include <queue>
#include <list>
#include <ctime>

using namespace std;

#define mp make_pair
#define sqr(a) ((a)*(a))

typedef long double ld;
typedef long long ll;

const int MAXN = 5e3;
const int INF = 1e9 + 7;

bool used[10];
int usedcnt;

void read_num(int n)
{
	do {
		if (!used[n % 10]) {
			used[n % 10] = 1;
			++usedcnt;
		}
		n /= 10;
	} while (n > 0);
}

void solve(int n)
{
	fill(used, used + 10, 0);
	usedcnt = 0;

	if (n == 0) {
		printf("INSOMNIA\n");
		return;
	}

	int cur = 0;
	while (usedcnt < 10) {
		cur += n;
		read_num(cur);
	}

	printf("%d\n", cur);
}

int main()
{
#ifndef ONLINE_JUDGE
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif

	int t;
	scanf("%d", &t);
	for (int i = 0; i < t; ++i) {
		int n;
		scanf("%d", &n);
		printf("Case #%d: ", i+1);
		solve(n);
	}

	return 0;
}