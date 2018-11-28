#include <iostream>
#include <vector>
#include <algorithm>
#include <utility>
using namespace std;
#define fo(i,n) for(int i=0, _n=(n); i < _n; ++i)
#define range(i,a,b) for(int i=(a), _n=(b); i < _n; ++i)

typedef long long ll;
const int MAX_B = 1100;
const ll oo = 1ll << 50ll;
int W, H, B;
bool seen[MAX_B];
ll dist[MAX_B];

typedef pair<int, int> pr;
typedef pair<pr, pr> rect;

rect buildings[MAX_B];

#define _topLeft first
#define _botRight second
#define _x first
#define _y second

ll rectDistLeft(rect r) {
	return r._topLeft._x;
}

ll rectDistRight(rect r) {
	return W - r._botRight._x;
}

inline bool between(int a, int low, int high) {
	return a >= low && a <= high;
}

ll rectDist(rect r1, rect r2) {
	ll xDist = min(abs(r1._topLeft._x - r2._botRight._x), abs(r1._botRight._x - r2._topLeft._x)), yDist = min(abs(r1._topLeft._y - r2._botRight._y), abs(r1._botRight._y - r2._topLeft._y));
	if (between(r1._topLeft._y, r2._topLeft._y, r2._botRight._y) || between(r1._botRight._y, r2._topLeft._y, r2._botRight._y) || between(r2._topLeft._y, r1._topLeft._y, r1._botRight._y) || between(r2._botRight._y, r1._topLeft._y, r1._botRight._y)) {
		yDist = 0;
	}
	if (between(r1._topLeft._x, r2._topLeft._x, r2._botRight._x) || between(r1._botRight._x, r2._topLeft._x, r2._botRight._x) || between(r2._topLeft._x, r1._topLeft._x, r1._botRight._x) || between(r2._botRight._x, r1._topLeft._x, r1._botRight._x)) {
		xDist = 0;
	}
	return max(xDist, yDist);
}


int main() {
	int T;
	cin >> T;
	range(testCase, 1, T+1) {
		cin >> W >> H >> B;
		fo(i,B) {
			int x0, y0, x1, y1;
			cin >> x0 >> y0 >> x1 >> y1;
			buildings[i] = rect(pr(x0, y0), pr(x1 + 1, y1 + 1));
			dist[i] = rectDistLeft(buildings[i]);
			seen[i] = false;
		}
		ll bestDist = W;
		fo(iter,B) {
			int m = 0;
			fo(i,B) if(seen[m] || (dist[i] < dist[m] && !seen[i])) m = i;
			seen[m] = true;
			bestDist = min(bestDist, dist[m] + rectDistRight(buildings[m]));

			fo(i,B) if(!seen[i]) dist[i] = min(dist[i], dist[m] + rectDist(buildings[m], buildings[i]));
		}
		cout << "Case #" << testCase << ": " << bestDist << endl;
	}

}