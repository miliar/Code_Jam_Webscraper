#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<cmath>

#include<algorithm>
#include<utility>
#include<string>

#include<deque>
#include<list>
#include<map>
#include<queue>
#include<set>
#include<stack>
#include<vector>

using namespace std;

#define REP(i,N) for (int i = 0; i < (N); i++)
#define FOR(i, a, b) for (int i = (a); i < (b); i++)
#define FORD(i, b, a) for (int i = (b) - 1; i >= a; i--)
#define DP(arg...) fprintf(stderr, ## arg) //COMPILER SPECIFIC!!!

typedef long long ll;

int T;
int S_max;
char str[10000];

void solve(int _case) {
	int sol = 0;
	scanf(" %d %s", &S_max, str);
	int prf_s = 0;
	for (int shyness = 0; shyness <= S_max; shyness++) {
		str[shyness] -= '0';
		if (shyness > prf_s)
			sol = max(sol,shyness-prf_s);

		prf_s += str[shyness];
	}


	printf("Case #%d: %d\n", _case, sol);
}

int main() {
	scanf("%d", &T);
	REP(t,T) solve(t+1);
	return 0;
}
