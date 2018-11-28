#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
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
#include <cctype>
#include <string>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
 
using namespace std;
 
#define FOR(i,a,b) for(__typeof(b) i=(a);i!=(b);i++)
#define REP(i,n) FOR(i,0,n)
#define ALL(a) a.begin(),a.end()
#define EACH(i,a) FOR(i,a.begin(),a.end())
#define PB push_back
#define iss istringstream
#define SZ(a) (int)a.size()
#define CLEAR(a) memset(a,0,sizeof(a))
#define ll long long

int T;
double C, F, X;

inline double calc(int m) {
	double ret = X / (2.0 + m * F);
	for(int i = 0 ; i < m ; i++) {
		ret += (C / (2.0 + i * F));
	}
	return ret;
}

int main() {
	scanf("%d", &T);
	for(int t = 1 ; t <= T ; t++) {
		scanf("%lf %lf %lf", &C, &F, &X);
		double ans = min(calc(0), calc(1));
		int Y = (int)((((double)(X)) / C) - (2.0 / F));
		for(int j = max(2, Y - 2) ; j <= Y + 2 ; j++) {
			ans = min(ans, calc(j));
		}
		printf("Case #%d: %.7lf\n", t, ans);
	}
	return 0;
}
