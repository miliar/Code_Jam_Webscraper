#include <iostream>
#include <cstdio>
#include <cmath>
#include <algorithm>

using namespace std;

const int NMAX = 10000;
int T, n;
double a[NMAX], b[NMAX];

int main() {
#ifndef ONLINE_JUDGE
 freopen("input.txt", "r", stdin);
 freopen("output.txt", "w", stdout);
#endif
 cin >> T;
 for (int t = 0; t < T; t++) 
 {
	cin >> n;
	for (int i = 0; i < n; i++) 
	{
		cin >> a[i];
	}
    for (int i = 0; i < n; i++) 
	{
		cin >> b[i];
    }

    sort(a, a + n);
    sort(b, b + n);
	
	int l = 0, r = 0, kol1 = 0;

	while (l < n)
	{
		while (l < n && a[l] < b[r])
			l++;
		if (l < n) kol1++;
		r++;
		l++;
	}
	l = 0, r = 0;
	int kol2 = 0;
	while (r < n)
	{
		while (r < n && a[l] > b[r])
			r++;
		if (r < n) kol2++;
		r++;
		l++;
	}
	 printf("Case #%d: %d %d\n", t + 1, kol1, n - kol2);
 }
 return 0;
}