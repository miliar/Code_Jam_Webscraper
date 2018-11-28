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
int P;
i64 Ei[10100], Fi[10100];
pair<i64, i64> S[10100];

vector<pair<i64, i64>> S2, St;

void reduce(i64 W)
{
	// W > 0
	St.clear();

	map<i64, i64> prev;

	for (int i = 0; i < S2.size(); ++i) {
		i64 cnt = S2[i].second - prev[S2[i].first - W];
		if (cnt > 0) St.push_back(make_pair(S2[i].first, cnt));
		prev.insert(make_pair(S2[i].first, cnt));
	}

	S2 = St;
}

bool reduce2(i64 W)
{
	i64 W2 = W < 0 ? -W : W;

	St.clear();

	map<i64, i64> prev;
	bool is_zero = false;

	for (int i = 0; i < S2.size(); ++i) {
		i64 cnt = S2[i].second - prev[S2[i].first - W2];
		if (cnt > 0) {
			if (W > 0) St.push_back(make_pair(S2[i].first, cnt));
			else St.push_back(make_pair(S2[i].first - W, cnt));
		}

		prev.insert(make_pair(S2[i].first, cnt));
	}

	for (auto &a : St) if (a.first == 0) is_zero = true;

	if (!is_zero) return false;
	S2 = St;
	return true;
}

int main()
{
	scanf("%d", &T);
	for (int t = 0; t++ < T;){
		scanf("%d", &P);
		for (int i = 0; i < P; ++i) scanf("%lld", Ei + i);
		for (int i = 0; i < P; ++i) scanf("%lld", Fi + i);

		for (int i = 0; i < P; ++i) S[i] = make_pair(Ei[i], Fi[i]);
		sort(S, S + P);

		int nZero = 0;
		while (S[0].second % 2 == 0) {
			++nZero;
			for (auto& x : S) x.second /= 2;
		}
		S2.clear();
		for (int i = 0; i < P; ++i) S2.push_back(S[i]);

		vector<i64> cand, ret;
		int c = 0;
		while(S2.size() > 1) {
			cand.push_back(S2[1].first - S2[0].first);
			reduce(S2[1].first - S2[0].first);

			// for (auto& a : S2) printf("%lld/%lld ", a.first, a.second); puts("");
		}
		// for (auto a : cand) printf("%lld ", a); puts("");
		sort(cand.begin(), cand.end());

		S2.clear();
		for (int i = 0; i < P; ++i) S2.push_back(S[i]);

		for (int i = cand.size() - 1; i >= 0; --i) {
			if (reduce2(-cand[i])) {
				ret.push_back(-cand[i]);
			} else {
				reduce2(cand[i]);
				ret.push_back(cand[i]);
			}
		}
		
		for (int i = 0; i < nZero; ++i) ret.push_back(0);

		sort(ret.begin(), ret.end());
		printf("Case #%d:", t);
		for (i64 a : ret) printf(" %lld", a);
		puts("");
	}

	return 0;
}
