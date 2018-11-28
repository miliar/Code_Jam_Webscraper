#include <vector>
#include <list>
#include <map>
#include <set>
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
#include <cstring>
#define BIG 1000000000
#define LL long long
using namespace std;

int ntest;
double C, F, X;

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	cin >> ntest;
	for (int test = 1; test <= ntest; test++) {
		cin >> C >> F >> X;
		double curRate = 2;
		double bestTime = X / curRate;
		double buyTime = 0;
		for (int i = 1; ; i++) {
			buyTime += C / curRate;
			curRate += F;
			double curTime = buyTime + X / curRate;
			if (curTime >= bestTime) {
				printf("Case #%d: %.9lf\n", test, bestTime);
				break;
			}
			bestTime = curTime;
		}
 	}
}	

