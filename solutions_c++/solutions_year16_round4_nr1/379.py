#include<iostream>
#include<vector>
#include<string>
#include<algorithm>
#include<cstdio>
#include<numeric>
#include<cstring>
#include<ctime>
#include<cstdlib>
#include<set>
#include<map>
#include<unordered_map>
#include<unordered_set>
#include<list>
#include<cmath>
#include<bitset>
#include<cassert>
#include<queue>
#include<stack>
#include<deque>
#include<cassert>
using namespace std;
typedef long long ll;
typedef long double ld;
bool check(int n, int p, int r, int s)
{
	return p + r + s == n && abs(p - r) <= 1 && abs(r - s) <= 1 && abs(p - s) <= 1;
}
int tmp[5];
void go(int n, int p, int r, int s)
{
	if (n == 1)
	{
		if (p == 1)
		{
			printf("P");
		}
		else if (r == 1)
		{
			printf("R");
		}
		else if (s == 1)
		{
			printf("S");
		}
	}
	else
	{
		tmp[0] = (n / 2) / 3;
		tmp[1] = ((n / 2) - tmp[0]) / 2;
		tmp[2] = n / 2 - tmp[0] - tmp[1];
		for (int i = 0; i < 6; i++)
		{
			if (check(n / 2, tmp[0], tmp[1], tmp[2]) && check(n / 2, p - tmp[0], r - tmp[1], s - tmp[2]))
			{
				break;
			}
			next_permutation(tmp, tmp + 3);
		}
		if (!(check(n / 2, tmp[0], tmp[1], tmp[2]) && check(n / 2, p - tmp[0], r - tmp[1], s - tmp[2])))
		{
			assert(0);
		}
		int p1 = tmp[0], r1 = tmp[1], s1 = tmp[2];
		int p2 = p - p1, r2 = r - r1, s2 = s - s1;
		if (make_pair(make_pair(p1, r1), s1) < make_pair(make_pair(p2, r2), s2))
		{
			swap(p1, p2);
			swap(r1, r2);
			swap(s1, s2);
		}
		go(n / 2, p1, r1, s1);
		go(n / 2, p2, r2, s2);
	}
}
int pw(int n, int k)
{
	int res = 1;
	for (int i = 1; i <= k; i++)
	{
		res *= n;
	}
	return res;
}
char play(char a, char b)
{
	if (a == 'R' && b == 'S') return 'R';
	if (a == 'S' && b == 'R') return 'R';
	if (a == 'S' && b == 'P') return 'S';
	if (a == 'P' && b == 'S') return 'S';
	return 'P';
}
char cur[17];
bool ok = true;
char check(int l, int r)
{
	if (l == r) return cur[l];
	char x = check(l, (l + r) / 2);
	char y = check((l + r) / 2 + 1, r);
	if (x == y) ok = false;
	return play(x, y);
}
int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int t;
	scanf("%d", &t);
	for (int tt = 1; tt <= t; tt++)
	{
		int n, p, r, s;
		scanf("%d %d %d %d", &n, &r, &p, &s);
		n = (1 << n);
	/*	bool gg = false;
		for (int mask = 0; mask < pw(3, n); mask++)
		{
			int cp = p, cr = r, cs = s;
			int tmp = mask;
			for (int i = n; i >= 1; i--)
			{
				if (tmp % 3 == 0)
				{
					cur[i] = 'P';
					cp--;
				}
				else if (tmp % 3 == 1)
				{
					cur[i] = 'R';
					cr--;
				}
				else
				{
					cur[i] = 'S';
					cs--;
				}
				tmp /= 3;
			}
			ok = true;
			if (cp != 0 || cs != 0 || cr != 0) ok = false;
			check(1, n);
			if (ok)
			{
				gg = true;				
				break;
			}
		}
		printf("Case #%d: ", tt);
		if (gg)
		{
			for (int i = 1; i <= n; i++)
			{
				printf("%c", cur[i]);
			}
			printf("\n");
		}
		else
		{
			printf("IMPOSSIBLE\n");
		} */
		if (!check(n, p, r, s))
		{
			printf("Case #%d: IMPOSSIBLE\n", tt);
			continue;
		}
		printf("Case #%d: ", tt);
		go(n, p, r, s);
		printf("\n");

	}
}
