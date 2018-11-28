#include <cstdio>
#include <iostream>
#include <cstring>
#include <map>
#include <queue>
#include <cstdlib>
#include <cmath>
#include <algorithm>
#define FOR(i, x, y) for(int i = x; i <= y; ++i)
#define rFOR(i, x, y) for(int i = x; i >= y; --i)
#define MS(a, b) memset(a, b, sizeof(a))
using namespace std;
const int maxn = 4200;
int t, n, tmp, all, a[3], b[3], c[3][maxn];
bool vis[3];
bool check1(int n,int m)
{
	if(m == -2) return true;
	FOR(i, 1, all)
	{
	    if(c[n][i] < c[m][i]) return true;
	    if(c[n][i] > c[m][i]) return false;
	}
	return true;
}
int get(int x)
{
	if (!x) return 1;
	if (x == 1) return 2;
	if (x == 2) return 0;
	return -1;
}
bool check2(int l, int mid, int r)
{
	FOR(i, 1, mid - l + 1)
	{
	    if(c[tmp][l + i - 1] > c[tmp][mid + i]) return true;
	    if(c[tmp][l + i - 1] < c[tmp][mid + i]) return false;
	}
	return false;
}
bool check3()
{
    FOR(i, 1, all) ++b[c[tmp][i]];
    FOR(i, 0, 2) if(b[i] == a[i]) return false;
    return true;
}
void make(int l, int r, int x, int depth)
{
	if(!depth)
	{
		c[tmp][l] = x;
		return;
	}
	int temp = get(x);
	int mid = (l + r) >> 1;
	make(l, mid, x, depth - 1);
	make(mid + 1, r, temp, depth - 1);
	if(check2(l, mid, r)) FOR(i, l, mid) swap(c[tmp][i], c[tmp][i + (1 << (depth - 1))]);
}
int main()
{
	scanf("%d", &t);
	FOR(m, 1, t)
	{
	    printf("Case #%d: ", m);
	    MS(vis, 0);
	    scanf("%d%d%d%d", &n, &a[1], &a[0], &a[2]);
	    all = 1 << n;
	    FOR(i, 0, 2)
	    {
	        MS(b, 0);
	        tmp = i;
	        make(1, all, i, n);
	        if(check3()) vis[i] = true;
	    }
	    tmp = -2;
	    FOR(i, 0, 2) if(vis[i] && check1(i, tmp))
	    {
	        tmp = i;
	        break;
	    }
	    if(tmp == -2)
        {
            printf("IMPOSSIBLE\n");
            continue;
        }
        FOR(i, 1, all)
        {
            if(c[tmp][i] == 0) printf("P");
            else if(c[tmp][i] == 1) printf("R");
            else printf("S");
        }
        printf("\n");
	}
	return 0;
}
