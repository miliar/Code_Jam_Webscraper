#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <ctime>
#include <cstring>
#include <string>
#include <bitset>
#include <vector>
#include <list>
#include <deque>
#include <queue>
#include <stack>
#include <set>
#include <map>
#include <algorithm>

using namespace std;

typedef long long LL;
typedef unsigned long long ULL;
typedef long double LD;

const double INF = 1e10;

int testCases;
double C, F, X, ans;

int main()
{
	cin >> testCases;
	for (int index = 1; index <= testCases; ++index) {
		cin >> C >> F >> X;
		ans = INF;
		double curTime = 0;
		double rate = 2;
		while (1) {
			if (curTime > ans) break;
			ans = min(ans, curTime + X / rate);
			curTime += C / rate;
			rate += F;
		}
		printf("Case #%d: %.10lf\n", index, ans);
	}
	return 0;
}
