#include <stdio.h>
#include <string.h>
using namespace std;

const int N = 100 +10;

bool ans;

int i;
int m;
int n;
int tdnum;
int a[N][N];
int c[N];
int r[N];

int min(int a, int b) {return a < b ? a : b;}
int max(int a, int b) {return a > b ? a : b;}

void ri()
{
	int i;
	int j;
	
	memset(c, 0, sizeof(c));
	memset(r, 0, sizeof(r));
	scanf("%d%d", &m, &n);
	for (i = 0; i < m; i++)
		for (j = 0; j < n; j++)
		{
			scanf("%d", &a[i][j]);
			r[i] = max(r[i], a[i][j]);
			c[j] = max(c[j], a[i][j]);
		}
}

bool solve()
{
	int i;
	int j;
	
	for (i = 0; i < m; i++) for (j = 0; j < n; j++) if (a[i][j] < r[i] && a[i][j] < c[j]) return false;	
	return true;
}

void print()
{
	printf("Case #%d: ", i);
	if (ans) printf("YES\n"); else printf("NO\n");
}

int main()
{
	scanf("%d" ,&tdnum);
	for (i = 1; i <= tdnum; i++)
	{
		ri();
		ans = solve();
		print();
	}
	return 0;
}
