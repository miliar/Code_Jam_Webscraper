#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cmath>
#include <string>
#include <string.h>
#include <stack>
#include <queue>
#include <map>
#include <vector>
#include <set>
#include <cassert>
#include <ctime>
#include <cstdlib>

using namespace std;

#define ll long long
#define ld long double
#define ull unsigned long long
#define uint unsigned int
#define fst first
#define snd second
#define pb push_back
#define mp make_pair
#define y0 alfdjasldfjeao
#define y1 safiodjafis

const ld eps = 1e-9;

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int T;
	cin >> T;
	for (int test = 1; test <= T; test++)
	{
		cout << "Case #" << test << ": ";
		int n;
		cin >> n;
		ld V, T;
		cin >> V >> T;
		ld sumv = 0, sumvt = 0;
		vector < pair < ld , ld > > v;
		for (int i = 1; i <= n; i++)
		{
			ld r, t;
			cin >> r >> t;
			v.pb(mp(t, r));
			sumv += r;
			sumvt += r * t;
		}
		sort(v.begin(), v.end());
		bool flag = false;
		if (v[0].fst < T + eps && v.back().fst > T - eps)
			flag = true;
		if (!flag)
		{
			cout << "IMPOSSIBLE\n";
			continue;
		}
		ld TT = sumvt / sumv;
		bool rev = false;
		if (TT > T)
			rev = true;
		ld L = 0, R = 1e9;
		while (R - L > 1e-8)
		{
			ld m = (L + R) / 2;
			ld cur = 0, curans = 0;
			if (rev)
			{
				for (int i = 0; i < v.size(); i++)
				{
					ld t = v[i].fst, r = v[i].snd;
					ld v = m * r;
					if (cur + (T - t) * v < -eps)
					{
						curans += cur / abs(T - t);
						break;
					}
					else
						curans += v, cur += (T - t) * v;
				}
			}
			else
			{
				for (int i = v.size() - 1; i >= 0; i--)
				{
					ld t = v[i].fst, r = v[i].snd;
					ld v = m * r;
					if (cur + (t - T) * v < -eps)
					{
						curans += cur / abs(T - t);
						break;
					}
					else
						curans += v, cur += (t - T) * v;
				}
			}
			if (curans >= V)
				R = m;
			else
				L = m;
		}
		cout.precision(8);
		cout << fixed << L << "\n";
	}
	return 0;
}
