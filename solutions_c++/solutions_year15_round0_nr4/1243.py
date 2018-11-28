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

int x, r, c;


int main() {
	int T;
	int cas = 0;
	scanf("%d", &T);
	while (T--) {
		scanf("%d%d%d", &x, &r, &c);
		printf("Case #%d: ", ++cas);
		if (x >= 7) {
			puts("RICHARD");
			continue;
		}
		if (x > 4) {
			int tmp;
			if (x & 1) tmp = (x - 1) / 2 + 1;
			else tmp = (x - 2) / 2 + 2;
			cout<<tmp<<endl;
			if (max(r, c) <= tmp + 1) {
				puts("RICHARD");
				continue;
			}
			if (x & 1) tmp = (x - 1) / 2 + 1;
			else tmp = (x - 2) / 2 + 1;
			cout<<tmp<<endl;
			if (min(r, c) <= tmp + 1) {
				puts("RICHARD");
				continue;
			}
		}
		if (x == 4) {
			if (max(r, c) < 4) {
				puts("RICHARD");
				continue;
			}
			if (min(r, c) <= 2) {
				puts("RICHARD");
				continue;
			}
		}
		if (x == 3) {
			if (max(r, c) < 3) {
				puts("RICHARD");
				continue;
			}
			if (min(r, c) == 1) {
				puts("RICHARD");
				continue;
			}
		}
		if (x == 2) {
			if (max(r, c) < 2) {
				puts("RICHARD");
				continue;
			}
		}
		if (r * c % x != 0) {
			puts("RICHARD");
			continue;
		}
		puts("GABRIEL");
		continue;
	}
	return 0;
}

