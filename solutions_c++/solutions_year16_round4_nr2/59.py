#include <iostream>
#include <stdio.h>
#include <vector>
#include <algorithm>
#include <set>
#include <map>
#include <cmath>
#include <string>
#include <cstring>
#include <ctime>
#include <cassert>
#include <queue>
#include <stack>
#include <bitset>
#define y1 y11
#define fs first
#define sc second
#define mp make_pair
#define pb push_back
#define mt make_tuple
#define NAME ""

using namespace std;
	
typedef long long ll;
typedef long double ld;

const ld PI = acos(-1.0);

const int MAXN = 202;

ld f1[MAXN][MAXN];
ld f2[MAXN][MAXN];
ld a[MAXN];


int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int tests;
	cin >> tests;
	cout.setf(ios::fixed);
	cout.precision(20);
	for (int test = 1; test <= tests; test++)
	{
		cout << "Case #" << test << ": ";
		int n, k;
		cin >> n >> k;
		for (int i = 0; i < n; i++)
		{
			cin >> a[i];
		}
		sort(a, a + n);
		for (int i = 0; i <= n; i++) f1[0][i] = f2[n][i] = 0.0;
		f1[0][0] = f2[n][0] = 1.0;
		ld ans = 0;
		for (int i = 0; i < n; i++)
		{
			for (int j = 0; j <= n; j++) f1[i + 1][j] = 0.0;
			for (int j = 0; j <= i; j++) f1[i + 1][j] += f1[i][j] * (1.0 - a[i]), f1[i + 1][j + 1] += f1[i][j] * a[i];	
		}
		for (int i = n - 1; i >= 0; i--)
		{
			for (int j = 0; j <= n; j++) f2[i][j] = 0.0;
			for (int j = 0; j < n - i; j++)
			{
				f2[i][j] += f2[i + 1][j] * (1.0 - a[i]);
				f2[i][j + 1] += f2[i + 1][j] * a[i];
			}
		}
		for (int i = 0; i <= k; i++)
		{
			ld cur = 0;
			for (int j = 0; j <= k / 2; j++)
			{
				cur += f1[i][j] * f2[n - k + i][k / 2 - j];
			}
			ans = max(ans, cur);
		}
		cout << ans << endl;
	}
	return 0;
}