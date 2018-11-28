#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cassert>
#include <ctime>
#include <cstring>
#include <string>
#include <set>
#include <map>
#include <vector>
#include <list>
#include <deque>
#include <queue>
#include <sstream>
#include <iostream>
#include <algorithm>

using namespace std;

#define pb push_back
#define mp make_pair
#define fs first
#define sc second

const double pi = acos(-1.0);


int main() {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);

    int tc;

    cin >> tc;
    for (int tnum = 0; tnum < tc; tnum++) {
    	double c, f, x;
    	cin >> c >> f >> x;

    	double cur = 0.0;
    	double best = x / 2.0;
    	double speed = 2.0;
    	int cnt = 0;
    	while (cur < best) {
    		cnt++;
    		cur += c / speed;
    		speed += f;
    		best = min(best, cur + x / speed);
    	}
    	cout.precision(20);
    	cout << "Case #" << tnum + 1 << ": " << best << endl;
    }

    return 0;
}