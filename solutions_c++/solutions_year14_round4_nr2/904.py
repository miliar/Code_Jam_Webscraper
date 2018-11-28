#include <stdio.h>
#include <memory.h>
#include <algorithm>
using namespace std;

int n, a[1000], s[1000];
int idx[1000];

int sl[1000];

int d[1000][1000];

void renew (int& a, int b) { if (a<0 || a>b) a=b; }
int movecnt (int a, int b) { return abs (a-b); }

int main ()
{
	freopen ("input.txt", "r", stdin);
	freopen ("output.txt", "w", stdout);

	int t, tt=0;
	scanf ("%d", &t);
	while (t--) {
		scanf ("%d", &n);
		for (int i=0; i<n; i++) scanf ("%d", &a[i]);

		for (int i=0; i<n; i++) {
			s[i]=0;
			for (int j=0; j<n; j++) {
				if (a[i] > a[j])
					s[i]++;
			}
			idx[s[i]] = i;
		}

		for (int i=0; i<n; i++) {
			sl[s[i]] = 0;
			for (int j=0; j<i; j++) {
				if (s[i] > s[j])
					sl[s[i]] ++;
			}
		}

		memset (d, -1, sizeof(d));
		d[0][0] = 0;
		for (int su=0; su<n; su++) {
			for (int i=0; i<=su; i++) {
				int j = su-i;
				renew (d[i+1][j], d[i][j] + movecnt (idx[i+j] - sl[i+j] + i, i));
				renew (d[i][j+1], d[i][j] + movecnt (idx[i+j] - sl[i+j] + i, n-j-1));
			}
		}

		int ans=-1;
		for (int i=0; i<=n; i++)
			renew (ans, d[i][n-i]);

		printf ("Case #%d: %d\n", ++tt, ans);
	}

	return 0;
}
