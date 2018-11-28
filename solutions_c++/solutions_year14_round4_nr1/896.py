#include <stdio.h>
#include <algorithm>
using namespace std;

int s[10000];

int main()
{
	freopen ("input.txt", "r", stdin);
	freopen ("output.txt", "w", stdout);

	int t, tt=0;
	scanf ("%d", &t);
	while (t--) {
		int n, x;
		int ans=0;

		scanf ("%d%d", &n, &x);
		for (int i=0; i<n; i++)
			scanf ("%d", &s[i]);

		sort (s, s+n);
		for (int i=n-1; i>=0; i--) if (s[i]) {
			ans++;
			for (int j=i-1; j>=0; j--) if (s[j]) {
				if (s[i] + s[j] <= x) {
					s[j] = 0;
					break;
				}
			}
		}

		printf ("Case #%d: %d\n", ++tt, ans);
	}

	return 0;
}
