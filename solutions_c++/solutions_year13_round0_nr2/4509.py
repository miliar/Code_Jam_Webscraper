#include <cstdio>
#include <cstring>

int n,m,ans;
int a[100][100];
int b[100][100];

bool check () {
	for (int i = 0; i < n; ++i)
		for (int j = 0; j < m; ++j)
			if (a[i][j] != b[i][j]) return false;
	return true;
}

void work(int x,int y,int p,int q,int k) {
	int u = x;
	int v = y;
	while (u < n && v < m) {
		if (a[u][v] > k) return;
		u += p;
		v += q;
	}
	while (x < n && y < m) {
		b[x][y] = k;
		x += p;
		y += q;
	}
}
int main(int argc, char const *argv[])
{
	int T;
	scanf("%d",&T);
	for (int i = 0; i < T; ++i)
	{
		scanf("%d%d",&n,&m);
		for (int j = 0; j < n; ++j)
			for (int k = 0; k < m; ++k) {
				scanf("%d", &a[j][k]);
				b[j][k] = 100;
			}
		for (int k = 100; k > 0; --k) {
			for (int j = 0; j < n; ++j) {
				work(j,0,0,1,k);
			}
			for (int j = 0; j < m; ++j) {
				work(0,j,1,0,k);
			}
		}
		printf("Case #%d: ", i + 1);
		if (check()) {
			printf("YES\n");
		} else printf("NO\n");
	}
	return 0;
}