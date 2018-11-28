#include <iostream>
#include <fstream>
#include <cstdio>
#include <iomanip>
#include <cassert>
#include <climits>
#include <cmath>
#include <ctime>
#include <vector>
#include <string>
#include <cstring>
#include <list>
#include <queue>
#include <deque>
#include <stack>
#include <map>
#include <set>
#include <unordered_set>
#include <unordered_map>
#include <functional>
#include <algorithm>
using namespace std;
 
typedef pair<int, int> pii;
typedef long long llong;
typedef pair<llong, llong> pll;
typedef unsigned long long ullong;
#define mp make_pair
#define sqr(x) ((x)*(x))
const double PI = 3.14159265359;
#define y1 Y1
#define y0 alalal1231

bool p[50];
bool u[50];
int cnt[50];
int r, c, m;
int dx[] = {0, 1, 1, 1, 0, -1, -1, -1};
int dy[] = {1, 1, 0, -1, -1, -1, 0, 1};
vector<int> neighbor[50];

int getCnt(int i)
{
	int ret = 0;
	for (int j : neighbor[i])
		ret += p[j];
	return ret;
}

int check()
{
	int nul = -1;
	int cntNum = 0;
	for (int i = 0; i < r*c; ++i)
	{
		if (!p[i])
		{
			cnt[i] = getCnt(i);
			if (!cnt[i])
				nul = i;
			else
				++cntNum;
		}
	}
	if (nul == -1)
		return cntNum > 1 ? 0 : 2;
	else
	{
		memset(u, 0, sizeof u);
		queue<int> q;
		q.push(nul);
		u[nul] = true;
		int cntU = 1;
		while (!q.empty())
		{
			int cur = q.front();
			q.pop();
			if (!cnt[cur])
				for (int j : neighbor[cur])
					if (!u[j])
						q.push(j), u[j] = true, ++cntU;
		}
		return cntU == r*c - m ? 1 : 0;
	}
}

void brute(int r, int c, int m)
{
	for (int i = 0; i < m; ++i)
		p[i] = true;
	for (int i = m; i < r*c; ++i)
		p[i] = false;

	for (int i = 0; i < r*c; ++i)
	{
		neighbor[i].clear();
		int x = i / c, y = i % c;
		for (int j = 0; j < 8; ++j)
		{
			int nx = x + dx[j], ny = y + dy[j];
			if (nx < r && nx >= 0 && ny < c && ny >= 0)
				neighbor[i].push_back(nx * c + ny);
		}
	}

	bool hasAns = false;
	do
	{
		if (int ret = check())
		{
			hasAns = true;
			if (ret == 1)
			{
				bool wasNull = false;
				for (int i = 0; i < r*c; ++i)
				{
					if (p[i])
						putchar('*');
					else if (!cnt[i] && !wasNull)
						wasNull = true, putchar('c');
					else
						putchar('.');
					if (i % c == c-1)
						puts("");
				}
			}
			else
			{
				for (int i = 0; i < r*c; ++i)
				{
					if (p[i])
						putchar('*');
					else
						putchar('c');
					if (i % c == c-1)
						puts("");
				}
			}
			break;
		}
	} while (prev_permutation(p, p + r*c));
		
	if (!hasAns)
		puts("Impossible");
}

int main()
{
#ifdef MYLOCAL
    freopen("input.txt","rt",stdin);
    freopen("output.txt", "wt", stdout);
    clock_t beginTime = clock();
#endif

	int _T;
	scanf("%d", &_T);
	for (int _i = 1; _i <= _T; ++_i)
	{
		scanf("%d %d %d", &r, &c, &m);
		printf("Case #%d:\n", _i);
		brute(r, c, m);
	}

#ifdef MYLOCAL
    //cout << endl << "time: " << double(clock() - beginTime) / CLOCKS_PER_SEC;
#endif
    return 0;
}