//venk13
#include <vector>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <algorithm>
#include <utility>
#include <sstream>
#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstring>
#include <fstream>
#include <cassert>
 
using namespace std;
 
#define sz(a) (int)(a.size())
#define len(a) (int)(a.length())
#define pb push_back
#define mp make_pair

int a[10000], b[10000], DP[1000][1000], n;

int dp(int front, int back) {
	if(front > back) return 0;
	int i = n - (back - front + 1);
	int &ret = DP[front][back];
	if(ret != -1) return ret;
	ret = 0;
	if(a[i] > b[front]) {
		ret = 1 + dp(front + 1, back);
	}
	else {
		if(a[i] < b[back])
			ret = dp(front + 1, back);
		else {
			ret = max(ret, dp(front + 1, back));
			ret = max(ret, 1 + dp(front, back - 1));
		}
	}
	return ret;
}

int main() {
	freopen("D-large.in", "r", stdin);
	freopen("output2.txt", "w", stdout);
	int t, cas = 1; scanf("%d", &t);
	while(t--) {
		printf("Case #%d: ", cas++);
		int zz; scanf("%d", &n);
		for(int i = 0; i < n; i++)
			scanf("%d.%d", &zz, a + i);
		for(int j = 0; j < n; j++)
			scanf("%d.%d", &zz, b + j);
		sort(a, a + n); sort(b, b + n, greater <int>());
		int y, z = 0;
		memset(DP, -1, sizeof DP);
		y = dp(0, n - 1);
		sort(b, b + n);
		int bptr = 0;
		for(int i = 0; i < n; ++i, ++bptr) {
			while(bptr < n && b[bptr] < a[i]) {
				++bptr;
				++z;
			}
			if(bptr == n) break;
		}
		printf("%d %d\n", y, z);
	}
	return 0;
}