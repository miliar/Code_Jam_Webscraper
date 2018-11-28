#include <stdio.h>
#include <string.h>
#include <string>
#include <algorithm>
#include <iostream>
#include <vector>
#include <map>
#include <set>
#include <stdlib.h>
#include <time.h>
using namespace std;

int n, k;
double p[222];
int a[222];
double dp[222][222];
bool vis[222][222];

double tot (int ind, int y) {
	int e = k - y - ind;
	if (!e && !y) {
		return 1.0000;
	}
	if (vis[ind][y]) {
		return dp[ind][y];
	}
	double ret = 0.000;
	if (y) {
		ret += p[a[ind]] * tot(ind+1, y-1);
	}
	if (e) {
		ret += (1.0000-p[a[ind]]) * tot(ind+1, y);
	}
	vis[ind][y] = true;
	return dp[ind][y] = ret;;
}

int main () {
	freopen ("input.txt", "r", stdin);
	freopen ("output.txt","w",stdout);

	int t;
	scanf ("%d", &t);

	for (int it=1;it<=t;it++) {
		printf ("Case #%d: ", it);
		scanf ("%d %d", &n, &k);
		for (int i=0;i<n;i++) {
			cin >> p[i];
		}
		sort (p, p+n);
		double ret = 0;
		for (int s=0;s<=k;s++) {
			for (int i=0;i<s;i++) {
				a[i] = i;
			}
			for (int i=0;i<k-s;i++) {
				a[k-i-1] = n-i-1;
			}
			memset (vis, 0, sizeof(vis));
			ret = max (ret, tot(0, k/2));
		}
		printf ("%.10lf\n", ret);
	}

	return 0;
}