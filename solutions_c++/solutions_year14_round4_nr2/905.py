#include <cstdio>
#include <algorithm>
#include <vector>

using namespace std;

int n;
vector<pair<int, int> > A;

bool ok() {
	bool mode = false;
	for (int i = 0; i < n-1; i++) {
		if (A[i+1].first < A[i].first) mode = true;
		if (A[i+1].first > A[i].first && mode) return false;
	}
	return true;
}

int ct() {
	int w = 0;
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < i; j++) if (A[j].second > A[i].second) w++;
	}
	return w;
}

void solve(int testcase) {
	scanf("%d", &n);
	A.clear(); A.resize(n);
	for (int i = 0; i < n; i++) {
		scanf("%d", &A[i].first);
		A[i].second = i;
	}
	sort(A.begin(), A.end());
	int ret = ct();
	while (next_permutation(A.begin(), A.end())) {
		if (ok()) ret = min(ret, ct());
	}
	printf("Case #%d: %d\n", testcase, ret);
}

int main() {
	int t; scanf("%d", &t);
	for (int i = 1; i <= t; i++) solve(i);
	return 0;
}