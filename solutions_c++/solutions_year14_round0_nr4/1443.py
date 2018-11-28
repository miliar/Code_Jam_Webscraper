#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<iostream>
#include<cmath>
using namespace std;

#define MAXN 1010

int Case;
int n;
double a[MAXN], b[MAXN];

int main()
{
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	scanf("%d", &Case);
	for (int tt = 1; tt <= Case; ++tt){
		scanf("%d", &n);
		for (int i = 0; i < n; ++i) scanf("%lf", &a[i]);
		for (int i = 0; i < n; ++i) scanf("%lf", &b[i]);
		sort(a, a + n);
		sort(b, b + n);
		int h = 0;
		int ans1, ans2;
		int i;
		for (i = 0; i < n; ++i){
			while (h < n)
				if (b[h] > a[i]) break;
				 else h++;
			if (h >= n) break;
			h++;
		}
		ans2 = n - i;
		ans1 = 0;
		int t = n-1;
		for (i = n-1; i >= 0; --i)
			if (a[t] > b[i]) { ans1++; t--; }
		printf("Case #%d: ", tt);
		printf("%d %d\n", ans1, ans2);
		}
	return 0;
	}
