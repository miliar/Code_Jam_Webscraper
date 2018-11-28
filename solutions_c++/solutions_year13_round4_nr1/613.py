// start: fa7bb87dcb078e6776e50dcb658bff0d
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <ctype.h>
#include <queue>
#include <algorithm>
#include <vector>
#include <string>
#include <utility>
#include <iostream>
#include <vector>
using namespace std;
typedef vector<int> vi;
typedef vector<vi> vvi;

#define TRACE(x...)
#define PRINT(x...) TRACE(printf(x))
#define WATCH(x) TRACE(cout << #x" = " << x << endl)

#define all(v) (v).begin(), (v).end()
#define rall(v) (v).rbegin(), (v).rend()

#define _FOR(it, b, e) for (decltype(b) it = (b); it != (e); ++it)
#define foreach(x...) _FOR(x)
#define fu(i, a) foreach(i, 0, a)
#define forall(i, v) foreach(i, all(v))

#define MSET(c, v) memset(c, v, sizeof(c))

#define pb push_back
#define sz(c) int((c).size())

const int INF = 0x3F3F3F3F; const int NEGINF = 0xC0C0C0C0;
const double EPS = 1e-10;

inline int cmp(double x, double y = 0, double tol = EPS) {
  return (x <= y + tol) ? (x + tol < y) ? -1 : 0 : 1;
}

const long long MAGIC = 1000002013ll;
typedef vector<pair<long long, long long> > vll;

long long cost(const vll& V, long long N) {
	long long ans = 0;
	for (auto&x : V) {
		long long K = x.second - x.first;
		long long temp = (K*(2ll*N + 1ll - K)/2ll) % MAGIC;
		ans = (ans + temp) % MAGIC;
	}
	return ans;
}

int main() {
	int __;
	scanf("%d", &__);
	fu(_,__) {
		printf("Case #%d:", _+1);
		int N, M;
		scanf("%d %d", &N, &M);

		vll V;
		fu(j, M) {
			long long A, B, C;
			scanf("%lld %lld %lld", &A, &B, &C);
			fu(i, C) V.push_back(make_pair(A,B));
		}

		M = V.size();

		sort(all(V));

		long long bef = cost(V, N);

		fu(i, M) {
			int cur = i+1;
			while (true) {
				int sw = -1;
				while (cur < M && V[cur].first <= V[i].second) {
					if (sw == -1 || V[cur].second >= V[sw].second) sw = cur;
					cur++;
				}
				if (sw == -1) break;
				if (V[sw].second <= V[i].second) break;
				swap(V[i].second, V[sw].second);
			}
		}
		long long aft = cost(V, N);
		printf(" %lld\n", (bef - aft)%MAGIC);
	}
	return 0;
}
