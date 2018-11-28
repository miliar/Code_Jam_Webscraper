# include <cstdio>
# include <cstring>

int x, y;
int a[5][5];
int b[5][5];
int is[17];

void read()
{
	scanf("%d", &x);
	for (int i = 1; i <= 4; ++i) for (int j = 1; j <= 4; ++j) scanf("%d", &a[i][j]);
	scanf("%d", &y);
	for (int i = 1; i <= 4; ++i) for (int j = 1; j <= 4; ++j) scanf("%d", &b[i][j]);
}
void solve()
{
	memset(is, 0, sizeof(is));
	for (int i = 1; i <= 4; ++i) {
		int t = a[x][i];
		is[t] = 1;
	}
	for (int i = 1; i <= 4; ++i) {
		int t = b[y][i];
		++ is[t];
	}
	int cnt = 0;
	for (int i = 1; i <= 16; ++i) if (is[i]>=2) ++cnt;
	if (cnt <= 0) printf("Volunteer cheated!\n");
	else if (cnt >=2) printf("Bad magician!\n");
	else {
		for (int i = 1; i <= 16; ++i) if (is[i]>=2) {
			printf("%d\n", i);
		}
	}
}

int main()
{
	freopen("A-small-attempt0.in", "r", stdin);
	freopen("outa.txt", "w", stdout);

	int T;
	scanf("%d", &T);
	for (int i = 1; i <= T; ++i) {
		read();
		printf("Case #%d: ", i);
		solve();
	}
	return 0;
}
