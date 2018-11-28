#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <algorithm>
#include <cstring>
#include <cstdio>
#include <queue>
#include <cassert>
#include <map>
#include <string>
#include <set>
#include <iomanip>
#include <ctime>
using namespace std;

#define FOR(i, n) for (int i = 0; i < (int)(n); ++i)
#define pb push_back
#define sz(v) (int)(v).size()
#define mp make_pair	
#define all(v) (v).begin(), (v).end()
typedef long double LD;
typedef long long LL;

int get_mask(int n) {
	int ret = 0;
	while(n) {
		ret |= (1 << (n % 10));
		n /= 10;
	}
	return ret;
}

int calc(int n) {
	int i, mask = 0;
	for (i = 1; ; ++i) {
		mask |= get_mask(n * i);
		if (mask == (1 << 10) - 1) return i * n;
	}
	return -1;
}

void solve() {
	int T;
	scanf("%d", &T);
	for (int test = 1; test <= T; ++test) {
		int n;
		scanf("%d", &n);
		printf("Case #%d: ", test);
		if (n == 0) puts("INSOMNIA");
		else printf("%d\n", calc(n));
	}
}

void testgen() {
    FILE *f = fopen("input.txt", "w");
    srand(time(0));
    fclose(f);
}

int main() {
#ifdef harhro94
    //testgen();
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
#else
    #define task "dream"
    //freopen(task".in", "r", stdin);
    //freopen(task".out", "w", stdout);
#endif

    solve();
/*
#ifdef harhro94
    cerr << "\ntime = " << fixed << setprecision(3) << clock() / (double)CLOCKS_PER_SEC << "s\n";
#endif*/
    return 0;
}