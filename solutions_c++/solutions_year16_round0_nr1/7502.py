#include "iostream"
#include "string"
#include "vector"
#include "algorithm"

using namespace std;

struct Solution {
	long long N;

	void mark(long long n, unsigned& unseen) {
		while (n > 0) {
			unseen &= ~(1 << (n % 10));
			n /= 10;
		}
	}
	
	void solve() {
		if (N == 0) cout << "INSOMNIA";
		else {
			unsigned unseen = (1<<10)-1;
			long long n;
			for (n = N; unseen; n+=N) mark(n, unseen);
			cout << n-N;
		}
	}
}
;
int main() {
	int T = 0;
	cin >> T;

	for (int t = 0; t < T; t++) {
		long long N;
		cin >> N;
		cout << "Case #" << t + 1 << ": ";
		Solution{ N }.solve();
		
		cout << endl;
	}

	return 0;
}