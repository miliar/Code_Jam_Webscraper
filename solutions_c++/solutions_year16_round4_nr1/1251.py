#include <bits/stdc++.h>
#define fst first
#define sec second
#define mp make_pair

using namespace std;

typedef long long LL;
typedef long double LD;

const int N = 201000;
const int fx[4] = {0, 1, 0, -1};
const int fy[4] = {1, 0, -1, 0};
int d[N];
bool f[211][211];
pair<int, int> q[N];

int getin() {
	char ch;
	while (!isdigit(ch = getchar()) && ch != '-');
	int x = ch == '-' ? 0 : ch - '0';
	int opt = ch == '-' ? -1 : 1;
	while (isdigit(ch = getchar())) x = x * 10 + ch - '0';
	return x * opt;
}

int main()
{
	freopen("flu.in", "r", stdin);
	freopen("flu.out", "w", stdout);
	
	int n = getin();
	int L = 1, R = 0;
	memset(f, 0, sizeof(f));
	for (int i = 1; i <= n; i++)
		for (int j = 1; j <= n; j++) {
			char ch;
			scanf(" %c", &ch);
			if (ch == '.') f[i][j] = 1;
			if (ch == '@') {
				q[++R] = mp(i, j);
				d[R] = 1;
			}
		}
		
 	int m = getin();
	for (; L <= R; L++) {
		int kx = q[L].fst;
		int ky = q[L].sec;
		//printf("(%d, %d) = %d\n", kx, ky, d[L]);
		if (d[L] >= m) continue;
		for (int i = 0 ; i < 4; i++) {
			int x = kx + fx[i];
			int y = ky + fy[i];
			if (f[x][y]) {
				f[x][y] = 0;
				q[++R] = mp(x, y);
				d[R] = d[L] + 1;
			}
		}
	}
	
	printf("%d\n", R);
	
	return 0;	
}
