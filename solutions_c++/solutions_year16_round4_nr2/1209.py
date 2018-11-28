#include <vector>
#include <string>
#include <iostream>
#include <algorithm>
#include <numeric>
#include <map>
#include <set>
#include <string.h>

typedef long long ll;
using namespace std;

void printv(const vector<int> &v) {
	int n = v.size();
	for (int i = 0; i < n; i++) {
		cout << " " << v[i];
	}
	cout << endl;
}

bool iszero(const vector<int> &v) {
	int n = v.size();
	for (int i = 0; i < n; i++) {
		if (v[i] != 0)
			return false;
	}
	return true;
}

void incr(vector<int> &v) {
	int n = v.size();
	for (int i = 0; i < n; i++) {
		v[i]++;
		if (v[i] < 3) {
			return;
		}
		v[i] = 0;
	}
}

int count(const vector<int> &v, int w) {
	int n = v.size();
	int c = 0;
	for (int i = 0; i < n; i++) {
		if (v[i] == w)
			c++;
	}
	return c;
}

double solve(int K, const vector<double> &P) {
	int N = P.size();
	double ans = 0.0;

	for (int i = 0; i < (1<<N); i++) {
		if (__builtin_popcount(i) != K)
			continue;
		double d = 0.0;
		for (int j = 0; j < (1<<K); j++) {
			if (__builtin_popcount(j) != K/2)
				continue;
			double e = 1.0;
			for (int k = 0; k < K; k++) {
				int b;
				int c = 0;
				for (b = 0;; b++) {
					if (i&(1<<b)) {
						if (c == k)
							break;
						c++;
					}
				}
				if (j&(1<<k)) {
					e *= P[b];
				} else {
					e *= 1.0 - P[b];
				}
			}
			d += e;
		}
		ans = max(ans, d);
	}

	return ans;
}

int main()
{
	int T;
	cin >> T;
	for (int i = 0; i < T; i++) {
		int N, K;
		cin >> N >> K;
		vector<double> P;
		for (int j = 0; j < N; j++) {
			double d;
			cin >> d;
			P.push_back(d);
		}
		double ans = solve(K, P);
		std::cout.setf(std::ios_base::fixed,std::ios_base::floatfield);
		cout.precision(17);
		cout << "Case #" << i+1 << ": " << ans << endl;
	}
}
