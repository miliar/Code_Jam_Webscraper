#include <array>
#include <functional>
#include <algorithm>
#include <iostream>
#include <fstream>
#include <sstream>
#include <iomanip>
#include <numeric>
#include <cstring>
#include <cassert>
#include <cstdio>
#include <string>
#include <vector>
#include <bitset>
#include <queue>
#include <stack>
#include <cmath>
#include <ctime>
#include <list>
#include <set>
#include <map>
#include <complex>
using namespace std;

#define FOR(i, a, b) for(int i = a, __up = b; i < __up; ++i)
#define REP(n) FOR(i, 0, n)
#define CLR(a) memset(a, 0, sizeof a)

typedef complex<double> point;
typedef long long ll;

// S E N W
int dx[]={1,0,-1,0};
int dy[]={0,1,0,-1};

int T, D;
// TODO: not enough
#define N 1010
int p[N];

template<typename T, std::size_t NN>
int get(int m, array<T, NN> h) {
	//TODO:
	int i;
	for (i = 9; i > m; --i) {
		if (h[i]) break;
	}
	i-=m;
	if (i <= 3) return i+m;
	int t = get(m+1, h);
	h[(i>>1)+m] += h[i+m];
	h[(i>>1)+(i&1)+m] += h[i+m];
	int add = h[i+m];
	h[i+m] = 0;
	int t2 = get(m, h) + add;

	return min(t, t2);
}


template<typename T, std::size_t NN>
int get(array<T, NN> h) {
	int i;
	for (i = 9; i > 0; --i) {
		if (h[i]) break;
	}
	if (i <= 3) return i;
	array<T, NN> hh=h;
	for (int i=1; i<9; ++i) {
		hh[i] = hh[i+1];
	}
	hh[9] = 0;
	h[i>>1] += h[i];
	h[(i>>1)+(i&1)] += h[i];
	int t = h[i];
	h[i] = 0;
	return min(get(h)+t, get(hh)+1);
}

#define P 1000
array<int, P+10> h;
int solve() {
	cin >> D;
	//TODO:
	int t;
	for(int i = 1; i<=P;++i) h[i] = 0;
	
	int maxp = 0;
	REP(D) {
		cin >> t;
		++h[t];
		maxp = max(maxp, t);
	}

	int mins = maxp;
	for (int i = 1; i < maxp; ++i) {
		int sum = 0;
		for (int j = maxp; j > i; --j) {
			sum += h[j]*(j/i+(!!(j%i))-1);
		}
		mins = min(sum+i, mins);
	}
	return mins;
}
/*
int solve() {
	cin >> D;
	int maxp = 0, maxi=-1;
	for (int i = 0; i < D; ++i) {
		cin >> p[i];
		if (maxp < p[i]) maxp = p[i], maxi = i;
	}
	for (int i = 0; i < maxp; ++i) {}

	if (maxp <= 3) return maxp;

	int ret = 0;
	while (maxp > 3) {
		p[D++] = (maxp >> 1)+1;
		if (maxp & 1) p[maxi] = p[D-1] + 1;
		else p[maxi] = p[D-1];
		++ret;
		maxp = 0, maxi = -1;
		for (int i = 0; i < D; ++i) {
			if (maxp < p[i]-ret) maxp = p[i]-ret, maxi = i;
		}
	}

	return ret+maxp;
}
*/

int main()
{
	cin >> T;
	for (int t = 1; t <= T; ++t) {
		printf("Case #%d: %d\n", t, solve());
	}

	return 0;
}
