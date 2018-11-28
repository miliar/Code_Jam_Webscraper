#define _CRT_SECURE_NO_DEPRECATE

#include <string>
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
#include <memory.h>
#include <assert.h>

using namespace std;

#define pb push_back
#define pf push_front
#define mp make_pair
#define fi(a, b) for(int i=a; i<=b; i++)
#define fj(a, b) for(int j=a; j<=b; j++)
#define fo(a, b) for(int o=a; o<=b; o++)
#define fdi(a, b) for(int i=a; i>=b; i--)
#define fdj(a, b) for(int j=a; j>=b; j--)
#define fdo(a, b) for(int o=a; o>=b; o--)
#define ZERO(x) memset(x, 0, sizeof(x))
#define COPY(x,y) memcpy(x, y, sizeof(y))
#define LEN(x) (int)x.length()
#define SIZE(x) (int)x.size()

typedef long long int64;

int testq;
int test;

#define MAX 1100

int n;
int a[MAX];

void Read() {
	scanf("%d", &n);
	fi(1, n) {
		scanf("%d", &a[i]);
	}
}

int calc(int x) {
	int res = 0;
	fi(1, n) {
		res += (a[i] - 1) / x;
	}
	return res + x;
}

void Solve() {
	int ans = 1000000000;
	fi(1, 1000) {
		ans = min(ans, calc(i));
	}
	printf("%d\n", ans);
}

int main(int argc, char **argv) {
	if (argc == 1) {
		freopen("input.txt","r",stdin);
	} else {
		freopen(argv[1], "r",stdin);
	}
	freopen("output.txt","w",stdout);
	scanf("%d", &testq);
	for (test = 1; test <= testq; test++) {
		Read();
		printf("Case #%d: ", test);
		Solve();
		fflush(stdout);
	}
	return 0;
}
