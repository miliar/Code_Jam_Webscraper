#include <iostream>
#include <ctime>
#include <fstream>
#include <cmath>
#include <cstring>
#include <cassert>
#include <cstdio>
#include <algorithm>
#include <iomanip>
#include <vector>
#include <stack>
#include <queue>
#include <set>
#include <map>
#include <complex>
#include <utility>
#include <cctype>
#include <list>
#include <bitset>

using namespace std;

#define FORALL(i,a,b) for(int i=(a);i<=(b);++i)
#define FOR(i,n) for(int i=0;i<(n);++i)
#define FORB(i,a,b) for(int i=(a);i>=(b);--i)

typedef long long ll;
typedef double ld;
typedef complex<ld> vec;

typedef pair<int,int> pii;
typedef map<int,int> mii;

#define pb push_back
#define mp make_pair

ll go(int K, int C, vector<int>& digits) {
	int L = digits.size();
	assert(L == C);
	FOR(i,L) assert(1<=digits[i]&&digits[i]<=K);

	ll cur_len = 1;
	FOR(x,C) cur_len *= K;
	assert(cur_len > 0);

	ll ans = 1;
	FOR(i,L) {
		assert((cur_len % K) == 0);
		ans += (digits[i]-1)*(cur_len / K);
		cur_len /= K;
	}

	assert(cur_len == 1);
	return ans;
}

int main() {
	int TEST, K, C, S;
	scanf("%d",&TEST);

	FOR(test,TEST) {
		scanf("%d%d%d",&K,&C,&S);
		//K = rand()%100;
		//S = rand()%K;
		//C = max(1, rand()%((int)(18*log(10)/log(K))));

		printf("Case #%d: ", (test+1));
		int need = (K+C-1) / C;
		if (S < need) {
			printf("IMPOSSIBLE\n");
		} else {
			S = min(S,need);
			bool sp = false;
			FOR(i,S) {
				vector<int> digits(C,0);
				FOR(j,C) digits[j] = min(i*C + j + 1, K);

				if (sp) printf(" ");
				printf("%lld",go(K,C,digits));
				sp = true;
			}
			printf("\n");
		}
	}
}













