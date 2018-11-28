#define _CRT_SECURE_NO_WARNINGS

#include <stdio.h> 
#include <stdlib.h> 
#include <string.h> 
#include <memory.h> 
#include <math.h> 
#include <assert.h> 
#include <stack> 
#include <queue> 
#include <map> 
#include <set> 
#include <algorithm> 
#include <string> 
#include <functional> 
#include <vector> 
#include <deque> 
#include <utility> 
#include <bitset> 
#include <limits.h>  
#include <unordered_map>

using namespace std;
typedef long long ll;
typedef unsigned long long llu;
typedef double lf;
typedef unsigned int uint;
typedef long double llf;
typedef pair<int, int> pii;
typedef pair<ll, int> pli;

int TC, TCC;

const int N_ = 250;

void precalc() {
}

int N;

vector<int> D[N_];
unordered_map<ll, int> ren; int renn;
void init() {
	ren.clear(); renn = 0;
	for (int i = 0; i < N; i++) {
		D[i].clear();
	}
}

char str[20000];
int Chk[20000];

void solve() {
	scanf("%d\n", &N);
	for (int i = 0; i < N; i++) {
		gets(str);
		ll t = 0;
		for (int j = 0; str[j]; j++) {
			if ('a' <= str[j] && str[j] <= 'z') t = t * 26 + (str[j] - '0');
			else {
				if (t > 0) {
					int x;
					if (ren.count(t)) x = ren[t]; 
					else ren[t] = x = ++renn;
					D[i].push_back(x);
				}
				t = 0;
			}
		}
		if (t > 0) {
			int x;
			if (ren.count(t)) x = ren[t];
			else ren[t] = x = ++renn;
			D[i].push_back(x);
		}
	}

	int ans = renn;
	if (N <= 20) {
		for (int state = 0; state < 1 << (N - 2); state++) {
			int cnt = 0;
			for (int i = 0; i <= renn; i++) Chk[i] = 0;
			for (int i = 0; i < N; i++) {
				int w;
				if (i <= 1) w = i;
				else w = (state >> (i - 2)) & 1;
				for (auto e : D[i]) Chk[e] |= 1 << w;
			}
			for (int i = 1; i <= renn; i++) if (Chk[i] == 3) ++cnt;
			if (ans > cnt) ans = cnt;
		}
	}

	printf("Case #%d: %d\n", TCC, ans);
}

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	fprintf(stderr, "precalc start\n");
	precalc();
	fprintf(stderr, "precalc finished\n");

	scanf("%d", &TC);
	while (++TCC <= TC) {
		fprintf(stderr, "Case #%d: \n", TCC);
		fprintf(stderr, " - Init Start\n", TCC);
		init();
		fprintf(stderr, " - Init End\n", TCC);
		fprintf(stderr, " - Call Solve()\n", TCC);
		solve();
		fprintf(stderr, " - Printed!\n", TCC);
	}
	return 0;
}