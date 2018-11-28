#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <set>
#include <map>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
using namespace std;

const int maxn = 10 + 2;

int n;
int x[maxn], y[maxn];
int a[maxn], b[maxn];
bool use[maxn];
bool cc[maxn][maxn];
bool ck[maxn][maxn][maxn][maxn];
double ret;

double cross(int a, int b)
{
	return x[a] * y[b] - x[b] * y[a];
}

double cross(int a, int b, int c)
{
	return (x[b] - x[a]) * (y[c] - y[a]) - (x[c] - x[a]) * (y[b] - y[a]);
}

int dot(int a, int b, int c)
{
	return (x[b] - x[a]) * (x[c] - x[a]) + (y[b] - y[a]) * (y[c] - y[a]);
}

void dfs(int h, double s)
{
	if (h == n) {
		bool flag = true;
		for (int j = 1; j + 1 < n - 1; ++j)
			if (!ck[a[j]][a[j + 1]][a[0]][a[n - 1]]) {
				flag = false;
				break;
			}
		if (!flag)
			return;
		s += cross(a[0], a[n - 1]);
		if (abs(s) > ret) {
			ret = abs(s);
			for (int i = 0; i < n; ++i)
				b[i] = a[i];
		}
			
	}else
		for (int i = 0; i < n; ++i)
			if (!use[i]) {
				a[h] = i;
				bool flag = true;
				for (int j = 0; j + 1 < h - 1; ++j)
					if (!ck[a[j]][a[j + 1]][a[h - 1]][i]) {
						flag = false;
						break;
					}
				if (!flag)
					continue;
				use[i] = true;
				dfs(h + 1, h == 0 ? s : s + cross(i, a[h - 1]));
				use[i] = false;
			}
}

void work()
{
	cin >> n;
	for (int i = 0; i < n; ++i)
		cin >> x[i] >> y[i];
	memset(cc, 0, sizeof(cc));
	for (int i = 0; i < n; ++i)
		for (int j = 0; j < n; ++j) if (i != j) {
			cc[i][j] = true;			
			for (int k = 0; k < n; ++k) if (i != k && j != k)
				if (cross(i, j, k) == 0 && dot(i, j, k) >= 0 && dot(j, i, k) >= 0) {
					cc[i][j] = false;
					break;
				}			
		}
	memset(ck, 0, sizeof(ck));
	for (int i = 0; i < n; ++i)
		for (int j = 0; j < n; ++j) if (i != j && cc[i][j])
			for (int k = 0; k < n; ++k) if (i != k && j != k)
				for (int l = 0; l < n; ++l) if (i != l && j != l && k != l && cc[k][l])
					ck[i][j][k][l] = cross(i, j, k) * cross(i, j, l) >= 0 || cross(k, l, i) * cross(k, l, j) >= 0;
	ret = 0;
	dfs(0, 0);	
	for (int i = 0; i < n; ++i)
		cout << b[i] << " ";	
}

int main()
{
    freopen("b1.in", "r", stdin);
    freopen("b1.out", "w", stdout);

    int t2;
    cin >> t2;
    for (int t1 = 1; t1 <= t2; ++t1) {
        printf("Case #%d: ", t1);
        work();
        printf("\n");
    }
    
    return 0;
}
