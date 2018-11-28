#include <cstdio>
#include <cstring>
#include <cmath>
#include <vector>
#include <queue>
#include <stack>
#include <map>
#include <list>
#include <utility>
#include <string>
#include <algorithm>
#define infinity 2139062143
#define swap(x, y) (x) ^= (y) ^= (x) ^= (y)
#define foreach( i, n ) 	for(int (i) = 0; (i) < (n); ++(i))
#define min( x, y )  ( ((x) < (y)) ? (x) : (y) )
#define max( x, y )  ( ((x) > (y)) ? (x) : (y) )
#define abs( x ) (((x) < 0)? (-x) : (x) )
#define full 100
#define PI 3.14159265359
using namespace std;

int main () {
	int n, r, t, acc, ri;
	scanf("%d", &n);
	foreach (caso, n) {
		scanf("%d %d", &r, &t);
		acc = 0;
		ri = r + 1;
		while (t > 0) {
			t -= ri*ri - r*r;
			if (t >= 0)
				acc++;
			r += 2;
			ri = r + 1;
		}
		printf("Case #%d: %d\n", caso+1, acc);
	}
	return 0;
}



	