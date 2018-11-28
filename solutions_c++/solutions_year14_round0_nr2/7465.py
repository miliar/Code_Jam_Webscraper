#include <cstdio>
#include <cmath>
#include <iostream>
#include <algorithm>
#include <cstring>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <list>
using namespace std;

typedef long long LL;
typedef vector<int> VI;
typedef pair<int, int> PII;
typedef vector<PII> VPII;

#define REP(x, n) for(int x = 0; x < (n); ++x)
#define FOR(x, b, e) for(int x = b; x <= (e); ++x)
#define FORD(x, b, e) for(int x = b; x >= (e); --x)
#define VAR(v, n) __typeof(n) v = (n)
#define FOREACH(i, c) for(VAR(i, (c).begin()); i != (c).end(); ++i)
#define SIZE(x) ((int)(x).size())
#define PB push_back
#define PF push_front
#define MP make_pair
#define FI first
#define SE second

const int INF = 1000000001;
const double EPS = 10e-9;


long double c,f,x;


long double ft(int k) {

	int d=0;
	long double t=0;

	while(d<k) {
		t += c/(2.0+(f*d));
		d++;
	}

	t += x/(2.0+(f*d));

	return t;
}



int main() {

	const int TIMES = 2;

	int testCases;
	scanf("%d", &testCases);

	FOR(testCase, 1, testCases) {

		scanf("%Lf%Lf%Lf", &c,&f,&x);

		int lft = 0, rght = 10000000;

		while(lft < rght) {
			int mid = (lft+rght) / 2;

			// printf("%d %d\n", lft, rght);

			if(ft(mid) > ft(mid+1)) {
				lft = mid+1;
			} else {
				rght = mid;
			}
		}

		long double result = INF;
		for(int i=max(0,lft-3); i<=lft+3; i++) {
			result = min(result, ft(i));
		}

		printf("Case #%d: %.7Lf\n", testCase, result);

	}

	return 0;
}
