#include <iostream>
#include <map>
using namespace std;

string solve(int n, string rps) {
	map<string, string> left, right;
	left["R"] = "PR"; right["R"] = "RS";
	left["P"] = "PR"; right["P"] = "PS";
	left["S"] = "PS"; right["S"] = "RS";
	left["PR"] = "P"; right["PR"] = "R";
	left["PS"] = "P"; right["PS"] = "S";
	left["RS"] = "R"; right["RS"] = "S";
	if (n == 0) {
		if (rps.size() != 1) {
			cerr << "err" << endl;
		}
		return rps;
	} else {
		return solve(n - 1, left[rps]) + solve(n - 1, right[rps]);
	}
}

string solve(int n, int r, int p, int s) {
	int k = (1<<n) / 3;
	if (r < k || r > k+1 || p < k || p > k+1 || s < k || s > k+1) {
		return "IMPOSSIBLE";
	} else {
		string rps;
		if (p > k) {
			rps += "P";
		}
		if (r > k) {
			rps += "R";
		}
		if (s > k) {
			rps += "S";
		}
		return solve(n, rps);
	}
}

int main() {
	int T; cin >> T;
	for (int No = 1; No <= T; No++) {
		int N, R, P, S; cin>> N >> R >> P >> S;
		string ans = solve(N, R, P, S);
		cout << "Case #" << No << ": " << ans << endl;
	}
	return 0;
}
