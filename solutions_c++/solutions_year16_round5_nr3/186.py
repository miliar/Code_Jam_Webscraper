#include <algorithm>
#include <bitset>
#include <cmath>
#include <cstdio>
#include <cstring>
#include <deque>
#include <iomanip>
#include <iostream>
#include <queue>
#include <map>
#include <numeric>
#include <set>
#include <sstream>
#include <stack>
#include <utility>
#include <vector>

#define INF 1000000000
#define FOR(i, a, b) for(int i=int(a); i<int(b); i++)
#define FORC(cont, it) for(typeof((cont).begin()) it = (cont).begin(); it != (cont).end(); it++)
#define pb push_back

using namespace std;

typedef long long ll;
typedef pair<int, int> ii;
typedef vector<int> vi;
typedef vector<ii> vii;
typedef vector<vi> vvi;

#define maxN 1000
#define maxS 101

struct Asteroid {
	double x, y, z, vx, vy, vz;
};

struct Data {
	int f;
	double v;
	bool operator <(const Data &r) const {
		return v > r.v;
	}
};

double d[maxN];
Asteroid a[maxN];

double getD(const Asteroid &l, const Asteroid &r) {
	return sqrt((l.x - r.x)*(l.x - r.x) + (l.y - r.y)*(l.y - r.y) + (l.z - r.z)*(l.z - r.z));
}

int main() {
	int T, caso=1, N, S;
	cin >> T;
	cout << fixed << setprecision(9);
	while (T--) {
		cin >> N >> S;
		FOR(i, 0, N) {
			cin >> a[i].x >> a[i].y >> a[i].z >> a[i].vx >> a[i].vy >> a[i].vz;
			d[i] = 1e9;
		}
		priority_queue<Data> q;
		d[0] = 0;
		q.push(Data{ 0, 0 });
		while (!q.empty()) {
			int f = q.top().f;
			q.pop();
			FOR(i, 0, N) {
				double nd = max(d[f], getD(a[f], a[i]));
				if (d[i] > nd) {
					d[i] = nd;
					q.push(Data{ i, nd });
				}
			}
		}
		cerr << "Case #" << caso << ": " << d[1] << endl;
		cout << "Case #" << caso++ << ": " << d[1] << endl;
	}
	return 0;
}
