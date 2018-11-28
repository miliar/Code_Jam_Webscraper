#include <set>
#include <map>
#include <stack>
#include <cmath>
#include <ctime>
#include <queue>
#include <string>
#include <vector>
#include <cstdio>
#include <sstream>
#include <cstring>
#include <climits>
#include <cstring>
#include <iostream>
#include <algorithm>
#define ff first
#define ss second
#define LL long long
#define pb push_back
#define mp make_pair
#define EPS 0.00000001
#define sqr(x) ((x) * (x))
#define PI 3.1415926535897932384626433832795
using namespace std;

int main() {
	int t, i, l, j, tc = 1;
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);
	scanf("%d", &t);
	while(t--) {
		double farm, k, need, prod = 2.0, ans = 0.0;
		scanf("%lf%lf%lf", &farm, &k, &need);
		while((need / prod) > ((farm / prod) + (need / (prod + k)))) {
			ans += (farm / prod);
			prod += k;
		}
		ans += (need / prod);
		printf("Case #%d: %.7lf\n", tc++, ans + EPS);
	}
	return 0;
}

