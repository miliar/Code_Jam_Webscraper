#include <iostream>
#include <cstdio>
#include <algorithm>
#include <string.h>
#include <string>
#include <math.h>
#include <vector>
using namespace std;

const int maxr = 500 + 10;
const int maxc = 100 + 10;
const int maxL = maxr * maxc;
const int di[8] = {-1, -1, -1, 0, 0, 1, 1, 1};
const int dj[8] = {-1, 0, 1, -1, 1, -1, 0, 1};

int gr[maxr][maxc];
int L[maxL], d[maxL];
int w, h, B;

int sp()
{
	memset(d, -1, sizeof(d));
	int f = 0, r = 0;
		for (int i = 0; i != h; i++) {
		L[r++] = i * (w + 2);
		d[i * (w + 2)] = 0;
	}
	int x, y, u, new_u;
	while (f != r) {
		u = L[f++];
		if (f >= maxL) f -= maxL;
		for (int t = 0; t != 8; t++) {
			x = (u / (w+2)) + di[t];
			y = (u % (w+2)) + dj[t];
			if (x >= 0 && y >= 0 && x < h && y <= w) {
				new_u = x * (w+2) + y;
				if (d[new_u] == -1 || d[new_u] > d[u] + 1 - gr[u / (w+2)][u % (w+2)]) {
					d[new_u] = d[u] + 1 - gr[u / (w+2)][u % (w+2)];
					L[r++] = new_u;
					if (r >= maxL) r -= maxL;
				}
			}
		}
	}
	int ans = 2147483647;
	for (int i = 0; i != h; i++) {
		if (d[i * (w + 2) + w] < ans)
			ans = d[i * (w + 2) + w];
	}
	return ans;
}

int main()
{
	freopen("C-small-attempt1.in", "r", stdin);
	freopen("C.out", "w", stdout);
	int TextN, x0, y0, x1, y1;
	scanf("%d", &TextN);
	for (int TT = 1; TT <= TextN; TT++) {
		memset(gr, 0, sizeof(gr));
		scanf("%d%d%d", &w, &h, &B);
		for (int i = 1; i <= B; i++) {
			scanf("%d%d%d%d", &x0, &y0, &x1, &y1);
			for (int x = x0; x <= x1; x++)
				for (int y = y0; y <= y1; y++) {
					gr[y][x] = 1;
				}
		}
		printf("Case #%d: %d\n", TT, sp());

	}
}