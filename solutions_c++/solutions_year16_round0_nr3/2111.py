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

const int BITS = 32;
const int N = 1000007;
int cnt, pr[N], lp[N];

void sieve() {
	for (int i = 2; i < N; ++i) {
		if (lp[i] == 0) {
			lp[i] = i;
			pr[cnt++] = i;
		}
		for (int j = 0; j < cnt && pr[j] <= lp[i] && pr[j] * i < N; ++j) {
			lp[pr[j] * i] = pr[j];
		}
	}
}

int check(unsigned int mask, int base, int cnt) {
	for (int j = 0; j < cnt; ++j) {
		int prime = pr[j];
		int rem = 0;
		for (int i = 0; i < BITS; ++i) {
			int cur = (int)((mask >> i) & 1);
			rem = (base * rem + cur) % prime;
		}
		if (rem == 0) return prime;
	}
	return -1;
}

void solve() {
	printf("Case #1:\n");
	sieve();
	vector<pair<unsigned int, vector<int> > > ans;
	int need = (BITS == 16 ? 50 : 500);
	while(sz(ans) != need) {
		int mas[BITS];
		mas[0] = 1;
		mas[BITS - 1] = 1;
		for (int i = 1; i < BITS - 1; ++i) {
			mas[i] = rand() & 1;
		}
		unsigned int mask = 0;
		for (int i = 0; i < BITS; ++i) {
			if (mas[i]) mask |= ((unsigned int)1) << i;
		}
		bool ok = true;
		vector<int> cur;
		for (int base = 2; base <= 10; ++base) {
			int ret = check(mask, base, 100);
			if (ret == -1) {
				ok = false;
				break;
			}
			cur.pb(ret);
		}
		if (ok) ans.pb(mp(mask, cur));
	}
	for (auto p : ans) {
		auto mask = p.first;
		auto proof = p.second;
		for (int i = 0; i < BITS; ++i) {
			printf("%d", (int)((mask >> i) & 1));
		}
		for (auto x : proof) printf(" %d", x);
		printf("\n");
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