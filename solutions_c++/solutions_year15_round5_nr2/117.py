
#include <iostream>
#include <algorithm>
#include <vector>
#include <queue>
#include <stack>
#include <utility>
#include <cassert>
using namespace std;

#define range(i,a,b) for(int i = (a), _n = (b); i < _n; ++i)
#define fo(i,n) range(i, 0, n)

typedef long long ll;
typedef pair<ll, ll> pr;

const int MAX_N = 1100, MAX_K = 110;
ll N, K, sums[MAX_N];
vector<ll> seq[MAX_K];

ll solve() {
	fo(i,K) seq[i].clear();
	fo(i,K) {
		int j = i;
		ll v = 0;
		seq[i].push_back(v);
		while (j+K < N) {
			v += sums[j+1] - sums[j];
			j += K;
			seq[i].push_back(v);
		}
	}

	vector<ll> seqMin, seqMax;
	fo(i,K) {
		ll mx = 0, mn = 0;
		fo(j,seq[i].size()) mx = max(mx, seq[i][j]), mn = min(mn, seq[i][j]);
		seqMin.push_back(mn);
		seqMax.push_back(mx);
	}

	vector<ll> seqStart, seqValue;
	ll biggestValue = 0;
	fo(i, K) {
		seqStart.push_back(-seqMin[i]);
		assert(seqStart.back() >= 0);
		seqValue.push_back(seqMax[i] + seqStart[i]);
		assert(seqValue.back() >= 0);
		//cout << seqStart.back() << ' ' << seqValue.back() << endl;
		biggestValue = max(biggestValue, seqValue.back());
	}

	ll startSum = 0;
	fo(i, K) startSum += seqStart[i];

	ll rem = (sums[0] - startSum + 10000000LL * K) % K;
	//ll rem = sums[0];
	//while (rem < 0) rem += K;
	//while (rem >= K) rem -= K;
	assert(rem >= 0 && rem < K);
	
	ll wiggle = 0;
	fo(i, K) {
		wiggle += biggestValue - seqValue[i];
	}
	//cout << wiggle << endl;

	if (wiggle < rem) biggestValue++;

	return biggestValue;
}

int main() {

	int T;
	cin >> T;
	range(testCase, 1, T+1) {
		cin >> N >> K;
		fo(i,N) sums[i] = 0;
		fo(i, N-K+1) cin >> sums[i], sums[i] += 10000LL * K;
		cout << "Case #" << testCase << ": " << solve() << endl;
	}

}
