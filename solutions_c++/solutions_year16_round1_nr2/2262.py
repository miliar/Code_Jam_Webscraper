#include <algorithm>
#include <assert.h>
#include <iostream>
#include <string.h>
#include <memory.h>
#include <stdio.h>
#include <vector>
#include <time.h>
#include <string>
#include<bitset>
#include <queue>
#include <stack>
#include <cmath>
#include <set>
#include <deque>
#include <map>
using namespace std;
typedef long long ll;
const int N = 10+ 10;
int n;
vector<vector<int> > g;
int k;
bool cmp(const vector<int> x, const vector<int> y) {
	for (int i = k; i < x.size(); ++i)
		if (x[i] != y[i])
			return x[i] < y[i];
	return x.size() < y.size();
}
vector<int> ans;
bool check(int flag,int miss) {
	vector<vector<int> > t(n, vector<int>(n,-1));
	for (int i = 0; i < n; ++i)
		t[i] = g[i * 2 + flag];
	for (int i = 0; i < n; ++i)
		if(i*2+!flag!=miss)
		for (int j = 0; j < n; ++j)
			if (t[j][i] != g[i * 2 + !flag][j])
				return false;
	for (int i = 0; i < n; ++i)
		ans.push_back(t[i][miss / 2]);
	return true;
}
int main() {
#ifndef ONLINE_JUDGE
	freopen("B-small-attempt0.in", "r", stdin);
	freopen("B-small-attempt0.out", "w", stdout);
#endif
	int t, cas = 1;
	scanf("%d", &t);
	while (t--) {
		scanf("%d", &n);
		g.clear();
		g.resize(2*n-1);
		for (int i = 0; i < 2 * n - 1; ++i) {
			g[i].resize(n);
			for (int j = 0; j < n; ++j)
				scanf("%d", &g[i][j]);
		}
		k = 0;
		int miss = -1;
		for (int i = 0; i < 2*n-1; i+=2) {
			sort(g.begin()+i, g.end(),cmp);
			if (i+1==2*n-1 || g[i][k] != g[i + 1][k]) {
				miss = i+1;
				--i;
			}
			++k;
		}
		g.push_back(vector<int>(n, -1));
		for (int i = 2 * n - 1; i > miss; --i)
			swap(g[i], g[i - 1]);
		for (int i = (1 << n) - 1; i >= 0; ++i) {
			for (int j = 0; j < n; ++j)
				if (i&(1 << j))
					swap(g[j * 2], g[j * 2 + 1]);
			bool isrow = false;
			if (i&(1 << (miss / 2)))
				isrow = true;
			if (check(isrow,miss))
				break;
			for (int j = 0; j < n; ++j)
				if (i&(1 << j))
					swap(g[j * 2], g[j * 2 + 1]);
		}
		printf("Case #%d:", cas++);
		for (int i = 0; i < ans.size(); ++i)
			printf(" %d", ans[i]);
		puts("");
		ans.clear();
	}
	return 0;
}