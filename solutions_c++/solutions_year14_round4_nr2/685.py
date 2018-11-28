#include <cstdio>
#include <algorithm>
using namespace std;


struct S {
	int val;
	int idx;
	const bool operator< (const S& other) const {
		return val < other.val;
	}
};

S a[1005];
bool moved[1005];
int n;

int leftMove(int idx) {
	int ans = 0;
	while (idx != -1) {
		ans += !moved[idx];
		idx--;
	}
	return ans;
}

int rightMove(int idx) {
	int ans = 0;
	while (idx != n) {
		ans += !moved[idx];
		idx++;
	}
	return ans;
}

int f() {
	scanf("%d", &n);
	for (int i = 0; i < n; i++) {
		a[i].idx = i;
		scanf("%d", &a[i].val);
		moved[i] = false;
	}
	sort(a, a+n);
	int ans = 0;
	for (int i = 0; i < n; i++) {
		moved[a[i].idx] = true;
		int l = leftMove(a[i].idx);
		int r = rightMove(a[i].idx);
		ans += min(l, r);
	}
	return ans;
}

int main() {
	int t;
	scanf("%d", &t);
	for (int i = 0; i < t; i++) {
		printf("Case #%d: %d\n", i+1, f());
	}
}