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

const int MOD = 1000002013;

template<int MOD = 1000002013> struct ModInteger {
	int x;
	ModInteger(int x = 0) : x(x) {}
	int getValue() { return x; }
	void operator = (const int v) { x = v; }
	ModInteger operator + (const int v) { return ModInteger(x >= MOD - v ? x - MOD + v : x + v); }
	ModInteger operator + (const ModInteger &rhs) { return ModInteger(x >= MOD - rhs.x ? x - MOD + rhs.x : x + rhs.x); }
	void operator += (const int v) { x = x >= MOD - v ? x - MOD + v : x + v; }
	void operator += (const ModInteger &rhs) { x = x >= MOD - rhs.x ? x - MOD + rhs.x : x + rhs.x; }
	ModInteger operator - (const int v) { return ModInteger(x < v ? x - v + MOD : x - v); }
	ModInteger operator - (const ModInteger &rhs) { return ModInteger(x < rhs.x ? x - rhs.x + MOD : x - rhs.x); }
	void operator -= (const int v) { x = x < v ? x - v + MOD : x - v; }
	void operator -= (const ModInteger &rhs) { x = x < rhs.x ? x - rhs.x + MOD : x - rhs.x; }
	ModInteger operator * (const int v) { return ModInteger((long long)x * v % MOD); }
	ModInteger operator * (const ModInteger &rhs) { return ModInteger((long long)x * rhs.x % MOD); }
	void operator *= (const int v) { x = (long long)x * v % MOD; }
	void operator *= (const ModInteger &rhs) { x = (long long)x * rhs.x % MOD; }
	ModInteger operator ^ (int e) { ModInteger res = ModInteger(1), a = *this; for ( ; e; e >>= 1, a *= a) if (e & 1) res *= a; return res; }
	void operator ^= (int e) { ModInteger res = ModInteger(1), a = *this; for ( ; e; e >>= 1, a *= a) if (e & 1) res *= a; x = res.x; }
	ModInteger operator / (const int v) { return ModInteger((long long)x * (ModInteger(v) ^ (MOD - 2)).getValue() % MOD); }
	ModInteger operator / (const ModInteger &rhs) { ModInteger a = rhs; return ModInteger((long long)x * (a ^ (MOD - 2)).getValue() % MOD); }
	void operator /= (const int v) { x = (long long)x * (ModInteger(v) ^ (MOD - 2)).getValue() % MOD; }
	void operator /= (const ModInteger &rhs) { ModInteger a = rhs; x = (long long)x * (a ^ (MOD - 2)).getValue() % MOD; }
};

int N, M;
map<int, long long> inMap, outMap, remCnt;
ModInteger<> newCost, cost;

void calcCost(ModInteger<> &cost, long long n, long long o, long long e) {
	if (o != e) {
		long long m = e - o;
		if (m & 1) {
			cost += ModInteger<>(((N * 2 - m + 1) / 2 % MOD + MOD) % MOD) * ModInteger<>(m % MOD) * ModInteger<>(n % MOD);
		} else {
			cost += ModInteger<>(((N * 2 - m + 1) % MOD + MOD) % MOD) * ModInteger<>(m / 2 % MOD) * ModInteger<>(n % MOD);
		}
	}
}

int main() {
	int taskNumber; scanf("%d", &taskNumber);
	for (int taskIdx = 1; taskIdx <= taskNumber; taskIdx++) {
		newCost = ModInteger<>();
		cost = ModInteger<>();
		inMap.clear();
		outMap.clear();
		remCnt.clear();
		scanf("%d%d", &N, &M);
		FOR(_, 0, M) {
			int o, e, p; scanf("%d%d%d", &o, &e, &p);
			inMap[o] += p;
			outMap[e] += p;
			calcCost(cost, p, o, e);
		}
		map<int, long long>::const_iterator it = inMap.begin(), jt = outMap.begin();
		while (it != inMap.end() || jt != outMap.end()) {
			remCnt[-it->first] += it->second;
			it++;
			while (jt != outMap.end() && (it == inMap.end() || jt->first < it->first)) {
				long long rem = jt->second;
				while (rem) {
					if (remCnt.begin()->second <= rem) {
						calcCost(newCost, remCnt.begin()->second, -remCnt.begin()->first, jt->first);
						rem -= remCnt.begin()->second;
						remCnt.erase(remCnt.begin());
					} else {
						calcCost(newCost, rem, -remCnt.begin()->first, jt->first);
						remCnt.begin()->second -= rem;
						rem = 0;
					}
				}
				jt++;
			}
		}
		printf("Case #%d: %d\n", taskIdx, (cost - newCost).getValue());
	}
	return 0;
}
