#define _USE_MATH_DEFINES

#include <iostream>
#include <cstdio>
#include <vector>
#include <cmath>
#include <list>
#include <iomanip>
#include <stack>
#include <map>
#include <set>
#include <queue>
#include <string>
#include <algorithm>
#include <cstring>
#include <cstdlib>

#define all(a) a.begin(),a.end()
#define pb push_back
#define mp make_pair
#define forn(i,n) for(int i = 0; i < int(n); ++i)

using namespace std;

typedef long long li;
typedef long double ld;

typedef pair<int,int> point;
#define X first
#define Y second

const double eps = 1e-7;

int main() {
#ifdef dans
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif

	int t;
	cin >> t;
	forn(i, t) {
		double c, f, x;
		cin >> c >> f >> x;
		double speed = 2.0, res = 0.;
		while (true) {
			if (c / speed + x / (speed + f) + eps < x / speed) {
				res += c / speed;
				speed += f;
			} else {
				res += x / speed;
				break;
			}
		}
		cout << "Case #" << i+1 << ": " << fixed << setprecision(7) << res << endl;
	}
	
	return 0;
}
