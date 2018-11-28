#include <iostream>
#include <fstream>
#include <set>
#include <map>
#include <string>
#include <vector>
#include <bitset>
#include <algorithm>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <cassert>
#include <queue>


typedef long long ll;
typedef long double ld;

using namespace std;
struct point {
	int x, y, z;
	point() {
		x = y = z = 0;
	}
	point(int X, int Y, int Z) {
		x = X, y = Y, z = Z;
	}
	point operator-(point a) {
		return point(x - a.x, y - a.y, z - a.z);
	}
	ld len() {
		return sqrt(x * x + y * y + z * z);
	}
};

ld dd[1200][1200];
int n, s;

point arr[1200];
point va[1200];


ld solve() {
	scanf("%d%d", &n, &s);
	for (int i = 0; i < n; ++i) {
		scanf("%d%d%d%d%d%d", &arr[i].x, &arr[i].y, &arr[i].z, &va[i].x, &va[i].y, &va[i].z);
	}
	for (int i = 0; i < n; ++i)
		for (int j = 0; j < n; ++j)
			dd[i][j] = (arr[i] - arr[j]).len();
	for (int k = 0; k < n; ++k)
		for (int i = 0; i < n; ++i)
			for (int j = 0; j < n; ++j)
				dd[i][j] = min(dd[i][j], max(dd[i][k], dd[k][j]));
	return dd[0][1];
}

int main() {
	int tt;
	scanf("%d", &tt);
	for (int i = 0; i < tt; ++i) {
		printf("Case #%d: %.7f\n", i + 1, (double)solve());
	}
	return 0;
}


