#define _USE_MATH_DEFINES
#define _CRT_SECURE_NO_DEPRECATE

#include <iostream>
#include <cstdio>
#include <cstring>
#include <vector>
#include <map>
#include <set>
#include <queue>
#include <algorithm>
#include <cmath>
#include <sstream>
#include <utility>
#include <ctime>
#include <memory.h>
#include <cctype>
#include <cstdlib>

using namespace std;

#pragma comment (linker, "/STACK:64000000")

#define y0 qwe
#define y1 asd
#define sz size()
#define pb push_back
#define fors(w,s) for(map <int, int> :: iterator w = s.begin(); w != s.end(); w++)
#define pii pair<int, int>
#define pll pair<ll, ll>
#define ull unsigned long long
#define vi vector <int>
#define vvi vector <vi>
#define inf 2000000000
#define mod 1000000007
#define ll long long
#define maxint 2139062143 //2147483647
#define maxll 9223372036854775807
#define fi first
#define se second
#define eps 1e-9
#define doubleinf 1000000.0

int n, m, t, y, j, l, i, h, q, q1, q2, a1[5][5], a2[5][5], cnt;

inline void solve(int t)
{
	scanf ("%d", &q1);
	for (j = 1; j <= 4; j++)
	{
		for (i = 1; i <= 4; i++)
		{
			scanf ("%d", &a1[j][i]);
		}
	}
	scanf ("%d", &q2);
	for (j = 1; j <= 4; j++)
	{
		for (i = 1; i <= 4; i++)
		{
			scanf ("%d", &a2[j][i]);
		}
	}
	cnt = 0;
	for (j = 1; j <= 4; j++)
	{
		for (i = 1; i <= 4; i++)
		{
			if (a1[q1][j] == a2[q2][i])
			{
				cnt++;
			}
		}
	}
	if (cnt != 1)
	{
		if (cnt)
		{
			printf ("Case #%d: Bad magician!\n", t);
		}
		else
		{
			printf ("Case #%d: Volunteer cheated!\n", t);
		}
	}
	else
	{
		for (j = 1; j <= 4; j++)
		{
			for (i = 1; i <= 4; i++)
			{
				if (a1[q1][j] == a2[q2][i])
				{
					printf ("Case #%d: %d\n", t, a1[q1][j]);
					break;
				}
			}
			if (i < 5)
			{
				break;
			}
		}
	}
}

inline void init()
{
    scanf ("%d", &t);
	for (int j = 1; j <= t; j++)
	{
		solve(j);
	}
}

inline void answer()
{
    
}

int main()
{
    freopen ("A-small-attempt0.in","r",stdin); freopen ("output.txt","w",stdout);
    //freopen ("olympiad.in","r",stdin); freopen ("olympiad.out","w",stdout);
    init();
	//solve();
    answer();
    return 0;
}