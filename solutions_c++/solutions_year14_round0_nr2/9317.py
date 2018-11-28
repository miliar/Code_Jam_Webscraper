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




int main() {
	freopen("B-large.in", "r", stdin);
	freopen("output.txt", "w", stdout);
	int t;
	cin >> t;
	forn (i, t)	{
		cout << "Case #" << i + 1 << ": ";        
		cin >> c >> f >> x;
		ld time = 0, v = 2;
		set<ld> ee;
		ee.insert(x / v);
		ee.insert(c / v);
		ld cur = 0;
		while (cur + 1e-8 < x) {
			ld t = *ee.begin();
			ee.erase(ee.begin());
			cur += (t - time) * v;
			time = t;
			if ((x - cur) / v > x / (v + f)) {
				cur = 0;
				v += f;
				ee.insert(time + c / v);
			}
			else
				break;
		}
		time += (x - cur) / v;
		cout << fixed << setprecision(10) << time << endl;
	}

	return 0;
}