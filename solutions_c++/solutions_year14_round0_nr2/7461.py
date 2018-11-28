/*~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
 |Author: WiYR
 |Created Time.: 2014/4/12 22:08:24
 |File Name: 1B.cpp
 |Description: 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~*/
#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <string>
#include <cstring>
#include <algorithm>
#include <vector>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
typedef long long ll;
const double eps=1e-7;
const int inf=0x7FFFFFFF;
#define show(x) cout << x << endl
#define rep(i,n) for(int i=0;i<n;i++)
#define mset(a,i) memset(a,i,sizeof(a))
#define PB(i) push_back(i)

using namespace std;
int main() {
	int T;
	double C, F, X;
	scanf("%d", &T);
	rep(cas, T) {
		scanf("%lf%lf%lf", &C, &F, &X);
		double ans = 0, speed = 2;
		for(double curt = X / speed, t = C / speed + X / (speed + F); curt > t;) {
			ans += C / speed;
			speed += F;
			curt = X / speed;
			t = C / speed + X / (speed + F);
		}
		ans += X / speed;
		printf("Case #%d: %.8lf\n", cas + 1, ans);
	}
	return 0;
}

