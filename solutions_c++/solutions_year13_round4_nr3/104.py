#include <stdio.h>

#include <memory.h>

int n;
int a[2010], b[2010];
int m1[2010], m2[2010];
int m1last[2010], m2first[2010];

#include <algorithm>
using namespace std;

int ans[2010];

int main()
{
	freopen ("c.in", "r", stdin);
	freopen ("c.out", "w", stdout);

	int t, tt=0;
	scanf("%d", &t);
	while (t--) {
		scanf ("%d", &n);
		for (int i=0; i<n; i++) scanf ("%d", &a[i]);
		for (int i=0; i<n; i++) scanf ("%d", &b[i]);

		memset(ans, 0, sizeof(ans));

		for (int i=0; i<n; i++) {
			memset(m1last, 0, sizeof(m1last));
			memset(m2first, 0, sizeof(m2first));

			for (int j=0; j<n; j++)
				m1[j] = max(j==0 ? 0 : m1[j-1], !ans[j] ? 0 : a[j]);
			for (int j=n-1; j>=0; j--)
				m2[j] = max(j==n-1 ? 0 : m2[j+1], !ans[j] ? 0 : b[j]);

			for (int j=0; j<n; j++)
				if (!ans[j]) m1last[a[j]] = j;
			for (int j=n-1; j>=0; j--)
				if (!ans[j]) m2first[b[j]] = j;

			for (int j=0; j<n; j++) {
				if (!ans[j] && m1[j]+1 == a[j] && m2[j]+1 == b[j] &&
					(m1last[a[j]] == j && m2first[b[j]] == j)) {
					ans[j] = i+1;
					break;
				}
			}
		}

		printf ("Case #%d:", ++tt);
		for (int i=0; i<n; i++) printf (" %d", ans[i]);
		printf ("\n");
	}

	return 0;
}
