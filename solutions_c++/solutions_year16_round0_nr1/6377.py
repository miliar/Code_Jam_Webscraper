#include <cstdio>
#include <algorithm>
#include <vector>
#include <queue>
#include <deque>
#include <stack>
#include <set>
#include <map>
#include <unordered_set>
#include <unordered_map>
#include <string>
#include <cassert>
#include <cmath>
#include <cstring>
#include <functional>
#include <iostream>
using namespace std;
typedef vector<int> VI;
typedef pair<int,int> PII;
typedef vector<PII> VPII;
typedef long long ll;
#define REP(i,a,n) for (int i = (a); i < (n); i++)

ll N;
bool c[10];

bool allcheck() {
	REP(i, 0, 10) 
		if(!c[i]) return false;
	return true;
}

ll solve() {
	ll res = 0;
	int i = 1;
	while(1) {
		res += N;
		ll tmp = res;

		while(tmp > 0) {
			c[tmp%10] = true;
			tmp /= 10;
		}

		if(allcheck()) break;
	}
	return res;
}

void docase() {
	scanf("%lld", &N);
	REP(i, 0, 10) c[i] = false;
	if(N == 0)
		printf("INSOMNIA\n");
	else {
		ll res = solve();
		printf("%lld\n", res);
	}
}

int main() {
	int T;
	scanf("%d ", &T);
	for (int test = 0; test < T; test++) {
		printf("Case #%d: ", test+1);
		docase();
	}
	return 0;
}
