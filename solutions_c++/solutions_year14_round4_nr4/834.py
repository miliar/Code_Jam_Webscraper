#include <stdio.h>
#include <string.h>
#include <algorithm>
#include <vector>
using namespace std;

int m, n;
char s[8][20];
int len[8];

int ans1, ans2;

vector<int> t[4];

void solve ()
{
	for (int i=0; i<n; i++) {
		if (t[i].empty()) return;
	}

	int cnt = 0;
	for (int i=0; i<n; i++) {
		for (int j=0; j<t[i].size(); j++) {
			int m = 0;
			for (int k=0; k<j; k++) {
				for (int l=0; l<len[t[i][j]] && l<len[t[i][k]]; l++) {
					if (s[t[i][j]][l] != s[t[i][k]][l])
						break;
					if (m < l+1)
						m = l+1;
				}
			}
			cnt += len[t[i][j]] - m;
		}
	}

	if (ans1 < cnt) {
		ans1 = cnt;
		ans2 = 1;
	}
	else if (ans1 == cnt)
		ans2++;
}

void getans (int x)
{
	if (x == m) {
		solve ();
		return;
	}
	for (int i=0; i<n; i++) {
		t[i].push_back (x);
		getans (x+1);
		t[i].pop_back ();
	}
}

int main ()
{
	freopen ("input.txt", "r", stdin);
	freopen ("output.txt", "w", stdout);

	int t, tt=0;
	scanf ("%d", &t);
	while (t--) {
		scanf ("%d%d", &m, &n);
		for (int i=0; i<m; i++)
			scanf ("%s", s[i]), len[i] = strlen(s[i]);

		ans1 = ans2 = 0;
		getans (0);
		printf ("Case #%d: %d %d\n", ++tt, ans1+n, ans2);
	}

	return 0;
}
