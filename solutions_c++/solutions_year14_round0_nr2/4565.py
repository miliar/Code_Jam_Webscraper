#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <algorithm>
#include <queue>
#include <vector>
#include <set>
#include <stack>
#include <map>
#include <math.h>
#include <time.h>
#include <string>
using namespace std;
typedef long long LL;
const int INF = 0x3f3f3f3f;
const int N = 105;
#define eps 1e-7

using namespace std;

int main()
{
    int cases;
    scanf ("%d", &cases);

    for (int t = 1; t <= cases; t++) {
		double C, F, X;
		cin >> C >> F >> X;
		double v = 2;
		double ans = X / 2, m = 0;
		while (X * F - v * C >= -eps){
		    if (ans > X / v + m) {
                ans = X / v + m;
		    }
			m += C / v;
			v += F;
		}
		printf("Case #%d: %.7f\n", t, ans);
	}
    return 0;
}
