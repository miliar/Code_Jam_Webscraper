#include<stdio.h>
#include<vector>
#include<algorithm>
using namespace std;
typedef pair<int, int>pii;
char ans[100][100];
int match[10000];
int dx[4] = { -1,0,1,0 };
int dy[4] = { 0,-1,0,1 };
int main()
{
	freopen("c-large.in", "r", stdin);
	freopen("large.txt", "w", stdout);
	int data;
	scanf("%d", &data);
	for (int p = 1; p <= data; p++)
	{
		int mx, my;
		scanf("%d%d", &mx, &my);
		for (int i = 0; i < mx + mx + my + my; i++)match[i] = 0;
		for (int i = 0; i < mx; i++)for (int j = 0; j < my; j++)ans[i][j] = 'X';
		vector<pii>vec;
		for (int i = 0; i < mx + my; i++)
		{
			int za, zb;
			scanf("%d%d", &za, &zb);
			za--;
			zb--;
			match[za] = zb;
			match[zb] = za;
			if (za > zb)swap(za, zb);
			vec.push_back(make_pair(za, zb));
		}
		bool flag = true;
		for (int i = 0; i < vec.size(); i++)
		{
			for (int j = 0; j < vec.size(); j++)
			{
				if (vec[i].first < vec[j].first&&vec[j].first < vec[i].second&&vec[i].second < vec[j].second)
				{
					flag = false;
					break;
				}
			}
		}
		if (!flag)goto l01;
		int num = mx + mx + my + my;
		for (int i = 0; i < num / 2; i++)
		{
			for (int j = 0; j < num; j++)
			{
				if (match[j] == (j + i) % num)
				{
					int nx, ny, d;
					if (j < my)nx = -1, ny = j, d = 2;
					else if (j < mx + my)nx = j - my, ny = my, d = 1;
					else if (j < mx + my + my)nx = mx, ny = my - 1 - (j - mx - my), d = 0;
					else nx = mx - 1 - (j - mx - my - my), ny = -1, d = 3;
					int kx, ky;
					int t = match[j];
					if (t < my)kx = -1, ky = t;
					else if (t < mx + my)kx = t - my, ky = my;
					else if (t < mx + my + my)kx = mx, ky = my - 1 - (t - mx - my);
					else kx = mx - 1 - (t - mx - my - my), ky = -1;
					//printf("%d %d     %d %d  %d %d\n", j, match[j], nx, ny, kx, ky);
					for (;;)
					{
						//printf("%d %d\n", nx, ny);
						nx += dx[d], ny += dy[d];
						//printf("%d %d\n", nx, ny);
						if (nx == kx&&ny == ky)break;
						if (nx < 0 || nx >= mx || ny < 0 || ny >= my)
						{
							flag = false;
							break;
						}
						if (ans[nx][ny] == 'X')
						{
							if (d % 2 == 0)ans[nx][ny] = '\\';
							else ans[nx][ny] = '/';
							d = (d + 1) % 4;
						}
						else
						{
							if ((ans[nx][ny] == '\\'&&d % 2 == 0) || (ans[nx][ny] == '/'&&d % 2 == 1))d = (d + 1) % 4;
							else d = (d + 3) % 4;
						}
					}
				}
			}
		}
	l01:;
		printf("Case #%d:\n", p);
		if (flag)
		{
			for (int i = 0; i < mx; i++)
			{
				for (int j = 0; j < my; j++)
				{
					if (ans[i][j] == 'X')ans[i][j] = '/';
					printf("%c", ans[i][j]);
				}
				printf("\n");
			}
		}
		else printf("IMPOSSIBLE\n");
	}
}