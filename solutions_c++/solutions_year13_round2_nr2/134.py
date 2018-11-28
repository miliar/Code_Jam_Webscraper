// _template.cpp : Defines the entry point for the console application.
//

#include <cstdio>
#include <algorithm>
#include <iostream>
#include <vector>
#include <cmath>

typedef long long ll;
#define PI 3.1415926535897932384626433832795

using namespace std;

const int HH = 10;
#define MAXN 1000


int a[2*MAXN][MAXN];
int xx, yy, n;
double ans;

int get(int X, int Y) {
	return a[X+MAXN][Y + 2];
}

void set(int X, int Y, int Z) {
    a[X+MAXN][Y + 2] = Z;
}

void down(int step, double p, int x, int y) {
	if (step == 0) return;
	//printf("Enter step=%i x=%i y=%i\n", step, x, y);
	while (y > 0) {
//		printf("step=%i x=%i y=%i\n", step, x, y);
		// when do we stop?
		if (get(x + 1, y - 1) && get(x - 1, y - 1)) {
			break;
		}

		// slide right
		if (get(x - 1, y - 1)) {
			x++;
			y--;
			continue;
		}

		// slide left
		if (get(x + 1, y - 1)) {
			x--;
			y--;
			continue;
		}

		// clear choice
		if (get(x, y - 2) &&  (get(x + 1, y - 1) == 0 && get(x - 1, y - 1) == 0)) {
			down(step, p*0.5, x - 1, y - 1);
			down(step, p*0.5, x + 1, y - 1);
			return;
		}

		// garbage choice: go left
		if (get(x, y - 2) &&  (get(x + 1, y - 1) == 1 && get(x - 1, y - 1) == 0)) {
			x--;
			y--;
			continue;
		}

		// garbage choice: go right
		if (get(x, y - 2) &&  (get(x + 1, y - 1) == 0 && get(x - 1, y - 1) == 1)) {
			x++;
			y--;
			continue;
		}

		// fall down
     	y--;		
	}
	//printf("DOWN: step=%i x=%i y=%i   p=%.5f\n", step, x, y, p);
	if (x==xx && y==yy) {
		ans += p;
		return;
	}
	set(x, y, 1);
	down(step - 1, p, 0, HH);
	set(x, y, 0);
}

int main()
{
	int tc = 0;
	freopen("B-small-attempt0.in", "r", stdin);
	freopen("B-small-attempt0.out", "w", stdout);
	cin >> tc;
	for(int tt=1; tt<=tc; ++tt) {
		cin >> n >> xx >> yy;
		ans = 0.0;
		memset(a, 0, sizeof(a));
		down(n, 1.0, 0, HH);
		printf("Case #%i: %.12f\n", tt, ans);		
	}
	return 0;
}

