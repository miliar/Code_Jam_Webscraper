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

char S[102];

ll solve(int i, char c, ll N) {
	while(i >= 0 && S[i] == c) --i;
	if(i == -1)
		return N;
	char d = c == '-' ? '+' : '-';
	while(i >= 0 && S[i] != c) --i;
	return solve(i, d, N+1);
}

void docase() {
	scanf("%s", S);
	ll res = solve(strlen(S) - 1, '+', 0);
	printf("%lld\n", res);
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
