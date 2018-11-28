#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cstdlib>
#include <vector>
#include <map>
#include <set>
#include <cstring>

#define forn(i, n) for (int i = 0; i < (int)n; ++i)

using namespace std;

void solve()
{
	double c, f, x;
	cin >> c >> f >> x;
	double total = 0;
	double speed = 2;
	double time = 0.0;
	while (total < x) {
		if (total >= c && (x - total + c) / (speed + f) < (x - total) / speed) {
//			cout << "Tuta" << endl;
			total -= c;
			speed += f;
		} else {
			double ctime = 1.0;
			if (total < c) {
				ctime = (c - total) / speed;
			}
			ctime = min(ctime, (x - total) / speed);
//			cout << c << ' ' << total << endl;
//			double ctime  = (x - total) / speed;
			time += ctime;
			total += ctime * speed;
		}
//		cout << total << endl << endl;
	}
	printf("%.10lf\n", time);
}


int main()
{
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);
	int tt;
	scanf("%d", &tt);
	forn(t, tt)
	{
		cout << "Case #" << (t + 1) << ": ";
		solve();
	}
	return 0;
}
