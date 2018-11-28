#pragma comment(linker, "/STACK:167177216")

#include<stdio.h>
#include<stack>
#include<math.h>
#include<iostream>
#include<algorithm>
#include<string.h>
#include<string>
#include<set>
#include<memory.h>
#include<vector>
#include<map>
#include<queue>
#include<iomanip>
#include<ctime>

using namespace std;

typedef long long li;
typedef long double ld;

#define forn(i, n) for (int i = 0; i < int(n); ++i)
#define pb push_back
#define mp make_pair

ld c, f, x;

void read()
{
	cin >> c >> f >> x;
}

void solve()
{
	ld time = 0, v = 2;
	set<ld> ev;
	ev.insert(x / v);
	ev.insert(c / v);
	ld cur = 0;
	while (cur + 1e-8 < x)
	{
		ld t = *ev.begin();
		ev.erase(ev.begin());
		cur += (t - time) * v;
		time = t;
		if ((x - cur) / v > x / (v + f))
		{
			cur = 0;
			v += f;
			ev.insert(time + c / v);
		}
		else
			break;
	}
	time += (x - cur) / v;
	cout << fixed << setprecision(10) << time << endl;
}

int main()
{
#ifdef Baster
    freopen("B-large.in", "r", stdin);
    freopen("output.txt", "w", stdout);
#endif
	int t;
	cin >> t;
	forn (i, t)
	{
		cout << "Case #" << i + 1 << ": ";
		read();
		solve();
	}

	return 0;
}