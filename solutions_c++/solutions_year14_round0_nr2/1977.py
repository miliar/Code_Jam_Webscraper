#include <cmath>
#include <iostream>
#include <string>
#include <vector>
#include <cstdlib>
#include <map>
#include <set>
#include <algorithm>
#include <cstring>
#include <queue>
#include <stack>
#include <sstream>
#include <cstdio>

using namespace std;

#define mp make_pair
typedef long long llong;
typedef unsigned long long ullong;
typedef pair<int, int> PI;
typedef pair<int, PI> PII;
typedef vector<int> VI;
typedef vector<VI> VVI;

int main()
{
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);
	int tc;
	scanf("%d", &tc);
	for(int t = 1; t <= tc; ++t){
		double c, f, x;
		scanf("%lf %lf %lf", &c, &f, &x);
		double mi = 1e18;
		double sofar = 0;
		double rate = 2.0;
		for(int i = 0; i <= 100000; ++i){
			mi = min(mi, sofar + 1.0*x/rate);
			sofar += 1.0*c/rate;
			rate += f;
		}
		printf("Case #%d: %.7lf\n", t, mi);
	}
	return 0;
}


