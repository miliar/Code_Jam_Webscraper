#include <cstdio>
#include <iostream>
#include <cstring>
#include <string>
#include <algorithm>
#include <vector>
#include <queue>
#include <set>
#include <map>
using namespace std;

#define mp make_pair
#define pb push_back
typedef long long ll;

ll N, M;
vector<ll> Q;

double check(ll mid) {
	ll out = mid * (37 - M);
	ll tot = (37 - M);
	for (ll i=0; i<M; i++)
		if (Q[i] <= mid) out += mid - Q[i], tot++;
	if (out > N) return -1;

	//printf("==%lld %lld\n", out, tot);
	double ans = 0;
	for (ll i=0; i<=tot; i++) {
		double in = 0;
		if (i < (tot - (37 - M))) {
			in = mid * 36 * ((double)(37 - M) / (double)(tot - i));
			//printf("==%lld %lld %lf\n", (37 - M), (tot - i), in);
			ll xx = 0;
			for (ll j=0; j<M; j++)
				if (Q[j] > mid) break;
				else {
					xx ++;
					if (xx > ((tot - (37 - M)) - i)) break;
					in += (mid - Q[j]) * 36.0 / (double)(tot - i);
				}
		} else if (M < 37) {
			in = mid * 36;
		}
		if (in - out > ans) ans = in - out;
		out++;
		if (out > N) break;
	}
	return ans;
}

int main() {
	int T, TC = 1;
	scanf("%d", &T);
	while (T--) {
		scanf("%lld%lld", &N, &M);
		Q.clear();
		for (ll i=0; i<M; i++) {
			ll tem;
			scanf("%lld", &tem);
			Q.pb(tem);
		}
		sort(Q.begin(), Q.end());


		//for (ll i=0; i<M; i++) printf("=%lld ", Q[i]); puts("");
		double ans = 0;
		if (M == 0) ans = 0;
		else if ((Q[0] - 1) * (37 - M) > N) {
			//puts("H");
			ans = max(0ll, (N / (37 - M)) * 36 - (N / (37 - M)) * (37 - M));
		} else {
			//puts("HH");
			ll last = 0, out = 0;
			for (ll i=0; i<M; i++) {
				ll tem = Q[i] - 1 - last;
				if (out + (37 - M + i) * tem> N) {
					tem = (N - out) / (37 - M + i);
				}
				out += (37 - M + i) * tem;
				if (out > N) break;

				//printf("out 1: %lld %lld %lld\n", i, tem, out);
				double in = 0;
				if ((37 - M + i) > 0) {
					in = (last + tem) * 36 * ((double)(37 - M) / (double)(37 - M + i));
					for (ll j=0; j<i; j++) {
						in += (last + tem - Q[j]) * 36 / (double)(37 - M + i);
					}
				}
				//printf("in 1: %lld %lf\n", i, in);
				if (in - out > ans) ans = in - out;

				out += (37 - M + i);
				if (out > N) break;
				//printf("out 2: %lld %lld %lld\n", i, tem, out);
				ll j = i;
				while (j < M && Q[j] == Q[i]) j++;
				i = j - 1;
				tem = Q[i] - 1 - last;
				in = Q[i] * 36 * ((double)(37 - M) / (double)(38 - M + i));
				//printf("%lld %lld %lf\n", i, 38 - M + i, in);
				for (ll j=0; j<i; j++) {
					in += (Q[i] - Q[j]) * 36 / (double)(38 - M + i);
				}
				//printf("in 2: %lld %lf\n", i, in);
				if (in - out > ans) ans = in - out;

				ll out2 = out;
				ll k = 1;
				for (j=min(i, N - out); j>=1; j--, k++) {
					out2++;
					in = Q[i] * 36 * ((double)(37 - M) / (double)(38 - M + i - k));
					for (ll j=0; j<i-k; j++) {
						in += (Q[i] - Q[j]) * 36 / (double)(38 - M + i - k);
					}
					if (in - out2 > ans) ans = in - out2;
				}
				last = Q[i];
			}

			
			
		}

		ll L=0;
			ll R=Q[M-1];
			while (L < R) {
				ll mid = (L + R) / 2;
				double t = check(mid);
				if (t < 0) R = mid - 1;
				else {
					ans = max(ans, t);
					if (mid > 1) {
						t = check(mid - 1);
						ans = max(ans, t);
					}
					if (mid > 2) {
						t = check(mid - 2);
						ans = max(ans, t);
					}
					if (mid > 3) {
						t = check(mid - 3);
						ans = max(ans, t);
					}
					t = check(mid +1);
						ans = max(ans, t);
					t = check(mid +2);
						ans = max(ans, t);
						t = check(mid + 3);
						ans = max(ans, t);
					L = mid + 1;
				}
			}
			
		printf("Case #%d: %.8lf\n", TC++, ans);
	}
}