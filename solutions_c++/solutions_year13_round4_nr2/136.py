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

long long N, P;

long long getBest(long long remN, long long rank) {
	if (remN == 1) return 0;
	long long back = remN - rank - 1;
	if (!back) return remN - 1;
	return getBest(remN / 2, remN / 2 - (back - 1) / 2 - 1);
}

long long getWorst(long long remN, long long rank) {
	if (remN == 1) return 0;
	long long front = rank;
	if (!front) return 0;
	return getWorst(remN / 2, (front - 1) / 2) + remN / 2;
}

int main() {
	int taskNumber; scanf("%d", &taskNumber);
	for (int taskIdx = 1; taskIdx <= taskNumber; taskIdx++) {
		scanf("%lld%lld", &N, &P);
/*		for (long long rank = 0; rank < 1LL << N; rank++) {
			printf("%lld best = %lld worst = %lld\n", rank, getBest(1LL << N, rank), getWorst(1LL << N, rank));
		}*/
		printf("Case #%d:", taskIdx);
		long long lower, upper, res;
		lower = 0; upper = (1LL << N) - 1; res = -1;
		while (lower <= upper) {
			long long medium = (lower + upper) >> 1;
			if (getWorst(1LL << N, medium) < P) {
				res = medium;
				lower = medium + 1;
			} else {
				upper = medium - 1;
			}
		}
		printf(" %lld", res);
		lower = 0; upper = (1LL << N) - 1; res = -1;
		while (lower <= upper) {
			long long medium = (lower + upper) >> 1;
			if (getBest(1LL << N, medium) < P) {
				res = medium;
				lower = medium + 1;
			} else {
				upper = medium - 1;
			}
		}
		printf(" %lld\n", res);
	}
	return 0;
}
