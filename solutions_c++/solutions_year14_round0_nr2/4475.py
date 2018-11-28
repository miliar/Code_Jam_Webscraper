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
#include <iostream>
#define infinity 2139062143
#define infinity64 9187201950435737471LL
#define foreach( i, n ) 	for(int (i) = 0; (i) < (n); ++(i))
#define abs( x ) (((x) < 0)? (-x) : (x) )
#define full 100
using namespace std;

int main () {
	int n;
	double res, c, f, x, resf, prod, acc;
	scanf("%d", &n);
	foreach (t, n) {
		scanf("%lf %lf %lf", &c, &f, &x);
		prod = 2.0;
		acc = 0.0;
		resf = res = x / prod;
		do {
			resf = res;
			acc += c / prod;
			prod += f;
			res = (x / prod) + acc;
		} while(res < resf);
		printf("Case #%d: %.7lf\n", t+1, resf);
	}
	return 0;
}


