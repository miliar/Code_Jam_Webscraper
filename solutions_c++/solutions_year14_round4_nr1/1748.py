#include <stdio.h>
#include <iostream>
#include <cstring>
#include <cstdlib>
#include <algorithm>
using namespace std;
const int N = 10005;
int s[N];
//bool vis[N];
int main(int argc, char **argv)
{
	//freopen("1.in", "r", stdin);
	//freopen("1.out", "w", stdout);
	int cases;
	scanf ("%d", &cases);
	for (int cas = 1; cas <= cases; cas++) {
		//memset(vis, 0, sizeof(vis));
		int n, x;
		scanf ("%d %d", &n, &x);
		for (int i = 0; i < n; i++) {
			scanf("%d", &s[i]);
		}
		sort(s, s + n);
		int ans = 0;
		int l = 0;
		int r = n - 1;
		while (l < r) {
			if (s[l] + s[r] <= x) {
				ans++;
				l++;
				r--;
			}
			else {
					r--;
			}
		}
		printf ("Case #%d: ", cas);
		
		printf ("%d\n", n - ans);
	}
	
	
	return 0;
}
