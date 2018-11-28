#include <algorithm>
#include <bitset>
#include <cctype>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <iostream>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <utility>
#include <vector>
using namespace std;

#define SIZE(v) ((int)(v).size())

#define BEGIN(v) ((v).begin())
#define END(v) ((v).end())
#define ALL(v) BEGIN(v),END(v)
#define SORT(v) sort(ALL(v))
#define UNIQUE(v) SORT(v);(v).erase(unique(ALL(v)),END(v))

#define FOR(i,l,r) for(int i=(l);i<(r);i++)
#define FOREACH(i,v) for(typeof((v).begin()) i=(v).begin();i!=(v).end();i++)

int n;
long long B;
vector<long long> bet;

double getBest(int n) {
	long long lower = bet[n - 1], upper = B + bet[0];
	double res = 0;
	while (lower <= upper) {
		long long medium = (lower + upper) >> 1, a = 0, b = 0;
		FOR(i, 0, n) a += medium - bet[i];
		FOR(i, n, 37) b += max(medium + 1 - bet[i], 0LL);
		if (a + b <= B) {
			lower = medium + 1;
			res = max(res, a * 36. / n - a - b);
		} else {
			upper = medium - 1;
		}
	}
	return res;
}

int main() {
	int taskNumber; scanf("%d", &taskNumber);
	for (int taskIdx = 1; taskIdx <= taskNumber; taskIdx++) {
		scanf("%lld%d", &B, &n);
		bet = vector<long long>(37, 0LL);
		FOR(i, 0, n) scanf("%lld", &bet[i]);
		SORT(bet);
		double res = 0;
		FOR(i, 1, 38) {
			res = max(res, getBest(i));
		}
		printf("Case #%d: %.10lf\n", taskIdx, res);
	}
	return 0;
}
