#include <iostream>
#include <cstdio>
#include <string.h>
#include <string>
#include <algorithm>
#include <math.h>
#include <vector>
using namespace std;

const int mod = 1000002013;
const int maxm = 2000 + 10;
struct node
{
	int l, r, p;
} a[maxm];
int x[maxm * 2], n, m, t;
long long b[maxm * 2];

int calc(int x, int y, int p)
{
	return (long long)(y - x) * (2*n + x - y + 1) / 2 % mod * p % mod;
}

int get(int w)
{
	int left = 1, right = t, mid;
	while (left <= right) {
		mid = (left + right) / 2;
		if (x[mid] == w) return mid;
		if (x[mid] > w) right = mid - 1;
		else left = mid + 1;
	}
	return -1;
}

int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("A_L.out", "w", stdout);

	int TextN = 0, TT = 0, L, R;
	long long ans, oldans;
	scanf("%d", &TextN);
	while (TextN--) {
		oldans = ans = 0;
		scanf("%d%d", &n, &m);
		for (int i = 1; i <= m; i++) {
			scanf("%d %d %d", &a[i].l, &a[i].r, &a[i].p);
			x[i * 2 - 1] = a[i].l;
			x[i * 2] = a[i].r;
			oldans = (oldans + calc(a[i].l, a[i].r, a[i].p) ) % mod;
		}
		sort(x + 1, x + 1 + 2 * m);
		t = 0;
		for (int i = 1; i <= 2 * m; i++)
			if (i == 1 || x[i] != x[t]) {
				++t;
				x[t] = x[i];
			}
		
		memset(b, 0, sizeof(b));
		for (int i = 1; i <= m; i++) {
			int L = get(a[i].l), R = get(a[i].r);
			for (int j = L; j <= R - 1; j++) 
				b[j] += a[i].p;
		}
		
		while (1) {
			int k = -1;
			long long minf = -1;
			for (int i = 1; i <= t - 1; i++) 
			if (b[i] > 0 && (minf < 0 || b[i] < minf)) {
				minf = b[i];
				k = i;
			}
			if (k < 0) break;
			//cout << L << " " << R << endl;
			for (int i = k; i >= 1; i--)
				if (b[k] <= b[i]) L = i;
				else break;
			for (int i = k; i <= t - 1; i++)
				if (b[k] <= b[i]) R = i;
				else break;
			
			//cout << k << " " << minf << " " << L << " " << R << endl;
			for (int i = L; i <= R; i++) b[i] -= minf;
			
			ans = (ans + calc(x[L], x[R+1], minf)) % mod;
			//cout << x[L] << " " << x[R+1] << " " << minf << endl;
		}
		
		printf("Case #%d: %d\n", ++TT, (oldans - ans + mod) % mod);
	}
	return 0;
}
