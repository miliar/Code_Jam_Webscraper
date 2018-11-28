#include <algorithm>
#include <numeric>
#include <cmath>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <iostream>
#include <sstream>
#include <map>
#include <queue>
#include <set>
#include <stack>
#include <string>
#include <unordered_map>
#include <unordered_set>
#include <vector>
#include <stdio.h>
#include <iomanip>
typedef long long ll;
#define mset(a, val) memset(a, val, sizeof(a))
#define up(i, s, t) for (ll i = (s); i < (t); i += 1)
#define down(i, s, t) for (ll i = (s); i > (t); i -= 1)
#define rd1(a) scanf("%d", &a)
#define rd2(a, b) scanf("%d %d", &a, &b)
#define rd3(a, b, c) scanf("%d %d %d", &a, &b, &c)
#define rd4(a, b, c, d) scanf("%d %d %d %d", &a, &b, &c, &d)
#define pii pair<int, int>

using namespace std;
const int MAXINT = 0x6fffffff;
const ll MAXLONG = (ll) 1 << 63 - 1;
int main () {
    #ifndef ONLINE_JUDGE
        freopen("input.txt", "r", stdin);
        freopen("output.txt", "w", stdout);
    #endif

	int t;
	cin >> t;
	up(ca, 1, t + 1) {
		double time = 0.0, have = 0.0, speed = 2.0;
		double c, f, x;
		cin >> c >> f >> x;
		
		cout << std::setprecision(7);
		if (c >= x) {
			time = x / speed;
			printf("Case #%d: ", ca);
			cout << fixed  <<  setprecision(7) << time  <<  endl;
			continue;
		}

		while (true) {
			if (have < c) {
				time += (c - have) / speed;
				have = c;
			} else { // have == c
				// two choices
				// first, don't buy another farm
				double t1 = (x - have) / speed;
				
				// second, buy another farm
				double t2 = (x + c - have) / (speed + f);

				if (t1 <= t2) {
					time += t1;
					break;
				} else {
					speed += f;
					have = have - c;
				}
			}
		}

		printf("Case #%d: ", ca);
		cout << fixed  <<  setprecision(7) << time  <<  endl;
	}
	
    return 0;
}