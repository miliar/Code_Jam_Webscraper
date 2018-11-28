#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <limits.h>
#include <vector>
#include <stdlib.h>
#include <algorithm>
#include <memory.h>
#include <string.h>
#include <math.h>
#include <string>
#include <algorithm>
#include <functional>
#include <cassert>
#include <map>
#include <set>
#include <list>

using namespace std;
typedef long long lli;
typedef vector<int> vi;
typedef vector<lli> vli;
typedef pair<int, int> pii;
typedef vector<pii> vpii;
typedef long double ld;

const int INF = 0x3f3f3f3f;
const lli LINF = 0x3f3f3f3f3f3f3f3f;

//#define _LOCAL_DEBUG_
#ifdef _LOCAL_DEBUG_
#define eprintf(...) fprintf(stderr,__VA_ARGS__)
#else
#define eprintf(...) 
#endif

const int MAX = 10;
int n;
int digitsSeen[MAX] = { 0 };

void clear() {
	memset(digitsSeen, 0, sizeof(digitsSeen));
}

bool seenAll() {
	for (int i = 0; i < MAX; i++)
		if (!digitsSeen[i]) return false;
	return true;
}

void update(int n) {
	while (n) {
		int d = n % 10;
		digitsSeen[d] = 1;
		n /= 10;
	}
}

void read() {
	scanf("%d", &n);
}

int c = 0;
int mn = -1;
int solve() {
	int tn = n, tc = 0;
	for (tn = n; 1; tn += n) {
		update(tn);
		tc++;
		if (c < tc)
			c = tc, mn = n;
		if (seenAll()) break;
	} 
	return tn;
}

int main() {
	//freopen("out.txt", "w", stdout);
	//printf("%d\n", 1000001);
	//for (int i = 0; i <= 1000000; i++)
	//	printf("%d\n", i);
	//fclose(stdout);

#ifdef _LOCAL_VAN
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
#endif
	int t;
	scanf("%d", &t);
	for (int i = 1; i <= t; i++) {
		clear();
		read();
		printf("Case #%d: ", i);
		if (n) {
			int res = solve();
			printf("%d\n", res);
		}
		else 
			printf("INSOMNIA\n");
	}
	return 0;
}