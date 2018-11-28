#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
long long f(int n, long long m) {
	if (n == 0) return 0;
	if (m == 0) return 0;
	return f(n-1, (m-1)/2) + (1LL << (n-1));
}
long long func1(int N, long long P) {
	if (P == 1) return 0;
	if (P == (1LL << N)) return (1LL << N) - 1;
	for (int i = 1; i <= N; ++ i) {
		if (P <= f(N, (1LL<<i)-2)) return (1LL<<(i-1))-2;
	}
	return (1LL<<N)-2;
}
long long g(int n, long long m) {
	if (n == 0) return 0;
	if (m == 0) return 0;
	if (m == (1LL << n) - 1) return (1LL << n) - 1;
	return g(n-1, (m-1)/2+1);
}
long long func2(int N, long long P) {
	if (P == 1) return 0;
	if (P == (1LL << N)) return (1LL << N) - 1;
	for (int i = N-1; i > 0; -- i) {
		if (P <= g(N, (1LL<<N)-(1LL<<i))) return (1LL<<N)-(1LL<<(i+1));
	}
	return (1LL<<N)-2;
}
pair<long long, long long> solve(int N, long long P) {
	return make_pair(func1(N, P), func2(N, P));
}
int main() {
	int T;
	cin >> T;
	for (int tt = 1; tt <= T; ++ tt) {
		int N;
		long long P;
		cin >> N >> P;
		auto r = solve(N, P);
		cout << "Case #" << tt << ": " << r.first << " " << r.second << endl;
	}
}
