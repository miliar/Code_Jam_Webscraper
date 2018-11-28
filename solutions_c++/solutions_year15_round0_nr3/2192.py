//by allenlyh
#include <string.h>
#include <stdio.h>
#include <algorithm>
#include <iostream>
#include <stdlib.h>
#include <math.h>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <stack>
#include <complex>
#include <assert.h>

using namespace std;

#define sign(x) ((x)<-eps?-1:((x)>eps))
#define foreach(it,s) for (__typeof(s.begin()) it=s.begin();it!=s.end();it++)

typedef long long LL;
typedef pair<int, int> Pii;
typedef pair<LL, LL> PLL;
typedef complex<double> point;

const int maxn = 10000 + 10;
int n, m;
int grp[5][5] = {
	{0, 0, 0, 0, 0},
	{0, 1, 2, 3, 4},
	{0, 2, -1, 4, -3},
	{0, 3, -4, -1, 2},
	{0, 4, 3, -2, -1}
};
char st[maxn];
int p[maxn];

void init() {
	scanf("%d%d", &n, &m);
	scanf("%s", st);
	for (int i=0;i<n;i++) {
		if (st[i] == 'i') p[i] = 2;
		if (st[i] == 'j') p[i] = 3;
		if (st[i] == 'k') p[i] = 4;
	}
}

void work() {
	int pos = 0;
	int cur = 1;
	int op = 1;
	while (cur*op != 2 && pos < n * 4) {
		cur = grp[cur][p[pos % n]];
		if (cur < 0) op *= -1, cur *= -1;
		pos++;
	}
	if (cur*op != 2) {
		puts("NO");
		return;
	}
	cur = 1;
	op = 1;
	for (int i=0;i<n*4;i++) {
		cur = grp[cur][p[(pos+i) % n]];
		if (cur < 0) op *= -1, cur *= -1;
		if (cur * op == 3) {
			pos += i + 1;
			break;
		}
	}
	if (cur*op != 3) {
		puts("NO");
		return;
	}
	cur = 1;
	op = 1;
	for (int i=0;i<n*4;i++) {
		cur = grp[cur][p[(pos+i) % n]];
		if (cur < 0) op *= -1, cur *= -1;
		if (cur * op == 4) {
			pos += i + 1;
			break;
		}
	}
	if (cur*op != 4) {
		puts("NO");
		return;
	}
	if (LL(n) * m < pos) {
		puts("No");
		return;
	}
	cur = 1;
	op = 1;
	while ((LL(n) * m - pos) % (n * 4) != 0) {
		cur = grp[cur][p[pos % n]];
		if (cur < 0) op *= -1, cur *= -1;
		pos++;
	}
	if (cur * op != 1) {
		puts("NO");
		return;
	}
	puts("YES");
}

int main() {
	int T;
	int cas = 0;
	scanf("%d", &T);
	while (T--) {
		init();
		printf("Case #%d: ", ++cas);
		work();
	}
	return 0;
}

