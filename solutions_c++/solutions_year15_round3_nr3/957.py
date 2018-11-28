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
#define DFOR(i, n) for(int i=(n)-1;i>=0;i--)
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

	FOR(o, T) {

		LL sum = 0; LL kolko = 0;
		
		int C, D, V; scanf("%d %d %d", &C, &D, &V);
		VB dos(V+1, false); dos[0] = true;
		int a; FOR(i, D) {
			scanf("%d", &a); 
			DFOR(i, V) 
				if ((dos[i]) && ((i + a) <= V) && (!dos[i+a])) 
					dos[i+a] = true;
		}

		For(i, 1, V+1) {
			if (dos[i]) cc;

			sum++;
			DFOR(j, V)
				if ((dos[j]) && ((j + i) <= V) && (!dos[j+i]))
					dos[j+i] = true;
		}

		printf("Case #%d: %lld\n", o+1, sum);
	}

	return 0;
}