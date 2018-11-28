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
#define DFOR(i, n) for(int i=((n)-1);i>=0;i--)
#define DFor(i, n, a) for(int i=((n)-1);i>=(a);i--)
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
#define INTFIN 1000000047

using namespace std;

int horne_deleno(int wh, int cim) {
	int ret = wh / cim;
	if ((wh % cim) > 0) ret++;

	return ret;
}

VI A;

int main() {

	int T; scanf("%d", &T);

	FOR(p, T) {

		int sum = INTFIN;
		int n; scanf("%d", &n);
		int mx = 0;
		A.resize(n); FOR(i, n) {scanf("%d", &A[i]); mx = max(mx, A[i]);}

		//i -> kolko normalnych minut prejde
		DFor(norm, mx+1, 1) {
			//ak prejde tolko normalnych, kolko presunuti musi byt
			int pres = 0;
			FOR(i, n) {
				if (A[i] <= norm) cc;

				pres += horne_deleno(A[i], norm) - 1;
			}

			sum = min(sum, norm+pres);
		}

		printf("Case #%d: %d\n", p+1, sum);
	}

	return 0;
}