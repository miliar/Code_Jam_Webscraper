#include <algorithm>
#include <cctype>
#include <cmath>
#include <cstdio>
#include <cstring>
#include <deque>
#include <iostream>
#include <list>
#include <map>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <vector>

using namespace std;

#define DEBUG(x) cout << ">>> " << #x << " = " << (x) << endl;
#define FOR(i,a,b) for(int i=(a);i<=(b);++i)
#define FORD(i,a,b) for(int i=(a);i>=(b);--i)
#define REP(i,a) for(int i=0;i<(a);++i)

#define INF (1<<29)
typedef long long ll;
typedef unsigned int uint;

int T, N;
char I[40];
map<uint, double> mem;

double solve(uint mask) {
	if (mask == (1U<<N)-1) return 0.0;

	auto it = mem.find(mask);
	if (it != mem.end()) return it->second;

	//fprintf(stderr, "%x\n", mask);
	//fflush(stderr);

	double res = 0.0;
	REP(i,N) {
		int j = i;
		int cost = N;
		while (mask&(1U<<j)) {
			++j; --cost;
			if (j >= N) j = 0;
		}
		uint nmask = mask | (1U<<j);
		res += cost+solve(nmask);
	}

	res /= N;

	mem[mask] = res;
	return res;
}

int main() {
	scanf("%d ", &T);
	REP(t,T) {
		gets(I);
		N = (int)strlen(I);
		uint start = 0;
		REP(i,N) if (I[i] == 'X') start |= 1U << i;
		printf("Case #%d: %.10lf\n", t+1, solve(start));
		mem.clear();
	}
	return 0;
}
