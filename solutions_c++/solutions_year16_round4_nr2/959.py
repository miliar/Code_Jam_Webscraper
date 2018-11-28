#include <iostream>
#include <algorithm>
using namespace std;

static double cache[205][205];
static bool seen[205][205];

static double evaltr(double *np, int K, int req) {
	if(seen[K][req]) return cache[K][req];
	double ans = 1.0;
	if(0 == req) {
		for(int i = 0; i < K; ++i) ans *= 1.0 - np[i];
	} else if(K == req) {
		for(int i = 0; i < K; ++i) ans *= np[i];
	} else {
		ans = (1-np[K-1]) * evaltr(np, K-1, req) + np[K-1] * evaltr(np, K-1, req-1);
	}
	seen[K][req] = true;
	cache[K][req] = ans;
	return ans;
}

static double evaltl(double *np, int K, int req) {
	double dp[205][205] = { {1.0} };

	for(int j = 1; j <= K; ++j) {
		dp[j][0] = dp[j-1][0] * (1.0 - np[j-1]);
	}

	for(int i = 1; i <= req; ++i) {
		dp[0][i] = dp[0][i-1] * np[i-1];
	}

	for(int i = 1; i <= req; ++i)
	for(int j = 1; j <= K; ++j) {
		dp[j][i] = (1 - np[j-1]) * dp[j-1][i] + np[j-1] * dp[j-1][i-1];
	}
	return dp[K][req];
}

static double evalt(double *np, int K) {
	string s2(K/2, '0');
	s2 += string(K/2, '1');
	double ret = 0.0;
	do {
		double v = 1.0;
		int i = 0;
		for(char ch : s2) {
			if(ch == '1') {
				v *= np[i];
			} else {
				v *= (1.0 - np[i]);
			}
			++i;
		}
		ret += v;
	} while(next_permutation(begin(s2), end(s2)));
	return ret;
}

int main() {
  int T;
  std::ios_base::sync_with_stdio(false);
  cin.tie(0);
  cin >> T;
  for(int cn = 1; cn <= T; ++cn) {
cerr << cn << " of " << T << '\n';
    int N, K;
	double ps[205];
	cin >> N >> K;
	for(int i = 0; i < N; ++i) cin >> ps[i];
	sort(&ps[0], &ps[N]);
	double nps[205];
	double ans = 0.0;

	int ignore_list[] = {0, N-K-1};
	double prevnps[205] = {0.0};

	while(ignore_list[0] < N && ignore_list[1] < N) {
		bool isdiff = false;
		for(int i = 0, j = 0; i < N; ++i) {
			if(ignore_list[0] <= i && i <= ignore_list[1]) continue;
			nps[j] = ps[i];
			isdiff |= (nps[j] != prevnps[j]);
			prevnps[j] = nps[j];
			++j;
		}
		if(isdiff) {
			for(int i = 0; i <= K; ++i) for(int j = 0; j <= K; ++j) seen[i][j] = false;
			//const double nt1 = evalt(nps, K);
			const double nt2 = evaltr(nps, K, K/2);
			ans = max(nt2, ans);
		}
		++ignore_list[0];
		++ignore_list[1];
	}

	cout << "Case #" << cn << ": ";
	cout << ans << '\n';
//	cout << ans << " : [N, K] = " << N << ',' << K << " : " << ds << endl;
  }
}
