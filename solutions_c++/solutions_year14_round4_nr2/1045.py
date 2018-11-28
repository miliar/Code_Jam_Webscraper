#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <vector>
#include <set>
#include <algorithm>
#include <queue>

#pragma warning(disable: 4996)

using namespace std;

int num[10000], n, tn[10000], dp[1008][1008];

void input() {
	scanf("%d", &n);
	for(int i = 0;i < n;i ++) scanf("%d", &num[i]);
}

void mycount(int *tn, int len, vector<pair<int,int> > &vp) {
	vp.clear();
	if(len <= 1) {
		if(len == 1) vp.push_back(make_pair(tn[0], 0));
		return ;
	}

	vector<pair<int,int> > vp1, vp2;
	int tlen = len/2;
	mycount(tn, tlen, vp1);
	mycount(tn+tlen, len-tlen, vp2);

	int i = 0, j = 0;
	while(i < (int)vp1.size()||j < (int)vp2.size()) {
		if(j >= (int)vp2.size()||i < (int)vp1.size()&&vp1[i].first < vp2[j].first) {
			vp.push_back(make_pair(vp1[i].first, vp1[i].second));
			++ i;
		}
		else {
			vp.push_back(make_pair(vp2[j].first, vp2[j].second + vp1.size() - i));
			++ j;
		}
	}
}

int solve_i(int p) {
	int max_p = 0;
	for(int i = 1;i < n;i ++) if(num[i] > num[max_p]) max_p = i;
	for(int i = 0;i < n;i ++) tn[i] = num[i];

	int res = 0;
	while(max_p > p) {
		swap(tn[max_p], tn[max_p-1]);
		++ res; -- max_p;
	}
	while(max_p < p) {
		swap(tn[max_p], tn[max_p+1]);
		++ res; ++ max_p;
	}

	vector<pair<int,int> > vp;
	mycount(tn, p, vp);
	for(int i = 0;i < (int)vp.size();i ++) res += vp[i].second;

	for(int i = p+1, j = n-1;i < j;i ++, j--) swap(tn[i], tn[j]);

	mycount(tn+p+1, n-p-1, vp);
	for(int i = 0;i < (int)vp.size();i ++) res += vp[i].second;

	return res;
}

void solve() {
	int res = n*n;
	for(int i = 0;i < n;i ++) {
		int tmp = solve_i(i);
		if(tmp < res) res = tmp;
	}

	printf(" %d\n", res);
}

int solve_1i(int p) {
	int max_p = 0;
	for(int i = 1;i < n;i ++) if(num[i] > num[max_p]) max_p = i;
	for(int i = 0;i < n;i ++) tn[i] = num[i];

	int res = 0;
	while(max_p > p) {
		swap(tn[max_p], tn[max_p-1]);
		++ res; -- max_p;
	}
	while(max_p < p) {
		swap(tn[max_p], tn[max_p+1]);
		++ res; ++ max_p;
	}

	for(int j = 0;j < p;j ++)
	for(int i = 0;i < p-1;i ++) if(tn[i] > tn[i+1]) {
		++ res;
		swap(tn[i], tn[i+1]);
	}

	for(int j = 0;j < n-p-1;j ++)
	for(int i = n-1;i > p+1;i --) if(tn[i] > tn[i-1]) {
		++ res;
		swap(tn[i], tn[i-1]);
	}

	return res;
}

void solve1() {
	int res = n*n;
	for(int i = 0;i < n;i ++) {
		int tmp = solve_1i(i);
		if(tmp < res) res = tmp;
	}

	printf(" %d\n", res);
}

int myabs(int x, int y) {
	if(x >= y) return x- y;
	return y-x;
}

void solve2() {
	vector<pair<int,int> > vp;
	for(int i = 1;i <= n;i ++) vp.push_back(make_pair(num[i], i));
	sort(vp.begin(), vp.end());

	dp[0][n+1] = 0;
	for(int i = 1;i <= n;i ++) {
		dp[0][n+1-i] = myabs(vp[i-1].second, n+1-i);
		dp[i][n+1] = myabs(vp[i-1].second, i);

		for(int j = 1;j < i;j ++) {
			dp[j][n+1-(i-j)] = dp[j-1][n+1-(i-j)] + myabs(vp[i-1].second, j);
			int tmp = dp[j][n+1-(i-j)+1] + myabs(vp[i-1].second, n+1-(i-j));
			if(tmp < dp[j][n+1-(i-j)]) dp[j][n+1-(i-j)] = tmp;

			//printf("%d %d %d\n", j, n+1-(i-j), dp[j][n+1-(i-j)]);
		}
	}

	int res = n*n;
	for(int j = 0;j <= n;j ++) if(dp[j][j+1] < res) res = dp[j][j+1];

	printf(" %d\n", res/2);
}

void solve4() {
	int b = 0, e = n-1;

	int res = 0;

	for(int i = 0;i < n;i ++) {
		int min_p = b;
		for(int j = b+1;j <= e;j ++) if(num[j] < num[min_p]) min_p = j;

		if(min_p - b < e - min_p) {
			while(min_p != b) {
				swap(num[min_p], num[min_p-1]);
				++ res;
				-- min_p;
			}
			++ b;
		}
		else {
			while(min_p != e) {
				swap(num[min_p], num[min_p+1]);
				++ res;
				++ min_p;
			}
			-- e;
		}
	}

	printf(" %d\n", res);
}

void solve3() {
	int res = n*n;
	for(int i = 0;i < (1<<n);i ++) {
		vector<int> left, right;
		for(int j = 0;j < n;j ++) {
			if(i&(1<<j)) left.push_back(num[j]);
			else right.push_back(num[j]);
		}

		sort(left.begin(), left.end());
		sort(right.begin(), right.end());

		int target[1000];

		for(int j = 0;j < (int)left.size();j ++) target[j] = left[j];
		for(int j = 0;j < (int)right.size();j ++) target[n-j-1] = right[j];

		//printf("x ");
		//for(int j = 0;j < n;j ++) printf("%d ", target[j]);
		//printf("\n");

		for(int j = 0;j < n;j ++) tn[j] = num[j];

		int tmp = 0;

		for(int j = 0;j < left.size();j ++) {
			int k;
			for(k = 0;k < n;k ++) if(tn[k] == target[j]) break;
			while(k > j) { swap(tn[k], tn[k-1]); ++ tmp; -- k; }
		}

		for(int j = 0;j < right.size();j ++) {
			int k;
			for(k = 0;k < n;k ++) if(tn[k] == target[n-1-j]) break;
			while(k < n-1-j) { swap(tn[k], tn[k+1]); ++ tmp; ++ k; }
		}

		if(tmp == 0) {
			//printf(" %d %d\n", left.size(), right.size());
			//for(int j = 0;j < n;j ++) printf("%d ", target[j]);
			//printf("\n");
		}

		if(tmp < res) {
			res = tmp;
			for(int j = 0;j < n;j ++) printf("%d ", target[j]);
			printf("\n");
		}
	}

	printf(" %d\n", res);
}


int main() {
	freopen("B-large.in", "r", stdin);
	freopen("output.txt", "w", stdout);
	int t;
	scanf("%d", &t);
	for(int cas = 1;cas <= t;cas ++) {
		input();
		printf("Case #%d:", cas);
		solve4();
		//solve3();
		//solve2();
		//solve();
		//solve1();
	}
	return 0;
}