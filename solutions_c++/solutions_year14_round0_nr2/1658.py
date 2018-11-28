#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <ctime>
#include <iostream>
#include <sstream>
#include <vector>
#include <string>
#include <queue>
#include <bitset>
#include <set>
#include <map>
#include <algorithm>
#include <iomanip>
#include <limits>

using namespace std;

typedef long long LL;
typedef pair<int, int> PII;
typedef pair<LL, LL> PLL;
typedef pair<int, double> PID;
typedef pair<double, double> PDD;

#define pb(x) push_back(x)
#define X first
#define Y second

int T, cases;
double C, F, X;

int main(){
	for (scanf("%d", &T), cases = 1; cases <= T; ++cases) {
		printf("Case #%d: ", cases);
		scanf("%lf %lf %lf", &C, &F, &X);

		double ans = 1e100, rate = 2, time = 0;
		for (int i = 0; i <= X; ++i) {
			ans = min(ans, time + X / rate);
			time += C / rate;
			rate += F;
		}
		printf("%.8f\n", ans);
	}
}
