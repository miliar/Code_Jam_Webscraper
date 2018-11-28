#include <set>
#include <map>
#include <stack>
#include <cmath>
#include <ctime>
#include <queue>
#include <string>
#include <vector>
#include <cstdio>
#include <sstream>
#include <cstring>
#include <climits>
#include <iostream>
#include <algorithm>
#define ff first
#define ss second
#define LL long long
#define pb push_back
#define mp make_pair
#define sqr(x) ((x) * (x))
#define PI 3.1415926535897
using namespace std;

int main() {
	int t, n, a[1005], maxx, ll, rr, mid, con, tmp, mm;
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);
	scanf("%d",  &t);
	for (int j = 1; j <= t; j++) {
		scanf("%d", &n); maxx = 0;
		for (int i = 0; i < n; i++) {
			scanf("%d", &a[i]);
			maxx = max(maxx, a[i]);
		}
		for (int k = 1; k <= maxx; k++) {
			con = 0; mm = 0;
			for (int i = 0; i < n; i++) {
				tmp = (a[i] / k) + (a[i] % k > 0);
				con += tmp - 1;
				mm = max(mm, (a[i]/tmp) + (a[i] % tmp > 0));
			}
			con += mm;
			if (con < maxx) maxx = con;
		}
		printf("Case #%d: %d\n", j, maxx);
	}
	return 0;
}
