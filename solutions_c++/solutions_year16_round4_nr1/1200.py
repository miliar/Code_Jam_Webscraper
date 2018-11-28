#include <bits/stdc++.h>
using namespace std;

const int MOD = 1000000007;

int ss[1 << 15];
int a[3];
int f(int top, int l, int r) {	
	if (l == r) {
		a[top]--;
		if (a[top] < 0) return 0;
		ss[l] = top;
		return 1;
	}
	
	int mid = l + r >> 1;
	return f(top, l, mid) && f( (top + 1) % 3, mid + 1, r );
}

void Sort (string &s, int l, int r) {
	if (l == r) return;
	
	int mid = l + r >> 1;
	Sort (s, l, mid); Sort (s, mid + 1, r);
	if (s.substr(l, mid - l + 1) > s.substr(mid + 1, r - mid)) {
		for (int i=l; i<=mid; i++) {
			swap(s[i], s[mid+i-l+1]);
		}
	}
}

int Main () {
	int n, r, p, s;
	scanf ("%d %d %d %d", &n, &r, &p, &s);
	
	for (int i=0; i<3; i++) {
		a[0] = p;
		a[1] = r;
		a[2] = s;
		
		if (f(i, 0, (1 << n) - 1)) {
			string s;
			for (int i=0; i<1<<n; i++) {
				if (ss[i] == 0) s += "P";
				else if (ss[i] == 1) s += "R";
				else s += "S";
			}
			
			Sort (s, 0, (1 << n) - 1);
			cout << s << endl;
			return 0;
		}
	}
	
	printf ("IMPOSSIBLE\n");
	return 0;
}

int main () {
	freopen ("A-large (2).in", "r", stdin);
	freopen ("A-large (2).out", "w", stdout);

	int t;
	scanf ("%d", &t);
	for (int tc=0; tc<t; tc++) {
		printf ("Case #%d: ", tc + 1);
		Main();
	}
	return 0;
}