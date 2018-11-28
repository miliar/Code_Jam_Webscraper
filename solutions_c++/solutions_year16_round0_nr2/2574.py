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

int rev(int l, int r, char *st) {
	reverse(st + l, st + r + 1);
	for (int i = l; i <= r; ++i) {
		st[i] = (int)'+' + '-' - st[i];
	}
}

int calc(int l, int r, char *st) {
	while(r >= l && st[r] == '+') --r;
	if (r < l) return 0;
	if (st[l] == '-') rev(l, r, st);
	else {
		int i = l;
		while(st[i] == '+') ++i;
		rev(l, i - 1, st);
	}
	return calc(l, r, st) + 1;
}

void solve() {
	char st[107];
	int T;
	scanf("%d", &T);
	for (int test = 1; test <= T; ++test) {
		scanf("%s", st);
		int n = strlen(st);
		printf("Case #%d: %d\n", test, calc(0, n - 1, st)); 
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