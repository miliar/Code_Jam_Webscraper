#include <cstdio>
#include <algorithm>
#include <memory.h>
#include <time.h>
#include <cmath>
#include <cstdlib>
#include <functional>
#include <set>
#include <map>
#include <string>
#include <cstring>
#include <sstream>
#include <fstream>
#include <stack>
#include <queue>
#include <bitset>
#include <vector>
#include <iomanip>
#include <iostream>
#include <assert.h>

#define ALL(x) x.begin(), x.end()
#define fill(a, b) memset(a, b, sizeof(a))
#define abs(x) ((x)>0?(x):-(x))
#define sqr(x) (1ll*(x)*(x))
#define min(a,b) ((a)>(b)?(b):(a))
#define max(a,b) ((a)<(b)?(b):(a))
#define gcd(a,b) __gcd(a,b)
#define F first
#define S second
#define SS stringstream
#define CC(x) cout << x << endl
#define CCS(x) cout << x << " "
#define pw(x) (1ll<<(x))
#define pb push_back
#define mp make_pair
#define FIN freopen("1.in", "r", stdin)
#define FOUT freopen("1.out", "w", stdout)
#define FILE FIN; FOUT
#define SC(x) scanf("%d", &x)
#define PR(x) printf("%d\n", x)
#define PRS(x) printf("%d ", x)
#define bits(mask) __builtin_popcount(mask)
#define bit(mask, i) ((mask & pw(i-1)) > 0)
#define pii pair<int,int>
#define vi vector<int>
#define vii vector<pair<int,int> > 
#define forr(i, l, r) for (int i = l; i <= r; i++)
#define ford(i, r, l) for (int i = r; i >= l; i--)
#define SRD srand((int)time(NULL))
#define GC getchar()
#define PC(x) putchar(x)
#define left lft
#define right rght
#define log lg
#define y1 yyy1

typedef long long LL;
typedef unsigned long long ULL;
typedef double DD;
typedef long double LD;
typedef unsigned char UC;
typedef unsigned int UI;
typedef unsigned short US;

using namespace std;

struct answer
{
	int x, y, val[7][7];
};
answer ans[7][7][27];
bool has[27];
int cur_mask, a[7][7], c[7][7];
char ansc[7][7];

	inline void go(int i, int j, int n, int m)
	{
		if (i < 1 || i > n || j < 1 || j > m || a[i][j]) return;
		int cur = pw((i-1)*m + j - 1);
		if (cur&cur_mask) return;
		cur_mask |= pw((i-1)*m + j - 1);
		if (c[i][j] == 0) 
			forr(dx, -1, 1) forr(dy, -1, 1) go(i+dx, j+dy, n, m);
	}

int main(int argc, char * argv[])
{
	//ios_base::sync_with_stdio(0);
	FILE;
	forr(n, 1, 5) forr(m, 1, 5)
	{
		fill(has, 0);
		int all = pw(n*m)-1;
		forr(mask, 0, all)
		{
			fill(a, 0); fill(c, 0);
			int mines = bits(mask);
			if (has[mines]) continue;
			forr(i, 1, n) forr(j, 1, m) a[i][j] = bit(mask, (i-1)*m + j);
			forr(i, 1, n) forr(j, 1, m) forr(dx, -1, 1) forr(dy, -1, 1) c[i][j] += a[i+dx][j+dy];
			bool found = false;
			forr(i, 1, n) if (!found) forr(j, 1, m) if (!a[i][j])
			{
				cur_mask = mask;
				go(i, j, n, m);
				if (cur_mask == all) 
				{
					has[mines] = true;
					forr(ii, 1, n) forr(jj, 1, m) ans[n][m][mines].val[ii][jj] = a[ii][jj];
					ans[n][m][mines].x = i; ans[n][m][mines].y = j;
					found = true;
					break;
				}
			}
		}
	}
	int ttt;
	SC(ttt);
	forr(it, 1, ttt)
	{
		printf("Case #%d:\n", it);
		int n, m, x;
		SC(n); SC(m); SC(x);
		if (ans[n][m][x].x == 0)
		{
			CC("Impossible");
			continue;
		}
		forr(i, 1, n) forr(j, 1, m) ansc[i][j] = '.';
		forr(i, 1, n) forr(j, 1, m) if (ans[n][m][x].val[i][j]) ansc[i][j] = '*';
		ansc[ans[n][m][x].x][ans[n][m][x].y] = 'c';
		forr(i, 1, n) 
		{
			forr(j, 1, m) PC(ansc[i][j]);
			PC('\n');
		}
	}
	return 0;
}

