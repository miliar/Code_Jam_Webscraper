#include <stdio.h>
#include <algorithm>
#include <functional>
#include <map>
#include <string.h>


using namespace std;
typedef pair<int, int> par;

const int MAXN = 1002;
const int inf = 0x7fffffff;
int d[MAXN];
int n[MAXN];
int s[MAXN];
int dd[MAXN];
int dp[MAXN];
int ds[MAXN];
int p[MAXN];
int l[MAXN];

int h[1000];
const int hoff = 500;
int chkh(int p, int l, int str)
{
	for (int i = p; i < p+l; i++)
		if (h[i] < str) return 1;
	return 0;
}
void seth(int p, int l, int str)
{
	for (int i = p; i < p+l; i++)
		h[i] = max(h[i], str);
}

void doet()
{
	// updejt d (day of attack), w/e (location), s (strength)
	int sol = 0;
	memset(h, 0, sizeof(h));
	int N; scanf("%d", &N);
	for (int i = 0; i < N; i++) {
		int w, e;
		scanf("%d%d%d%d%d%d%d%d", d+i, n+i, &w, &e, s+i, dd+i, dp+i, ds+i);
		p[i] = w + hoff;
		l[i] = e - w;
	}
	
	bool doet = true;
	while (doet)
	{
		doet = false;
		int mind = inf;
		for (int i = 0; i < N; i++) if (n[i]>0) mind = min(mind, d[i]);
		for (int i = 0; i < N; i++)
		{
			if (d[i] > mind || n[i] == 0) continue;
			doet = true;
			sol += chkh(p[i], l[i], s[i]);
		}
		for (int i = 0; i < N; i++)
		{
			if (d[i] > mind || n[i] == 0) continue;
			seth(p[i], l[i], s[i]);
			d[i] += dd[i];
			p[i] += dp[i];
			s[i] += ds[i];
			n[i]--;
		}
	}
	printf("%d\n", sol);
}


int main()
{
	int t;
	scanf("%d", &t);
	for (int i = 0; i < t; i++)
	{
		printf("Case #%d: ", i+1);
		doet();
	}
	return 0;
}

