#include <stdio.h>

int r;
int d[4][4];

int ch[17];

int main()
{
	freopen ("input.txt", "r", stdin);
	freopen ("output.txt", "w", stdout);

	int t, tt=0;
	scanf ("%d", &t);
	while (t--) {
		scanf ("%d", &r); r--;
		for (int i=0; i<4; i++) for (int j=0; j<4; j++) scanf ("%d", &d[i][j]);
		for (int i=1; i<=16; i++) ch[i] = 0;
		for (int j=0; j<4; j++) ch[d[r][j]] ++;

		scanf ("%d", &r); r--;
		for (int i=0; i<4; i++) for (int j=0; j<4; j++) scanf ("%d", &d[i][j]);
		for (int j=0; j<4; j++) ch[d[r][j]] ++;

		int ans=-1;
		for (int i=1; i<=16; i++) {
			if (ch[i] == 2) {
				if (ans==-1) ans = i;
				else if (ans!=-2) ans = -2;
			}
		}
		
		printf ("Case #%d: ", ++tt);
		if (ans==-1) printf ("Volunteer cheated!\n");
		else if (ans==-2) printf ("Bad magician!\n");
		else printf ("%d\n", ans);
	}

	return 0;
}
