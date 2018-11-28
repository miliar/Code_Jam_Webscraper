#include <iostream>
#include <cstring>
#include <algorithm>

using namespace std;

int A, B, K;

long long dp[32][2][2][2];
bool go[32][2][2][2];

//try to put a zero
bool flag(bool f, int v, int bit) {
	if((v & (1 << bit)) != 0)
		return true;
	return f;
}

//try to put a 1
bool can(bool f, int v, int bit) {
	if(f == true)
		return true;
	return (v & (1 << bit)) != 0;
}

long long solve(int bit, bool a, bool b, bool k) {
	if(bit < 0)
		return 1;

	if(go[bit][a][b][k])
		return dp[bit][a][b][k];

	long long &val = dp[bit][a][b][k];
	go[bit][a][b][k] = true;

	//bits 0 and 0

	// cout << "go 0 0\n";
	val = solve(bit - 1, flag(a, A, bit), flag(b, B, bit), flag(k, K, bit));

	//case 1 0
	if(can(a, A, bit)) {
		// cout << "go 1 0\n";
		val += solve(bit - 1, a, flag(b, B, bit), flag(k, K, bit));
	}

	//case 0 1
	if(can(b, B, bit)) {
		// cout << "go 0 1\n";
		val += solve(bit - 1, flag(a, A, bit), b, flag(k, K, bit));
	}

	//case 1 1 
	if(can(a, A, bit) && can(b, B, bit) && can(k, K, bit)) {
		// cout << "go 1 1\n";
		val += solve(bit - 1, a, b, k);
	}

	return val;
}

void test() {
	cin >> A >> B >> K;
	memset(go, 0, sizeof(go));
	memset(dp, 0, sizeof(dp));

	A--; B--; K--;

	cout << solve(30, false, false, false) << "\n";
}

int main() {
	int T;
	cin >> T;
	for(int t = 1; t <=  T; t++) {
		cout << "Case #" << t << ": ";
		test();
	}
}