#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;

typedef vector<int> vi;
typedef long long ll;
typedef pair<int, int> ii;
typedef vector<ii> vii;
typedef vector<vi> vvi;
typedef vector<vii> vvii;

#define INF 100000000

int main()
{
	int T; cin >> T;
	int temp;
	for(int t = 1; t <= T; ++t)
	{
		double C, F, X; cin >> C >> F >> X;
		double cps = 2.0;
		double res = 0.0;
		while ((X/cps) > (C/cps + X/(cps+F))) {
			res += C/cps;
			cps += F;
		}
		res += X/cps;
		printf("Case #%d: %.7f\n", t, res);
	}
}
