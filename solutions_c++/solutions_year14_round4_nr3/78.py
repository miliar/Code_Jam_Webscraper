#include <cstdlib>
#include <cctype>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <vector>
#include <string>
#include <iostream>
#include <sstream>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <fstream>
#include <numeric>
#include <iomanip>
#include <bitset>
#include <list>
#include <stdexcept>
#include <functional>
#include <utility>
#include <ctime>
using namespace std;

#define PB push_back
#define MP make_pair

const double pi = acos(-1.);
const double eps = 1e-6;
/*
const int fx[4] = {1, -1, 0, 0};
const int fy[4] = {0, 0, 1, -1};

int bl[610000], la[610000], last[610000], pr[1010000], up[1010000], ro[1010000];
int sourse, target;
int ans, delta, now, T, n, w, h;
int index(int a, int b, int c)
{
	return a * h * 2 + b * 2 + c;
}
bool dfs(int a)
{
//	cout << a << endl;
	bl[a] = ans;
	if (a == target) {
		ans++;
		delta = 1;
		return 1;
	}
	if (la[a] != 0) {
		int tmp = last[a];
		do {
			if (bl[ro[tmp]] < ans && up[tmp] && dfs(ro[tmp])) {
				up[tmp] -= delta;
				up[tmp ^ 1] += delta;
				last[a] = tmp;
				return 1;
			}
			tmp = pr[tmp];
			if (tmp == 0) tmp = la[a];
		} while (tmp != last[a]);
	}
	return 0;
}
void ins(int a, int b, int c)
{
//	cout << a << ' ' << b << endl;
	now++;
	pr[now] = la[a];
	la[a] = now;
	ro[now] = b;
	up[now] = c;
	
	now++;
	pr[now] = la[b];
	la[b] = now;
	ro[now] = a;
	up[now] = 0;
}
int ax[1100], ay[1100], bx[1100], by[1100], blo[1100][1100];
*/
int ax[1100], ay[1100], bx[1100], by[1100];
int T, w, h, n, dist[1100][1100], d[1100];
int done[1100], X[10][10], Y[10][10];
int calc(int i, int j)
{
	int dist = 1992837465;
	X[0][0] = ax[i];
	X[0][1] = bx[i] + 1;
	X[1][0] = ay[i];
	X[1][1] = by[i] + 1;
	
	Y[0][0] = ax[j];
	Y[0][1] = bx[j] + 1;
	Y[1][0] = ay[j];
	Y[1][1] = by[j] + 1;
	for (int x = 0; x < 2; x++)
		for (int x2 = 0; x2 < 2; x2++)
			for (int y = 0; y < 2; y++)
				for (int y2 = 0; y2 < 2; y2++)
					dist = min(dist, max(abs(X[0][x] - Y[0][y]), abs(X[1][x2] - Y[1][y2])));
	for (int x = 0; x < 2; x++)
		for (int x2 = 0; x2 < 2; x2++)
			if (ax[j] <= X[0][x] && X[0][x] <= bx[j] + 1)
				for (int y2 = 0; y2 < 2; y2++)
					dist = min(dist, abs(X[1][x2] - Y[1][y2]));
	for (int y = 0; y < 2; y++)
		for (int y2 = 0; y2 < 2; y2++)
			if (ax[i] <= Y[0][y] && Y[0][y] <= bx[i] + 1)
				for (int x2 = 0; x2 < 2; x2++)
					dist = min(dist, abs(X[1][x2] - Y[1][y2]));
	for (int x = 0; x < 2; x++)
		for (int x2 = 0; x2 < 2; x2++)
			if (ay[j] <= X[1][x2] && X[1][x2] <= by[j] + 1)
				for (int y = 0; y < 2; y++)
					dist = min(dist, abs(X[0][x] - Y[0][y]));
	for (int y = 0; y < 2; y++)
		for (int y2 = 0; y2 < 2; y2++)
			if (ay[i] <= Y[1][y2] && Y[1][y2] <= by[i] + 1)
				for (int x = 0; x < 2; x++)
					dist = min(dist, abs(X[0][x] - Y[0][y]));
//	cout << i << ' ' << j << ' ' << dist << endl;
	return dist;
}
int main()
{
	int ca = 0;
	freopen("c.in", "r", stdin);
	freopen("c.out", "w", stdout);
	for (scanf("%d", &T); T; T--) {
		scanf("%d%d%d", &w, &h, &n);
		for (int i = 0; i < n; i++) {
			scanf("%d%d%d%d", ax + i, ay + i, bx + i, by + i);
		}
		for (int i = 0; i < n; i++)
			for (int j = i + 1; j < n; j++)
				dist[i][j] = dist[j][i] = calc(i, j);
		for (int i = 0; i < n; i++)
			dist[n][i] = dist[i][n] = ax[i];
		for (int i = 0; i < n; i++)
			dist[n + 1][i] = dist[i][n + 1] = w - (bx[i] + 1);
		dist[n][n + 1] = dist[n + 1][n] = w;
		memset(d, -1, sizeof d);
		d[n] = 0;
		memset(done, 0, sizeof done);
		for (int i = 0; i <= n + 1; i++) {
			int best = 192837465, r = -1;
			for (int j = 0; j <= n + 1; j++)
				if (d[j] != -1 && d[j] < best && !done[j]) {
					best = d[j];
					r = j;
				}
			if (r == n + 1)
				break;
			done[r] = 1;
//			cout << r << ' ' << best << endl;
			for (int j = 0; j <= n + 1; j++)
				if (!done[j]) {
					if (d[j] == -1 || d[r] + dist[r][j] < d[j])
						d[j] = d[r] + dist[r][j];
				}
		}
		printf("Case #%d: %d\n", ++ca, d[n + 1]);
	}
}
