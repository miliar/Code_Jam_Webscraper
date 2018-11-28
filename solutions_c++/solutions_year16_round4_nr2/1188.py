#pragma comment(linker, "/STACK:108777216")
#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <string>
#include <cmath>
#include <vector>
#include <deque>
#include <map>
#include <set>
#include <bitset>
#include <utility>
#include <algorithm>
using namespace std;

int const MAX_N = 1024;
int const MAX_CH = 100100;

char st[MAX_CH];
double p[MAX_N], pn[1<<20], py[1<<20];

double slow_calc(int n, int k, double *p) {
	double mx = 0.0;

	for (int i=0; i<(1<<n); i++) {
		py[i] = pn[i] = 1.0;
		for (int j=0; j<n; j++)
			if ((i>>j)&1) {
				py[i] *= p[j];
				pn[i] *= 1.0-p[j];
			}
	}

	for (int i=0; i<(1<<n); i++) {
		int cnt = 0;
		int x = i;
		while (x) {
			cnt += x&1;
			x>>=1;
		}

		double lc = 0;
		if (cnt == k) {
			for (int s=i; s; s=(s-1)&i) {
				int QQ = s, cnt_s = 0;
				while (QQ) {
					cnt_s += QQ&1;
					QQ>>=1;
				}
				if (cnt_s * 2 == k)
					lc += py[s] * pn[i-s];
			}
		}

		mx = max(mx,lc);
	}

	return mx;
}

int main() {
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);

	gets(st);
	int tst_count;
	sscanf(st,"%d",&tst_count);
	for (int qqq=1; qqq<=tst_count; qqq++) {
		printf("Case #%d:",qqq);

		//
		int n,k;
		scanf("%d%d",&n,&k);
		for (int i=0; i<n; i++) scanf("%lf",&p[i]);
		
		printf(" %.10lf",slow_calc(n,k,p));
		//

		printf("\n");
	}
	return 0;
}