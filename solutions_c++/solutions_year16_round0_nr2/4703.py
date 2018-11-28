#include <iostream>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <algorithm>
#include <vector>
#include <queue>
using namespace std;
#define maxn 111

char a[maxn];

void rev (int r) {//逆置(0,r)
	for (int i = 0; i <= r/2; i++) {
		swap (a[i], a[r-i]);
	}//cout << a << endl;
	for (int i = 0; i <= r; i++) {
		a[i] = (a[i] == '+' ? '-' : '+');
	}
}

void solve () {
	int ans = 0;
	int l = 0, r = strlen (a)-1;
	while (1) {
		l = 0;
		while (a[r] == '+' && r >= 0)
			r--;
		if (r < 0)
			break;
		if (a[l] == '+')
			ans++;
		while (a[l] == '+') {
			a[l] = '-';
			l++;
		}// cout << r << endl;
		rev (r); 
		ans++;
		//cout << a << endl; //while (1) {}
	} 
	printf ("%d\n", ans);
}

int main () {
	freopen ("in", "r", stdin);
	freopen ("out", "w", stdout);
	int t, kase = 0;
	scanf ("%d", &t);
	while (t--) {
		scanf ("%s", a);
		printf ("Case #%d: ", ++kase);
		solve ();
	}
	return 0;
}