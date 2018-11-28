#include <iostream>
#include <vector>
#include <sstream>
#include <cstdio>
#include <string>
#include <queue>
#include <map>
#include <set>
#include <algorithm>
#include <functional>
#include <deque>
#include <cmath>
#include <math.h>
#include <stack>
#include <time.h>

#define FOR(i, n) for(int i=0;i<(n);i++)
#define For(i, a, n) for(int i=(a);i<(n);i++)
#define itFOR(it, S) for(auto it=S.begin();it!=S.end();++it)
#define range(x) x.begin(), x.end()
#define cc continue
#define LL long long
#define MKP make_pair
#define PII pair<int, int>
#define PLL pair<LL, LL>
#define VI vector<int>
#define VLL vector<LL>
#define VB vector<bool>
#define VS vector<string>
#define pb push_back
#define LD long double
#define INFIN 1000000000000000001

using namespace std;

int main() {

	int T; scanf("%d", &T);

	FOR(p, T) {

		LL sum = 0; LL kolko = 0;
		int mx; string s; cin >> mx >> s;

		FOR(i, mx+1) {
			int wh = s[i] - '0';

			if (kolko < i) {
				int k = i - kolko;
				sum += k;
				kolko += k;
			}
			kolko += wh;
		}

		printf("Case #%d: %lld\n", p+1, sum);
	}

	return 0;
}