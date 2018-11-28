#include <iostream>
#include <string.h>
#include <string>
#include <algorithm>
#include <vector>

using namespace std;

const int MAXN = 110 * 510;

int m[510][110];
int q[MAXN], d[MAXN];

int dx[] = { -1, -1, -1, 0, 0, 1, 1, 1 };
int dy[] = { -1, 0, 1, -1, 1, -1, 0, 1 };

int Work()
{
	int W, H, B, x0, y0, x1, y1;
	cin >> W >> H >> B;
	int ww = W + 2;
	memset(m, 0, sizeof(m));
	for (int k = 0; k < B; k ++)
	{
		cin >> x0 >> y0 >> x1 >> y1;
		for (int i = x0; i <= x1; i ++)
			for (int j = y0; j <= y1; j ++)
				m[j][i] = 1;
	}
	memset(d, 0x7f, sizeof(d));
	int qh = 0, ql = 0;
	for (int i = 0; i < H; i ++)
		d[q[ql++]=i*ww] = 0;
	while (qh != ql)
	{
		int z = q[qh++];  qh %= MAXN;
		int row = z / ww, col = z % ww;
		for (int de = 0; de < 8; de ++)
		{
			int rr = row + dx[de], cc = col + dy[de];
			if (rr >= H || rr < 0 || cc < 0 || cc > W)
				continue;
			int nd = d[z] + 1 - m[row][col], zz = rr * ww + cc;
			if (nd < d[zz])
				d[q[ql++]=zz] = nd;
			ql %= MAXN;
		}
	}
	int ret = 0x7f7f7f7f;
	for (int i = 0; i < H; i ++)
		ret = min(ret, d[i*ww+W]);
	return ret;
}

int main()
{
	freopen("C-small-attempt2.in", "r", stdin);
	freopen("C-small-attempt2.out", "w", stdout);
	cin.sync_with_stdio(false);
	int T;
	cin >> T;
	for (int tt = 1; tt <= T; tt ++)
		cout << "Case #" << tt << ": " << Work() << endl;
	return 0;
}