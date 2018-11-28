#include <iostream>
#include <cmath>
#include <vector>
#include <map>
#include <set>
#include <string>
#include <cstring>
#include <queue>
#include <ctime>
#include <cassert>
#include <cstdio>
#include <algorithm>
#include <unordered_set>
#include <unordered_map>
#include <bitset>

using namespace std;

#define fr first
#define sc second
#define mp make_pair
#define pb push_back
#define epr(...) fprintf(stderr, __VA_ARGS__)
#define db(x) cerr << #x << " = " << x << endl
#define db2(x, y) cerr << "(" << #x << ", " << #y << ") = (" << x << ", " << y << ")\n"; 
#define db3(x, y, z) cerr << "(" << #x << ", " << #y << ", " << #z << ") = (" << x << ", " << y << ", " << z << ")\n"
#define all(a) (a).begin(), (a).end()

#define equal equalll
#define less lesss
const int N = 10000;
const long long INF = 1e9 + 19;

struct pt {
	double x, y, z;
	pt () { }
	pt (double x, double y, double z): x(x), y(y), z(z) { }
	pt operator - (pt A) {
		return pt(x - A.x, y - A.y, z - A.z);
	}
	double len() {
		return sqrt(x * x + y * y + z * z);
	}
	void read() {
		scanf("%lf%lf%lf", &x, &y, &z);
	}
};

int n, s;

pt p[N];
bool use[N];

bool check(double d) {
	memset(use, 0, sizeof(use));
	queue < int > q;
	q.push(1);
	use[1] = 1;
	while (!q.empty()) {
		int v = q.front();
		q.pop();
		for (int i = 0; i < n; i++)
			if (!use[i] && (p[i] - p[v]).len() < d) {
				use[i] = 1;
				q.push(i);
			}
	}
	return use[0];
}

void read() {
	scanf("%d%d", &n, &s);
	for (int i = 0; i < n; i++) {
		p[i].read();
		pt v;
		v.read();
	}
	double l = 0;
	double r = INF;
	for (int it = 0; it < 100; it++) {
		if (check((l + r) / 2))
			r = (l + r) / 2;
		else
			l = (l + r) / 2;
	}
	printf("%.17f\n", l);
}

void solve() {

}

void stress() {

}

int main(){
#ifdef MY_DEBUG
    freopen("in", "r", stdin);
	freopen("out", "w", stdout);
#endif
    if (1) {
        int k = 1;
		scanf("%d", &k);
        for (int tt = 0; tt < k; tt++) {
			printf("Case #%d: ", tt + 1);
            read();
            solve();
        }
    }
    else {
        stress();
    }

    return 0;
}


