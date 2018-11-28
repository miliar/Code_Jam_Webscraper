//By Lin
#include <cstdio>
#include <cstring>
#include <iostream>
#include <algorithm>
#include <map>
#include <set>
#include <bitset>
#include <cmath>
#include <string>
#include <cstdlib>
#include <vector>

#define X first
#define Y second
#define mp make_pair
#define sqr(x) ((x) * (x))
#define Rep(i, n) for(int i = 0; i<(n); i++)
#define foreach(it, n) for(__typeof(n.begin()) it = n.begin(); it != n.end(); it++)

using namespace std;
typedef long long LL;
typedef pair<int, int> pii;

#define esp 1e-8
#define N 1000100

int n, p, q, r, s, data[N];

bool pan(LL mid) {
	LL A[3];
	int k = 0;
	memset(A, 0, sizeof A);
	Rep(i, n) {
		bool flag = false;
		while (k < 3 && !flag) {
			if (A[k] + data[i] < mid) A[k] += data[i], flag = true;
			else k++;
		}
		if (k == 3) return false;
	}
	return true;
}

int main() {
	int cas, tt = 0;
	scanf("%d", &cas);
	while (cas --) {
		scanf("%d%d%d%d%d", &n, &p, &q, &r, &s);
		Rep(i, n) 
			data[i] = (i * 1ll * p + q) % r + s;
		LL tol = 0;
		Rep(i, n) tol += data[i];
		LL l = 1, r = tol, ans = 0;
		while (l <= r) {
			LL mid = l + r >> 1;
			if (pan(mid)) r = mid - 1;
			else l = mid + 1, ans = mid;
		}
		ans = tol - ans;
		printf("Case #%d: %.12f\n", ++tt, ans * 1.0 / tol);
	}
	return 0;
}

