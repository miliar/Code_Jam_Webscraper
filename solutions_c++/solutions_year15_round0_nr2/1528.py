#define _CRT_SECURE_NO_WARNINGS
#include<iostream>
#include<string>
#include<math.h>
#include<queue>
#include<set>
#include<memory.h>
#include<algorithm>
#include<vector>
using namespace std;
typedef long long ll;
int t, n, a[1000];
pair<int,int> dp[1001][1001];
pair<int, int> get(int a, int b){
	if (dp[a][b].first != -1)
		return dp[a][b];
	int ret = a;
	int p = (a + b - 1) / b;
	dp[a][b] = make_pair(p - 1, b);
	for (int i = b - 1; i; --i)
		dp[a][b] = min(dp[a][b], get(a, i));
	return dp[a][b];
}
int solve(int mid){
	int ret = 0;
	priority_queue<int>q;
	for (int i = 0; i<n; ++i)
		q.push(a[i]);
	while (!q.empty()){
		int m = q.top();
		if (m <= mid)
			break;
		q.pop();
		pair<int, int> g = get(m, mid);
		ret += g.first;
		q.push(g.second);
	}
	return ret + q.top();
}
int main(){
	memset(dp, -1, sizeof(dp));
	freopen("B-large.in", "r", stdin);
	freopen("out.txt", "w", stdout);
	cin >> t;
	for (int k = 1; k <= t; ++k){
		cin >> n;
		int res = 1000;
		for (int i = 0; i < n; ++i)
			cin >> a[i];
		for (int i = 1; i <= 1000; ++i)
			res = min(res, solve(i));
		printf("Case #%d: %d\n", k, res);
	}
}