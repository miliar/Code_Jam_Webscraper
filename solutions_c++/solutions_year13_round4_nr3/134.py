#include <algorithm>
#include <iostream>
#include <cstdlib>
#include <cstring>
#include <cassert>
#include <cstdio>
#include <string>
#include <vector>
#include <cmath>
#include <map>
#include <set>
using namespace std;

int z_codejam_testcase;
#define SIZE(A) ((int)(A).size())
#define PB push_back
#define MP make_pair
#define gout printf("Case #%d: ", ++z_codejam_testcase), cout

const int MAXN = 5000;

int n, t;
int a[MAXN], w[MAXN], q[MAXN], ans[MAXN];
vector <int> ed[MAXN];

void dfs(int u) {
 	w[u] = 1;
 	for (int i = 0; i < SIZE(ed[u]); i++)
 		if (!w[ed[u][i]])
 			dfs(ed[u][i]);
 		else
 			assert(w[ed[u][i]]==2);
 	w[u] = 2;
 	q[t++] = u;
}

void main2() {
	scanf("%d", &n);
	for (int i = 0; i < n; i++)
		scanf("%d", a+i);
	for (int i = 0; i < n; i++) ed[i].clear();
	for (int i = 0; i < n; i++) {
		for (int j = i-1; j >= 0; j--)
			if (a[i] == a[j]) {
			 	ed[j].PB(i);
			 	break;
			}
		int x = a[i]-1;
		for (int j = i-1; j >= 0; j--)
			if (a[j]==x) {
				ed[i].PB(j);
				x--;
			}
 	}

	for (int i = 0; i < n; i++)
		scanf("%d", a+i);
	for (int i = n-1; i >= 0; i--) {
		for (int j = i+1; j < n; j++)
			if (a[j] == a[i]) {
			 	ed[j].PB(i);
			 	break;
			}
		int x = a[i]-1;
		for (int j = i+1; j < n; j++)
			if (a[j]==x) {
			 	ed[i].PB(j);
			 	x--;
			}
	}
	for (int i = 0; i < n; i++) if (SIZE(ed[i]))
		sort(ed[i].begin(), ed[i].end());
	memset(w, 0, sizeof(w)); t = 0;
	for (int i = 0; i < n; i++)
		if (!w[i]) dfs(i);
	for (int i = 0; i < n; i++) ans[q[i]] = i+1;
	gout;
	for (int i = 0; i < n; i++)
		printf("%d%c", ans[i], " \n"[i+1==n]);
}




int main() {
	int test_num;
	scanf("%d", &test_num);
	for (; test_num--;) {
	 	main2();
	}


	return 0;
}
