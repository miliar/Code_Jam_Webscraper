#include <iostream>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <string>
#include <cstring>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <list>
#include <deque>

using namespace std;

int T, n;
double a[1005], b[1005];

int main () {
	freopen ("input.in", "r", stdin);
	freopen ("output.out", "w", stdout);
	scanf ("%d", &T);
	for (int c = 1; c <= T; c++) {
        pair <int, int> res;
        scanf ("%d", &n);
        for (int i = 0; i < n; i++) scanf ("%lf", &a[i]);
        for (int i = 0; i < n; i++) scanf ("%lf", &b[i]);
        sort(a, a + n); sort(b, b + n);
        for (int i = 0, j = 0, k = 0; i < n; i++, k++) {
            if (a[i] > b[j]) { res.first++; j++; }
            while (k < n && b[k] < a[i]) { k++; res.second++; }
        }
        printf ("Case #%d: %d %d\n", c, res.first, res.second);
	}
	return 0;
}
