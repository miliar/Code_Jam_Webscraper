#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <algorithm>
using namespace std;
const int MAXN = 1001;

bool cmp1(double a, double b) { return a < b; }
bool cmp2(double a, double b) { return a > b; }

double naomi[MAXN], ken[MAXN];
bool vis[MAXN];
int war(int n)
{
	sort(naomi, naomi+n, cmp2);//decrese
	sort(ken, ken+n, cmp1);//increase
	memset(vis, false, sizeof(vis));
	int ret = 0;
	for (int i=0; i<n; i++) {
		bool flag = false;
		for (int j=0; j<n; j++) {
			if (!vis[j] && ken[j]>naomi[i]) {
				flag = true;
				vis[j] = true;
				break;
			}
		}
		if (!flag) {
			for (int j=0; j<n; j++) {
				if (!vis[j]) {
					vis[j] = true;
					ret++;
					break;
				}
			}
		}
	}
	return ret;
}

int dwar(int n)
{
	sort(naomi, naomi+n, cmp1);//increase
	sort(ken, ken+n, cmp2);//decrease
	memset(vis, false, sizeof(vis));
	int ret = 0;
	for (int i=0; i<n; i++) {
		bool flag = false;
		for (int j=0; j<n; j++) {
			if (!vis[j] && naomi[j]>ken[i]) {
				flag = true;
				vis[j] = true;
				ret++;
				break;
			}
		}
		if (!flag) {
			for (int j=0; j<n; j++) {
				if (!vis[j]) {
					vis[j] = true;
					break;
				}
			}
		}
	}
	return ret;
}

int main()
{
	freopen("D--large.in", "r", stdin);
	freopen("D--large.out", "w", stdout);
	int T, N;
	scanf("%d", &T);
	for (int t=1; t<=T; t++) {
		scanf("%d", &N);
		for (int i=0; i<N; i++) scanf("%lf", &naomi[i]);
		for (int i=0; i<N; i++) scanf("%lf", &ken[i]);
		int ans_war = war(N);
		int ans_dwar = dwar(N);
		printf("Case #%d: %d %d\n", t, ans_dwar, ans_war);
	}
	return 0;
}