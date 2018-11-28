#include<ctime>
#include<cassert>
#include<stdio.h>
#include<string>
#include<algorithm>
#include<iostream>
#include<vector>
#include<set>
#include<map>
#include<queue>
#include<list>
#include<memory.h>
#include<unordered_map>
using namespace std;

typedef long long ll;
typedef vector<int> vi;
typedef long double ld;
typedef pair<int, int> pii;

const int inf = 1e9+7;
const ld eps = 1e-16;
const int maxn = 3500;

int simulate(vi &a, int k) {
	priority_queue<int> q(begin(a), end(a));
	int res = 0;
	while (1) {
		if (q.empty()) break;
		int d = q.top();
		if (d <= k) break;
		q.pop();
		++res;
		q.push(k);
		q.push(d - k);
	}
	if (!q.empty()) res += q.top();
	
	return res;
}

int main(){
#ifdef TANAS_JUDGE
	freopen("in", "r", stdin);
	freopen("out", "w", stdout);
#endif
	int T;
	cin >> T;
	for (int t = 0; t < T; ++t) {
		int n;
		cin >> n;
		vi a(n);
		int mx = 0;
		for (int i = 0; i < n; ++i) {
			scanf("%d", &a[i]);
			mx = max(mx, a[i]);
		}
		int res = mx;
		for (int i = 2; i <= mx; ++i) {
			res = min(res, simulate(a, i));
		}
		
		printf("Case #%d: %d\n", t + 1, res);
	}

	return 0;
}

