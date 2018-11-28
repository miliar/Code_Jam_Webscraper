#include <bits/stdc++.h>
using namespace std;
#define inf 1e9
#define s1(x) scanf("%d", &x)
#define ms0(x) memset(x, 0, sizeof(x))

int v[10];

int find(int* v) {
	int i = 9;
	while (i && !v[i]) --i;
	if (i <= 3) return i;
	if (v[i] > i) return i;
	
	int n[10];
	int j = 1;
	ms0(n);
	while (j < i) {
		n[j] = v[j];
		++j;
	}
	int ans = i;
	int mid = i/2;
	while (mid >= 2) {
		int a = i-mid;
		int b = mid;
		n[a] += v[i];
		n[b] += v[i];
		int j = ans;
		ans = min(ans, v[i] + find(n));
		// if (ans != j) cout << "cut " << ans << endl;
		
		n[a] -= v[i];
		n[b] -= v[i];
		--mid;
	}
	return ans;	
}


int main() {
	int t; s1(t);
	int n, a, b, c;
	ms0(v);
	for (int i = 1; i <= t; ++i) {
		s1(n);
		ms0(v);
		// s.clear();
		while (n--) {
			s1(a);
			v[a] += 1;
		}
		a = find(v);
		cout << "Case #" << i << ": " << a << endl;
	}
	
	return 0;
}