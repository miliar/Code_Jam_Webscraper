#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <stack>
#include <queue>
#include <set>
#include <map>
using namespace std;
#define MOD
#define ADD(X,Y) ((X) = ((X) + (Y)%MOD) % MOD)
typedef long long i64; typedef vector<int> ivec; typedef vector<string> svec;

int T;
int N;
i64 D, Rs, Rm, As, Am, Cs, Cm;
i64 S0, M0;
i64 S[1010101], M[1010101];

vector<pair<i64, int> > sal;
vector<int> child[1010101];

vector<pair<i64, int> > eve;

void visit(int p, i64 lo, i64 hi)
{
	if (hi - lo <= D) {
		eve.push_back(make_pair(lo, 1));
		eve.push_back(make_pair(hi - D, 0));
	}

	for (int q : child[p]) {
		visit(q, min(lo, S[q]), max(hi, S[q]));
	}
}

int main()
{
	scanf("%d", &T);
	for (int t = 0; t++ < T;){
		scanf("%d%lld", &N, &D);
		scanf("%lld%lld%lld%lld", &S0, &As, &Cs, &Rs);
		scanf("%lld%lld%lld%lld", &M0, &Am, &Cm, &Rm);

		for (int i = 0; i < N; ++i) {
			child[i].clear();
			S[i] = S0;
			M[i] = M0;

			S0 = (S0 * As + Cs) % Rs;
			M0 = (M0 * Am + Cm) % Rm;

			if (i > 0) {
				M[i] %= i;
				child[M[i]].push_back(i);
			}
			sal.push_back(make_pair(S[i], i));
		}

		eve.clear();
		visit(0, S[0], S[0]);

		sort(eve.begin(), eve.end());

		int ret = 0, p = 0;
		for (auto &x : eve) {
			if (x.second == 0) ++p;
			else --p;

			ret = max(ret, p);
		}
		fprintf(stderr, "%d\n", t);
		printf("Case #%d: %d\n", t, ret);
	}

	return 0;
}
