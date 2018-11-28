#include <stdio.h>
#include <memory.h>
#include <string.h>

int n;
char data[30];
double d[1048576], c[1048576];

int main()
{
	freopen ("d.in", "r", stdin);
	freopen ("d.out", "w", stdout);

	int t, tt=0;
	scanf ("%d", &t);

	while (t--) {
		scanf ("%s", data);
		n=strlen(data);

		int s=0;
		for (int i=0; i<n; i++) if (data[i]=='X') s |= 1<<i;
		
		memset(c, 0, sizeof(c));
		memset(d, 0, sizeof(d));
		c[s] = 1;

		if (tt==12)
			tt=tt;

		for (int i=0; i<(1<<n); i++) if ((i&s) == s) {
			for (int j=0; j<n; j++) if ((i&(1<<j)) && ((i-(1<<j)) & s) == s) {
				for (int k=0; k<n; k++) {
					int l = (j+n-k)%n;
					if (i&(1<<l))
						d[i] += (d[i-(1<<j)] + c[i-(1<<j)] * (n-k)), c[i] += c[i-(1<<j)];
					else break;
				}
			}
		}

		printf ("Case #%d: %.10lf\n", ++tt, d[(1<<n)-1]/c[(1<<n)-1]);
	}

	return 0;
}
