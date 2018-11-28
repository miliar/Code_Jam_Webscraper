#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <assert.h>
#include <time.h>
#include <math.h>

#include <algorithm>
#include <vector>
#include <deque>
#include <stack>
#include <queue>
#include <functional>
#include <string>
#include <set>
#include <map>
#include <iostream>

#define FOR(var, size) for (int (var) = 0; (var) < (size); (var)++)

using namespace std;
//const int inf = 0x7fffffff;
typedef long long int llint;
const double eps = 1e-10;
const double inf = 1e+308;



void solve()
{
	int i, j, k;
	double coo = 2.0, cur = 0.0, min = inf;
	
	double c, f, x;
	cin >> c >> f >> x;
	
	for (i = 0; i < x/c+2; i++) {
		double tmp = cur + x / coo;
		if (tmp < min)
			min = tmp;
		cur += c / coo;
		coo += f;
	}
	
	printf("%.7lf\n", min);
}


int main()
{
	int t, i;
	
	scanf("%d", &t);
	
	for (i = 0; i < t; i++) {
		printf("Case #%d: ", i+1);
		solve();
	}
	
	return 0;
}
